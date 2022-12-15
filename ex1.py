import pandas as pd

data = pd.read_csv("train.csv")
alive = [[0, 0] for i in range(3)]  # 1 Класс (0 индекс) [Живых мужчин][Живых женщин] и тд
dead = [[0, 0] for i in range(3)]
for index, row in data.iterrows():
    if row["Survived"] == 1:
        alive[row["Pclass"] - 1][0 if row["Sex"] == "male" else 1] += 1
    else:
        dead[row["Pclass"] - 1][0 if row["Sex"] == "male" else 1] += 1
for i in range(3):
    print("Статистика в ", i + 1, " классе:\n", "Мужчины\n\tВыжили: ", alive[i][0], "\n\tПогибли: ", dead[i][0],
          "\nЖенщины\n\tВыжили: ", alive[i][1], "\n\tПогибли: ", dead[i][1])
