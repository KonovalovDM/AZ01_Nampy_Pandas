import pandas as pd

df = pd.read_csv('gym_members_exercise_tracking.csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df[['Age', 'Weight (kg)', 'Height (m)']])
print(df.loc[57])
print(df.loc[75, 'Weight (kg)'])
print(df[df['Weight (kg)'] < 50])