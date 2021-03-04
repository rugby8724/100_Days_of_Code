# data = []
#
# with open('weather_data.csv') as weather:
#     for line in weather:
#         line = line.rstrip()
#         data.append(line)
#
# print(data)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#
# print(temperatures)

import pandas

data = pandas.read_csv('weather_data.csv')
# print(data['temp'])

# avg_temp = data['temp'].mean()
# print(data['temp'].max())
#
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# total_temp = 0
#
# for temp in temp_list:
#     total_temp += temp
#
# avg_temp = total_temp / len(temp_list)
#
# print(avg_temp)

# get data in Row
# print(data[data.day == 'Monday'])

# print(data[data.temp == data.temp.max()])

# mon = data[data.day == 'Monday']
# mon_f = (mon.temp * 9/5) + 32
# print(mon_f)

# create a DataFrame from scratch

data_dict = {
    'students': ['Amy', 'James', 'Tad'],
    'scores': [76,56, 65]
}

new_data = pandas.DataFrame(data_dict)

new_data.to_csv('new_data.csv')