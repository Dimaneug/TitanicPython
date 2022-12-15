import pandas as pd

data = pd.read_csv('train.csv')
is_nan = data.isna().any()
print(is_nan[is_nan])
data['Age'] = data['Age'].fillna(data['Age'].median())
is_nan = data.isna().any()
print(is_nan[is_nan])
