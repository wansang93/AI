#%%
import urllib.parse
import os
import pandas as pd
import logging
import io
import re
import csv

#%%
from io import BytesIO
from openpyxl import load_workbook
import os
import urllib.parse
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#%%
# 로컬 파일 경로에서 bucket_name, full_path, file_name 추출
def get_file_info(local_file_path):
    try:
        # URL 인코딩된 문자열일 경우 디코딩
        full_path = urllib.parse.unquote_plus(local_file_path, encoding='utf-8')
        _, file_name = os.path.split(full_path)
        bucket_name = None  # 로컬이므로 bucket 개념 없음
        logger.info(f"Retrieved file info: full_path={full_path}, file_name={file_name}")
        return bucket_name, full_path, file_name
    except Exception as e:
        logger.error(f"Error getting file info: {e}")
        raise e


#%%
# 로컬 파일에서 엑셀 파일 읽기
def get_excel_file(full_path):
    try:
        with open(full_path, "rb") as f:
            excel_data = f.read()
        logger.info(f"Loaded Excel file from local path={full_path}")
        return excel_data
    except Exception as e:
        logger.error(f"Error loading Excel file: {e}")
        raise e

#%%
# 엑셀 데이터를 DataFrame으로 변환 후 TSV 형식으로 가공하는 함수
def convert_to_tsv(excel_data):
    try:
        all_sheets = pd.read_excel(
            io.BytesIO(excel_data),
            engine="openpyxl",
            header=1,
            sheet_name=None,
            dtype=str
        )

        df = pd.concat(all_sheets.values(), ignore_index=True)
        logger.info(f"Excel all sheets read into DataFrame with shape {df.shape}")
        tsv_buffer = io.StringIO()
        df.to_csv(
            tsv_buffer,
            sep="\t",
            index=False,
            encoding="utf-8",
            quoting=csv.QUOTE_NONE,
            escapechar="\\"
        )
        logger.info(f"Converted DataFrame to TSV format")
        return tsv_buffer.getvalue()

    except Exception as e:
        logger.error(f"Error converting Excel to TSV: {e}")
        raise

#%%
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#%%
# 변환된 TSV 데이터를 로컬에 저장하는 함수
def save_tsv_to_local(tsv_data, full_path, output_dir="./output"):
    try:
        if tsv_data is None:
            logger.warning("TSV data is None. Skipping save.")
            return
        
        # 디렉토리가 없으면 생성
        os.makedirs(output_dir, exist_ok=True)

        base_name, _ = os.path.splitext(os.path.basename(full_path))
        local_path = os.path.join(output_dir, f"rev_{base_name}.tsv")

        with open(local_path, "w", encoding="utf-8") as f:
            f.write(tsv_data)

        logger.info(f"Saved TSV file locally: {local_path}")
        return local_path
    except Exception as e:
        logger.error(f"Error saving TSV locally: {e}")
        raise e

#%%
if __name__ == "__main__":
    local_file_path = "./FY2023 대웅출고.xlsx"
    excel_data = get_excel_file(local_file_path)
    tsv_data = convert_to_tsv(excel_data)
    save_tsv_to_local(tsv_data, local_file_path)

# # Lambda 핸들러 함수: 전체 실행 흐름 제어
# def lambda_handler(event, context):
#     try:
#         logger.info("Lambda function triggered")
#         bucket_name, full_path, file_name = get_file_info(event)
#         excel_data = get_excel_file(bucket_name, full_path)
#         tsv_data = convert_to_tsv(file_name, excel_data)
#         upload_tsv_to_s3(tsv_data, bucket_name, full_path)
#         return {
#             'statusCode': 200,
#             'body': 'Lambda call executed successfully'
#         }
#     except Exception as e:
#         logger.error(f"Lambda function failed: {e}")
#         return {
#             'statusCode': 400,
#             'body': f'''\
#                     Lambda call failed
#                     Error: {str(e)}
#                     '''
#             }

        # upload_date = extract_date_from_filename(file_name)
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


# %%
