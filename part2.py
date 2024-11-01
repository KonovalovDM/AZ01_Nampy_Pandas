import pandas as pd

df = pd.read_csv('dz.csv')
print(df.head(15))

# Печать отступа
print()

df['City'] = df['City'].fillna('Unknown')
# df['Salary'] = df['Salary'].fillna(0)

print(df.head(15))

# Печать отступа
print()

# Группировка и вычисление средней зарплаты
group = df.groupby('City')['Salary'].mean()

# Округление средней зарплаты до двух десятичных знаков
group = group.round(2)

# Преобразование в DataFrame и переименование столбца
group_df = group.reset_index()
group_df = group_df.rename(columns={'Salary': 'Средняя з/п'})

print(group_df)