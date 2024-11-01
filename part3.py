import pandas as pd

data = {
    'Возраст' : [23, 22, 21, 27, 23, 20, 29, 28, 22, 55],
    'Зарплата' : [54000, 58000, 60000, 52000, 55000, 59000, 51000, 49000, 53000, 6100000],
}

df = pd.DataFrame(data)

print(f'Средний возраст - {df["Возраст"].mean()}')
print(f'Медианный возраст - {df["Возраст"].median()}')
print(f'Стандартное отклонение возраста - {df["Возраст"].std().round(4)}')
# Печать отступа
print()
print(f'Средняя зарплата - {df["Зарплата"].mean()}')
print(f'Медианная зарплата - {df["Зарплата"].median()}')
print(f'Стандартное отклонение зарплаты - {df["Зарплата"].std().round(4)}')
# Печать отступа
print()
print(df.describe())