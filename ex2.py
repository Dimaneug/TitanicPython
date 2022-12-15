import pandas as pd

data = pd.read_csv("train.csv")
describe_fields = ["Age", "Fare", "Pclass", "SibSp", "Parch"]
# print(data[data["Sex"] == "male"].select_dtypes(include=['float64', 'int64']).describe())
print("Мужчины\n", data[data['Sex'] == 'male'][describe_fields].describe())
print("Женщины\n", data[data['Sex'] == 'female'][describe_fields].describe())
