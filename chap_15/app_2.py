import pandas as pd

data = pd.read_csv("squirrel_data.csv")
gray_data = data[data["Primary Fur Color"] == "Gray"]
print(gray_data)

# print(data["X"].head())
# dic_data = data.to_dict()
# for i in dic_data:
#     print(i == ["Gray"])

# data_series = dic_data["Primary Fur Color"]
# black_color = dic_data[dic_data["Primary Fur Color"] == "Gray"]
# print(dic_data)
# print(data[data.temp == temp_max])
