import boto3
import urllib.parse
import os
import pandas as pd
import logging
import io
import re
import csv

from io import BytesIO
from openpyxl import load_workbook

logger = logging.getLogger()
logger.setLevel(logging.INFO)

S3 = boto3.client('s3')

# S3 이벤트에서 파일 경로와 파일명을 추출하는 함수
def get_file_info(event):
    try:
        encoded_full_path = event['Records'][0]['s3']['object']['key']
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        full_path = urllib.parse.unquote(encoded_full_path, encoding='utf-8')
        _, file_name = os.path.split(full_path)
        logger.info(f"Retrieved file info: bucket={bucket_name}, full_path={full_path}, file_name={file_name}")
        return bucket_name, full_path, file_name
    except Exception as e:
        logger.error(f"Error getting file info: {e}")
        raise e

# S3에서 엑셀 파일을 다운로드하는 함수
def get_excel_file(bucket_name, full_path):
    try:
        excel_object = S3.get_object(Bucket=bucket_name, Key=full_path)
        excel_data = excel_object['Body'].read()
        logger.info(f"Downloaded Excel file from bucket={bucket_name}, key={full_path}")
        return excel_data
    except Exception as e:
        logger.error(f"Error downloading Excel file: {e}")
        raise e

# 엑셀 데이터를 DataFrame으로 변환 후 TSV 형식으로 가공하는 함수
def convert_to_tsv(file_name, excel_data):
    try:
        # upload_date = extract_date_from_filename(file_name)
        df = pd.read_excel(io.BytesIO(excel_data), engine='openpyxl', header=1).astype(str)
        logger.info(f"Excel data read into DataFrame with shape {df.shape}")
                tsv_buffer = io.StringIO()
        logger.info(f"Columns after processing: {df.columns.tolist()}")
        df.to_csv(
            tsv_buffer,
            sep='\t',
            index=False,
            encoding='utf-8',
            quoting=csv.QUOTE_NONE,
            escapechar='\\'
        )
        tsv_data = tsv_buffer.getvalue()
        logger.info(f"Converted DataFrame to TSV format")
        return tsv_data
    except Exception as e:
        logger.error(f"Error converting Excel to TSV: {e}")
        raise e
        # f = df.loc[:, ~df.columns.duplicated()]
        # if 'Month' in df.columns:
        #     df['Month'] = df['Month'].astype(str).str.replace('월', '', regex=False)
        #     df['Month'] = df['Month'].str.lstrip('0')
        #     logger.info("'Month' column has been converted.")
        # else:
        #     logger.info("'Month' column does not exist. Skipping conversion.")
        # if upload_date:
        #     df['UploadDate'] = upload_date
        #     logger.info("'UploadDate' column has been added.")
        # else:
        #     logger.warning("'UploadDate' column could not be added due to missing date information.")
        # if '#' in df.columns:
        #     df = df.drop(columns=['#'])
        #     logger.info("'#' column has been removed.")
        # else:
        #     logger.info("'#' column does not exist. Skipping removal.")
        # if 'UploadDate' in df.columns:
        #     df['UploadDate'] = (
        #         pd.to_datetime(df['UploadDate'], format='%Y%m%d', errors='coerce')
        #         .dt.strftime('%Y-%m-%d')
        #     )

        #     cols = df.columns.tolist()
        #     cols.insert(0, cols.pop(cols.index('UploadDate')))
        #     df = df[cols]
        #     logger.info("'UploadDate' column has been converted to YYYY-MM-DD and moved to the front.")
        # else:
        #     logger.warning("'UploadDate' column does not exist. Skipping reordering.")
        # df = df.fillna("")
        # df.fillna("", inplace=True)
        # df.replace(["nan", "NaN", "nat", "NaT"], "", inplace=True)
        # df.replace('\t', ' ', regex=True, inplace=True)
        # df.replace('\r', ' ', regex=True, inplace=True)
        # df.replace('\n', ' ', regex=True, inplace=True)


# # 파일명에서 업로드 날짜(YYYYMMDD)를 추출하는 함수
# def extract_date_from_filename(file_name):
#     try:
#         base_name, _ = os.path.splitext(file_name)
#         match = re.search(r'(\d{8})$', base_name)
#         if match:
#             date_str = match.group(1)
#             logger.info(f"Extracted date from filename: {date_str}")
#             return date_str
#         else:
#             logger.warning(f"No date found in filename: {file_name}")
#             return None
#     except Exception as e:
#         logger.error(f"Error extracting date from filename: {e}")
#         return None

# 변환된 TSV 데이터를 S3에 업로드하는 함수
def upload_tsv_to_s3(tsv_data, bucket_name, file_name):
    try:
        if tsv_data is None:
            logger.warning("TSV data is None. Skipping upload.")
            return
        tsv_buffer = BytesIO(tsv_data.encode())
        base_name, ext = os.path.splitext(file_name)
        # s3_path = f"monthly_data_rev/{base_name}.tsv"
        s3_path = f"monthly_data_rev/raw_data_final.tsv"
        S3.upload_fileobj(tsv_buffer, bucket_name, s3_path)
        logger.info(f"Uploaded TSV file to bucket={bucket_name}, key={s3_path}")
    except Exception as e:
        logger.error(f"Error uploading TSV to S3: {e}")
        raise e

# Lambda 핸들러 함수: 전체 실행 흐름 제어
def lambda_handler(event, context):
    try:
        logger.info("Lambda function triggered")
        bucket_name, full_path, file_name = get_file_info(event)
        excel_data = get_excel_file(bucket_name, full_path)
        tsv_data = convert_to_tsv(file_name, excel_data)
        upload_tsv_to_s3(tsv_data, bucket_name, file_name)
        return {
            'statusCode': 200,
            'body': 'Lambda call executed successfully'
        }
    except Exception as e:
        logger.error(f"Lambda function failed: {e}")
        return {
            'statusCode': 400,
            'body': f'''\
                    Lambda call failed
                    Error: {str(e)}
                    '''
            }
