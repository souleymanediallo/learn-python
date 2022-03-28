# while ("weather_data.csv") as with open("", "") as f:

# with open("weather_data.csv") as f:
#     data = f.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     print(data)
#     for d in data:
#         print(d[1])

import pandas as pd

data = pd.read_csv("weather_data.csv")

# data_dic = data.to_dict()
# print(data_dic)

# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)
# mean_data = data["temp"].max()
# print(mean_data)
# temp_max = data.temp.max()
# print(data[data.temp == temp_max])
# print(data[data.day == "Monday"])

monday = data[data.day == "Monday"]
monday_morning = monday.temp

monday_temp = int(monday_morning)
monday_temp_F = monday_temp * 9 / 5 + 32
print(monday_temp_F)