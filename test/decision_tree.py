
"""
Python에서 결정 트리(Decision Tree)를 사용한 머신러닝 예제를 보여드리겠습니다.
예제로는 `scikit-learn` 라이브러리를 사용하여 붓꽃(Iris) 데이터셋을 분류하는 모델을 만들겠습니다.
붓꽃 데이터셋은 다양한 종류의 붓꽃 품종을 구분하기 위한 데이터셋입니다.

### 1. 라이브러리 설치
먼저 필요한 라이브러리를 설치합니다.
`scikit-learn`은 머신러닝 알고리즘을 제공하는 라이브러리입니다.

```bash
pip install scikit-learn matplotlib pandas
```

### 2. 코드 예제
다음은 결정 트리를 사용하여 붓꽃 데이터셋을 분류하는 Python 코드입니다.

### 코드 설명
1. **데이터 로드**: `load_iris()` 함수를 사용하여 붓꽃 데이터셋을 로드합니다.
2. **데이터 분할**: `train_test_split()` 함수를 사용하여 데이터셋을 훈련용 데이터와 테스트용 데이터로 나눕니다.
3. **모델 생성 및 훈련**: `DecisionTreeClassifier` 객체를 생성하고 훈련 데이터로 모델을 학습시킵니다.
4. **예측 수행**: 테스트 데이터에 대해 예측을 수행합니다.
5. **성능 평가**: `accuracy_score()`, `classification_report()`, `confusion_matrix()` 함수를 사용하여 모델의 성능을 평가합니다.
6. **결정 트리 시각화**: `plot_tree()` 함수를 사용하여 결정 트리 구조를 시각화합니다.

이 코드를 실행하면 붓꽃 데이터셋을 기반으로 한 결정 트리 모델이 어떻게 작동하는지, 그리고 모델의 성능이 어떻게 되는지 알 수 있습니다.
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
from sklearn import tree

# 1. 데이터 로드
iris = load_iris()
X = iris.data  # 특성(Feature) 데이터
y = iris.target  # 타겟(라벨) 데이터

# 2. 데이터 분할 (훈련용 데이터와 테스트용 데이터로 나누기)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. 결정 트리 모델 생성
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)  # 모델 훈련

# 4. 예측 수행
y_pred = clf.predict(X_test)

# 5. 성능 평가
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_report(y_test, y_pred))
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

# 6. 결정 트리 시각화
plt.figure(figsize=(12,8))
tree.plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.show()
