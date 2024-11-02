import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Имя ученика' : ['Мария', 'Иван', 'Алексий', 'Артемий', 'Николай', 'Анна', 'Марина', 'Антоний', 'Екатерина', 'Александр'],
    'Математика' : [5, 5, 4, 4, 5, 3, 5, 4, 5, 4],
    'Русский язык' : [5, 4, 5, 4, 4, 5, 3, 5, 4, 4],
    'Физика' : [5, 4, 5, 4, 5, 3, 5, 4, 4, 5],
    'Информатика' : [5, 5, 5, 5, 5, 4, 5, 5, 5, 5],
    'НВП' : [4, 5, 5, 5, 5, 4, 4, 5, 4, 5],
}

df = pd.DataFrame(data)

print(df.head(15))
print() # Печать отступа

subjects = ['Математика', 'Русский язык', 'Физика', 'Информатика', 'НВП']

for subject in subjects:
    mean_score = df[subject].mean()
    median_score = df[subject].median()
    std_score = df[subject].std().round(4)
    print(f'Средняя оценка по {subject} - {mean_score}')
    print(f'Медианная оценка по {subject} - {median_score}')
    print(f'Стандартное отклонение по {subject} - {std_score}')
    print() # Печать отступа

print() # Печать отступа
print(df.describe())

Q1 = df['Математика'].quantile(0.25)
Q3 = df['Математика'].quantile(0.75)
IQR = Q3 - Q1

downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

df_new = df[(df['Математика'] >= downside) & (df['Математика'] <= upside)]

df_new.boxplot(column='Математика')
plt.show()