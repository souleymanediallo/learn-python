# with open("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         temperature.append(row[1])
#
# print(temperature[1:])

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print("========")
# print(type(data["temp"]))
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)
print(data[data.day == "Monday"])
print(data[data.temp == 14])

