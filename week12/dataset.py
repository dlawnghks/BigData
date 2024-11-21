import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression  # 적용모델 : 선형 회귀 분석 모델
from sklearn.model_selection import train_test_split  # 훈련 / 검증 셋트 분할 함수

# 나이에 따른 생존율 계산

titanic = sns.load_dataset('titanic')  # 데이터 로딩
median_age = titanic['age'].median()  # 나이 중앙값 산출
titanic_fill_row = titanic.fillna({'age' : median_age})  # 결측치 처리

X = titanic_fill_row[['age']]  # 독립 변수 설정
y = titanic_fill_row[['survived']]  # 종속 변수 설정

# 훈련/검증 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 선택
model = LogisticRegression()

# 선형 회귀 모델 훈련
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)  # 검증 셋트를 인수로 예측

# 시각화
plt.figure(figsize=(5, 2))
plt.scatter(X_test, y_test, color='blue', label='Real')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.title('Linear Regression: Real vs Predicted')
plt.xlabel('Age')
plt.ylabel('Survivied')
plt.show()