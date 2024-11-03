import pandas as pd

# Создаем словарь
data = {
    'name' : ['Alis', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender' : ['female', 'male', 'male', 'male', 'female'],
    'department' : ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

df = pd.DataFrame(data) # Создаем датафрейм

# Преобразуем столбцы в категориальные данные
df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')
print() # пустая строка

print(df) # печатаем DataFrame
print() # пустая строка

print('Выводим на печать уникальные категории:')
print(df['gender'].cat.categories)
print(df['department'].cat.categories)
print() # пустая строка

# Выводим на печать числовые коды категорий
print(f'числовые коды категорий gender\n {df['gender'].cat.codes}')
print() # пустая строка
print(f'числовые коды категорий department \n {df['department'].cat.codes}')
print() # пустая строка

df['department'] = df['department'].cat.add_categories(['Finance']) # добавляем категорию Finance

print('уникальные категории:')
print(df['department'].cat.categories)
print() # пустая строка

print(df) # печатаем DataFrame
print() # пустая строка

print('уникальные категории:')
print(df['department'].cat.categories)
df['department'] = df['department'].cat.remove_categories(['HR']) # удаляем категорию HR
print() # пустая строка
print(df)