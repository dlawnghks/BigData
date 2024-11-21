import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
# print(titanic.describe())
# print(titanic.head())
# print(len(titanic))
# print(titanic.tail(10))
# print(titanic.info())
# print(titanic['embarked'], titanic['deck'], titanic['class'])

#print(titanic['deck'])
titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
#print(titanic['deck'])
titanic['deck'].fillna('Unknown', inplace=True)
#print(titanic['deck'])
print(titanic.info())