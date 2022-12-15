import pandas as pd

data = pd.read_csv('train.csv')
names = {}
for index, row in data.iterrows():
    name = row['Name'].split('. ')[1].split()[0]
    if name in names:
        names[name] += 1
    else:
        names[name] = 1

names = sorted(names.items(), key=lambda x: x[1], reverse=True)
print("Топ-10 имен:")
for i in range(10):
    print('{0}. {1}'.format(i+1, names[i][0]))
