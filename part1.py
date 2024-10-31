import pandas as pd

df = pd.read_csv('gym_members_exercise_tracking.csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

