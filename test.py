import pandas as pd

df=pd.read_csv('doctor clean data.csv')
City=sorted(df.City.unique())
Speciality=sorted(df.Speciality.unique())
Degree_1=sorted(df.Degree_1.unique())

print(Speciality)
print(Degree_1)