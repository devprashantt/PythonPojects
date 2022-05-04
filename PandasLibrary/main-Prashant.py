# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))

# method 1
# avg = 0
# for data in temp_list:
#     avg = avg + data/7
# print(avg)


# method 2
# average = sum(temp_list)/len(temp_list)
# print(average)


# method 3
# print(data["temp"].mean())

# print(data["temp"].max())
#
# print(data["condition"])

# print(data.condition)

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = int(monday)

# create data frame

data_dict = {
    "students":["prashant", "jaya", "shakshi" ],
    "scores":[76, 76, 76]
}
data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv")
