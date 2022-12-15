import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import csv

# Создаем словарь для замены данных в DataFrame в дальнейшем
d = {'male': 0, 'female': 1, 'S': 0, 'C': 1, 'Q': 2}

data = pd.read_csv('train.csv')
# Создаем серию с выжившими для машинного обучения
expected_data = data['Survived']
# Заменяем пустые значения возраста средним показателем
data['Age'] = data['Age'].fillna(data['Age'].median())
# Убираем столбцы,которые не понадобятся (субъективно)
data = data.drop(columns=['Name', 'Ticket', 'Fare', 'Cabin', 'PassengerId', 'Survived'])
# Выделим 4 возрастные группы
data.loc[data['Age'] <= 22, 'Age'] = 0
data.loc[(40 >= data['Age']) & (data['Age'] > 18), 'Age'] = 1
data.loc[(60 >= data['Age']) & (data['Age'] > 40), 'Age'] = 2
data.loc[data['Age'] > 60, 'Age'] = 3
# Заменяем пол и порт посадки на число для машинного обучения
data = data.replace(d)
# Заменяем пустые значения портов на средние
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].median())

test = pd.read_csv('test.csv')
# Заменяем пустые значения возраста на средние
test['Age'] = test['Age'].fillna(test['Age'].median())
# Убираем ненужные столбцы
test = test.drop(columns=['Name', 'Ticket', 'Fare', 'Cabin', 'PassengerId'])
# Заменяем пол и порт на число
test = test.replace(d)
# Делим на 4 возрастных группы
test.loc[test['Age'] <= 18, 'Age'] = 0
test.loc[(40 >= test['Age']) & (test['Age'] > 18), 'Age'] = 1
test.loc[(60 >= test['Age']) & (test['Age'] > 40), 'Age'] = 2
test.loc[test['Age'] > 60, 'Age'] = 3

# Применяем машинное обучение
clf = DecisionTreeClassifier()
# Загружаем данные
clf.fit(data, expected_data)
# Получаем результат
final_data = clf.predict(test)

# Создаем список из номеров пассажиров
indexes = []
for i in range(len(final_data)):
    indexes.append(i+892)
# Записываем в файл для проверки на Kaggle
with open('output.csv', 'w') as f:
    fieldnames = ['PassengerId', 'Survived']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(418):
        writer.writerow({'PassengerId': indexes[i], 'Survived': final_data[i]})
