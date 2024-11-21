import pandas as pd

data = [[14, 72, 100],
        [51, 8, 11],
        [6, 72, 12]]
df = pd.DataFrame(data, index=[1, 2, 3], columns=["a", "b", "c"])

print(df)
print(df.shape, df.dtypes)
print(df['b'].value_counts())
print(df['b'].nunique())
# print(df.describe())

# import pandas as pd
#
# df = pd.DataFrame(``````````````````````````````````````````````````````
#     {
#         "a": [14, 51, 6],
#         "b": [72, 8, 9],
#         "c": [100, 11, 12]
#     }, index=[1, 2, 3]
# )
# print(df)
# df2 = pd.melt(df)\
#     .rename(columns={'variable':'var', 'value':'val'})\
#     .query("val > 50")
# print(df2.tail(2))

# import numpy as np
#
# m = np.array([[1,1,2,2],
#               [3,3,4,4],
#               [5,6,7,8],
#               [9,9,9,0]])
# print(m[::2, 1::2])
# print(m[::2, 1])