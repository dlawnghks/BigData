import matplotlib.pyplot as plt
import pandas as pd
#from sklearn.linear_model import LinearRegression
#from sklearn.neighbors import KNeighborsRegressor
import jhlearn  # Custom library

lifesat = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

# print(lifesat.head(27))

lifesat.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23000, 63000, 3, 10])
plt.show()

#model = LinearRegression()
#model = KNeighborsRegressor(n_neighbors=3)

# Apply Custom LinearRegression Model
#model = tglearn.LinearRegression()
model = jhlearn.KNeighborsRegressor(3)

model.fit(X, y)

X_new = [[32142.0]]  # 대한민국 1인당 GDP 2022년 자료
print(model.predict(X_new))