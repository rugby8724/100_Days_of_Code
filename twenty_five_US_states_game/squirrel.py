import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# for col in data.columns:
#     print(col)


squirrel_color = data['Primary Fur Color'].value_counts()
print(squirrel_color)
