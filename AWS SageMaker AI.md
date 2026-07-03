# SageMaker 가이드 목차

## 1. 서론

### 📌 가이드 목적 및 대상

#### 목적

Amazon SageMaker를 이해하고 활용할 수 있도록 안내

#### 대상

- ML/AI 프로젝트에 새로 합류한 팀원
- 클라우드 기반 ML 워크플로우를 이해하려는 데이터 사이언티스트
- 모델 배포 및 운영까지 포함한 **엔드투엔드 ML 파이프라인**이 필요한 엔지니어

### 📌 SageMaker를 사용하는 이유

- **엔드투엔드 ML 지원**: 데이터 준비 → 학습 → 배포 → 운영까지 한 플랫폼에서 제공
- **관리형 인프라**: 인스턴스, GPU 클러스터, 스케일링 등을 직접 관리할 필요 없음
- **확장성 & 유연성**: 소규모 실험부터 대규모 분산 학습까지 확장 가능
- **비용 최적화**: 필요한 만큼만 리소스 사용 (Spot 인스턴스, 온디맨드)
- **통합 생태계**: Studio, Processing, Autopilot, Clarify, Pipelines 등 다양한 서비스와 통합
- **보안 & 거버넌스**: IAM Role, VPC, CloudTrail 등 AWS 보안 및 추적 기능과 연계

👉 요약: SageMaker는 **“ML 프로젝트를 더 쉽고, 빠르고, 안전하게 운영”** 하기 위한 AWS의 통합 플랫폼
목적

## 2. Amazon SageMaker 개요

### 📌 SageMaker란 무엇인가?

- Amazon Web Services(AWS)에서 제공하는 **완전관리형 머신러닝(ML) 서비스**
- 데이터 준비, 모델 학습, 하이퍼파라미터 튜닝, 배포 및 운영까지 **ML 전 과정(End-to-End)** 지원
- Jupyter 기반의 통합 개발 환경(Studio) 및 다양한 API/SDK 제공

👉 즉, SageMaker는 **ML 파이프라인을 빠르고 확장 가능하게 구축**할 수 있도록 돕는 플랫폼

### 📌 주요 특징 및 장점

- **완전관리형 인프라**  
  - GPU/CPU 인스턴스 관리, 클러스터 프로비저닝 자동화  
- **확장성**  
  - 소규모 실험에서 대규모 분산 학습까지 지원  
- **다양한 학습 옵션**  
  - 내장 알고리즘, 커스텀 코드, 프레임워크(PyTorch, TensorFlow 등) 지원  
- **MLOps 기능 내장**  
  - Pipelines, Model Monitor, Clarify로 운영까지 통합  
- **통합 환경 제공**  
  - SageMaker Studio를 통한 협업 및 시각화 지원  
- **보안 및 규제 준수**  
  - IAM, VPC, KMS, CloudTrail 등 AWS 보안 기능과 연계 가능  

### 📌 SageMaker 비용

- **사용한 만큼 과금 (Pay-as-you-go)**  
  - 데이터 처리/학습/배포 시 사용한 리소스(인스턴스, 스토리지, 네트워크)에 따라 과금
- **비용 구성 요소**
  - **Notebook 인스턴스 비용**: Studio, Notebook 실행 시간
  - **학습 비용**: 사용한 인스턴스 타입 × 시간
  - **배포 비용**: 엔드포인트 실행 시간 × 인스턴스 수
  - **추가 서비스 비용**: Data Wrangler, Processing Jobs, Feature Store 등
- **비용 절감 방법**
  - Spot Instance 활용 (최대 90% 저렴)
  - 엔드포인트 자동 종료 또는 Serverless Inference 활용
  - 실험 종료 후 인스턴스 정리 습관화

👉 정리: SageMaker는 “필요할 때만 리소스를 쓰고, 다 쓰면 바로 정리”하는 구조라서 **비용 최적화 전략**이 중요함

## 3. SageMaker Studio 소개

### 📌 Studio 개념 및 특징

Amazon SageMaker Studio는 **올인원(All-in-one) 머신러닝 통합 개발 환경(IDE)**  

- 웹 기반 인터페이스로, 데이터 준비 → 모델 학습 → 배포 → 운영까지 **단일 환경**에서 수행 가능  
- 기존 Jupyter Notebook을 확장한 형태로, 실험 관리 및 협업 기능이 강화됨  

#### 주요 특징

- **통합 관리**: 코드, 데이터셋, 실험 결과, 모델 아티팩트 한 곳에서 관리  
- **협업 지원**: 여러 사용자가 동일 프로젝트에 참여 가능  
- **시각화 도구 제공**: 모델 학습 로그, 성능 지표, 디버깅 결과를 시각적으로 확인  
- **클릭 기반 워크플로우**: 데이터 전처리(Data Wrangler), AutoML(Autopilot) 등 GUI 기반 활용 가능  

### 📌 Studio에서의 워크플로우

1. **데이터 준비**  
   - S3, Redshift, RDS 등 다양한 데이터 소스 연동  
   - Data Wrangler를 통한 시각적 데이터 전처리  

2. **모델 개발**  
   - Jupyter 기반 Notebook에서 코드 작성  
   - 내장 알고리즘, 프레임워크(TensorFlow, PyTorch 등) 지원  

3. **모델 학습**  
   - 단일 인스턴스 또는 분산 학습 클러스터에서 실행  
   - 실험 관리(Experiments) 기능으로 학습별 성능 비교  

4. **모델 배포**  
   - Studio 내에서 클릭 몇 번으로 엔드포인트 생성 가능  
   - 실시간 추론 / 배치 추론 모두 지원  

5. **모델 운영**  
   - Model Monitor로 데이터 드리프트 감지  
   - Clarify로 편향 탐지 및 설명 가능성 확보  

6. **실험 관리 및 협업**  
   - 여러 팀원이 동일 Studio 프로젝트에서 실험 추적 및 비교 가능  
   - Git 통합으로 버전 관리 용이  

👉 요약: Studio는 **“ML 개발의 Jupyter + 협업 + 운영 기능까지 한 데 모은 통합 IDE”**

## 4. SageMaker 활용 사례

### 📌 일반적인 SageMaker 활용 프로젝트 예시

- 데이터 준비 → 모델 학습 → 배포 → 운영까지 **엔드투엔드 ML 파이프라인** 구축 가능  
- 예: 고객 이탈 예측, 이미지 분류, 추천 시스템, 시계열 예측 등  
- 빠른 실험과 확장성을 동시에 제공  

### 📌 모델 학습 및 배포

- 내장 알고리즘(XGBoost, Linear Learner 등)이나 프레임워크(PyTorch, TensorFlow 등)를 활용한 모델 학습  
- 학습 완료 후 **한 줄 코드 또는 클릭 몇 번**으로 엔드포인트 생성 가능  
- 실시간 추론(REST API) 및 대규모 배치 추론 지원  

### 📌 데이터 전처리 파이프라인

- **Processing Jobs** 또는 **Data Wrangler**를 활용하여 데이터 정제, 특징 엔지니어링 수행  
- 대규모 데이터셋도 분산 환경에서 처리 가능  
- 전처리 과정을 자동화하여 재사용성 확보  

### 📌 Studio 기반 활용 프로젝트 예시

- 여러 팀원이 동일한 Studio 환경에서 **협업** 가능  
- **Experiments 기능**으로 각 실험(학습)의 성능, 하이퍼파라미터, 로그 추적  
- 모델 학습 후 디버깅, 성능 비교, 운영 환경 배포까지 한 흐름에서 진행  

### 📌 협업 환경에서의 실험 관리

- 실험별 결과를 체계적으로 관리하여 **재현성 확보**  
- Git과 연동하여 코드 버전 관리 및 협업 강화  
- 데이터 사이언티스트와 ML 엔지니어가 **같은 환경에서 빠르게 피드백 루프**를 돌릴 수 있음  

👉 요약: SageMaker는 **프로젝트 단위 협업 + 재현성 + 확장성**을 동시에 만족시키는 ML 플랫폼

## 5. SageMaker 주요 기능 정리

### 📌 데이터 준비

- **Data Wrangler**: GUI 기반 데이터 탐색 및 전처리 도구  
- **Processing Jobs**: 대규모 데이터 전처리 및 특성 엔지니어링 수행  
- **Feature Store**: 학습/추론 시 일관성 있게 사용할 수 있는 피처 저장소 제공  

### 📌 데이터 전처리 (SageMaker Processing)

- 스케일링, 정규화, 결측치 처리 등 전처리 작업을 분산 환경에서 실행  
- scikit-learn, Spark, PyTorch 등 다양한 프레임워크 지원  
- 반복적인 전처리 파이프라인을 자동화 가능  

### 📌 모델 학습

- **내장 알고리즘**: XGBoost, Linear Learner, Object Detection 등  
- **커스텀 학습**: TensorFlow, PyTorch, MXNet 등 원하는 프레임워크 사용 가능  
- **분산 학습**: Horovod, Parameter Server 등을 활용하여 대규모 학습 처리  

### 📌 모델 최적화

- **하이퍼파라미터 튜닝 (HPO)**  
  - 자동으로 다양한 하이퍼파라미터 조합을 탐색  
  - 최적 성능을 내는 모델 조합을 빠르게 찾아줌  
  - Bayesian Optimization, Random Search 지원  

### 📌 모델 배포

- **실시간 엔드포인트**: API 형태로 모델을 배포하여 실시간 추론 가능  
- **Batch Transform**: 대규모 데이터셋을 한 번에 추론 가능  
- **멀티모델 엔드포인트**: 여러 모델을 하나의 엔드포인트에서 서비스 가능  
- **서버리스 추론**: 트래픽이 적은 경우 비용 효율적인 방식으로 배포  

### 📌 모델 운영

- **Model Monitor**: 데이터 드리프트, 품질 저하 감지  
- **Clarify**: 편향 탐지 및 모델 설명 가능성 제공  
- **Debugger**: 학습 중간 단계에서 지표를 추적하고 문제 디버깅 지원  

### 📌 Pipelines (MLOps)

- 엔드투엔드 **머신러닝 파이프라인** 자동화 도구  
- 데이터 준비 → 학습 → 배포 과정을 워크플로우로 정의  
- CI/CD와 유사하게 ML 모델의 지속적 통합 및 배포(MLOps) 지원  

👉 요약: SageMaker는 **데이터 준비 → 학습 → 최적화 → 배포 → 운영 → 자동화**까지 ML 전 주기를 포괄적으로 지원

## 6. 결론 및 참고 자료

### 📌 결론

- Amazon SageMaker는 **데이터 준비 → 학습 → 최적화 → 배포 → 운영 → 자동화**까지 전 과정을 지원하는 완전관리형 ML 플랫폼  
- Studio 환경을 통해 데이터 사이언티스트, 엔지니어, 분석가가 **협업**하고 **재현 가능한 실험**을 수행할 수 있음  
- 비용 최적화, 확장성, 보안성을 모두 제공하여 **사내 ML 프로젝트를 효율적이고 안정적으로 운영** 가능  

👉 정리: 사내 ML/AI 프로젝트에 SageMaker를 도입하면, **빠른 실험 → 안정적인 운영 → 비용 절감**의 선순환 구조를 만들 수 있음  

### 📌 SageMaker 학습 리소스

- [공식 문서 (AWS)](https://docs.aws.amazon.com/sagemaker/)  
- [SageMaker 예제 노트북 GitHub](https://github.com/aws/amazon-sagemaker-examples)  
- [AWS SageMaker Workshop](https://sagemaker-examples.readthedocs.io/en/latest/)  
- [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/)  

### 📌 추가 참고 자료 및 Best Practice

- 비용 절감을 위한 **Spot Instance + Serverless Inference** 활용 전략  
- 모델 운영 단계에서 **Model Monitor + Clarify** 적용으로 품질 및 공정성 확보  
- MLOps 구축 시 **Pipelines + CI/CD** 연동으로 자동화 수준 향상  
- IAM, VPC, KMS를 활용한 **보안 강화** 방안  

👉 참고 자료를 통해 학습을 이어가고, **실제 사내 프로젝트에서 작은 PoC부터 적용**하는 것이 가장 효과적
