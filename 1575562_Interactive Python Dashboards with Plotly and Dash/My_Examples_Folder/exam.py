# conda activate mydashenv

import pandas as pd

df = pd.read_csv('salaries.csv')
#print(df)
#print(df['Salary'])
#print(df[['Name','Salary']])
#print(df['Salary'].min())
#print(df['Salary'].mean())

#series_of_bool = df['Age'] > 30
#print(series_of_bool)
#print(df[series_of_bool])
#print(df[df['Age'] > 30])

#print(df['Age'].unique())
#print(df['Age'].nunique())

#print(df.columns)
#print(df.info())
#print(df.describe())
print(df.index)