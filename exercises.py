# with open("weather_data.csv") as weather_data:
#    data = weather_data.readlines()
#    print(data)

# import csv

# with open("weather_data.csv") as weather_data:
#    data = csv.reader(weather_data)
#    temperature = []
#    for row in data:
#        if row[1] != "temp":
#            temperature.append(int(row[1]))
#    print(temperature)

import pandas
import statistics

data = pandas.read_csv("weather_data.csv")
print(data)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
# temp_avg = statistics.mean(temp_list)
temp_avg = data["temp"].mean()
print(round(temp_avg, 2))
temp_max = data["temp"].max()
print(temp_max)
sunday = data[data.temp == data["temp"].max()]
print(sunday)
fahrenheit = sunday.temp * 9/5 + 32
print(fahrenheit)