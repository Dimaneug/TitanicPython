import pandas as pd

data = pd.read_csv("train.csv")
stat = {'S': [0, 0], 'C': [0, 0], 'Q': [0, 0]}  # 0 индекс - погибшие, 1 - выжившие
for index, row in data.iterrows():
    try:
        stat[row['Embarked']][row['Survived']] += 1
    except KeyError:
        pass
for key, item in stat.items():
    print('Из порта ', key, ':\n\tВыжили: ', item[1], '\n\tПогибли: ', item[0],
          '\n\tПроцент выживших: %.2f%%' % (item[1] / sum(item) * 100))
