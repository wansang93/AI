# TensorFlow Basic

2020.08.19 ~ 2020.08.24

https://opentutorials.org/module/4966

https://www.youtube.com/watch?v=auCw6qikSYs&list=PLl1irxoYh2wyLwJutUZx5Q_QEEDZoXBnz

## 1. Orientation

- 기계학습(Muchine learning)
  - 지도학습(Supervised learning)
    - 분류(classification)
    - 회귀(regression)
  - 비지도학습(Unsupervised learning)
    - 군집화(clustering)
    - 변환(transform)
    - 연관(association)
  - 강화학습

- 알고리즘들
  - Decision Tree
  - Random Forest
  - KNN
  - SVM
  - Neural Network

- 다양한 라이브러리들
  - TensorFlow
  - PyTorch
  - Caffe2
  - theano

## 2. Goals and Strategies

- 딥러닝 입문
  1. 파이썬 입문
  2. 데이터 입문
  3. 머신러닝 이해
  4. 딥러닝 원리
  5. 딥러닝 구현

## 3. Big picture of Supervised learning

1. 과거의 데이터를 준비합니다.  
종속변수(y) = w * 독립변수(x)
2. 모델의 구조를 만든다.
3. 데이터로 모델을 학습(Fit)한다.
4. 모델을 이용한다.

## 4. Google Colaboratory

## 5. Pandas: Table handling Tools

## 6. Practice - Pandas: Table handling Tools

[판다스 예제](https://colab.research.google.com/github/blackdew/tensorflow1/blob/master/practice1-pandas.ipynb)

## 7. Lemonade data

## 8. Loss function meaning

학습이 얼마나 진행되었는지 알려주는 부분

Loss 값이 크다 -> 예측값과 결괏값의 차이가 크다.

$$
Loss = (\sum_{i = 1}^{n}{(결괏값 - 예측값)^{2}}) / 데이터 갯수
$$

## 9. Practice Lemonade data

1개의 x와 1개의 y로 구성된 간단한 관계를 머신러닝을 통해 예측해보자

[레모네이드 실습](./pandas_practice.ipynb)

## 10. Predict Boston housing price

14개의 종속변수 x와 집 값 y의 관계를 머신러닝을 통해 구해보자

## 11. Formula and Perceptron

$$ y = (\sum_{i = 1}^{n}{x_{i} + w_{i}}) + b $$

학습한다는 것은 weight 와 bias 를 찾는 과정

## 12. Practice Boston data

[보스턴 집값 실습](./practice_boston.ipynb)

## 13. Truth reality of Learning

1. weight 와 bias 에 랜덤한 값을 준다.
2. Loss 값을 구한다.
3. weight 를 약간 조정한다.
4. Loss의 차이를 미분한 값을 구한다.
5. 이 값을 기준으로 다음 weight 값을 조정한다.
6. 2번부터 다시 반복한다. 

## 14. Classify Iris

회귀(regression)과 분류(classification)의 차이를 다음 강의에서 잘펴보자

## 15. Onehot-encoding

결괏값이 숫자가 아닌 범주형 카테고리를 0 또는 1로 바꾸는 과정

``` python
pd.get_dummies('해당 범주형')  # 자동으로 범주형을 onehot-encoding을 해줌
```

## 16. Softmax

분류 예측 -> 0 ~ 100% 확률로 표현

Sigmoid, Softmax 등으로 변환

x -> y 로 가는 과정중에 activation function 이 존재함

## 17. Practice Iris data

[아이리스 실습](./practice_iris.ipynb)

## 18. Hidden layer

Deep Learning 이란 Persecptron을 여러개 이어 붙여 학습하는 것

정답율이 올라감

입력 부분: input layer
히든 부분: hidden layer
출력 부분: output layer

## 19. Practice Hidden layer

[히든 레이어 실습](./practice_hidden_layser.ipynb)

## 20. appendix 1 - Tip for data

데이터 타입 바꾸기 연습

[appendix 1](./appendix_01.ipynb)

## 21. appendix 2 - Tip for Model

batchNormalization 을 넣어서 학습 효과 극대화 하기

[appendix 2](./appendix_02.ipynb)

## 22. Finish