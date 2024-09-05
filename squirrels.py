import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data)

grey_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_count)
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(cinnamon_count)
black_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_count)

data_dict = {
    "Squirrels": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, cinnamon_count, black_count]
}

conversion = pandas.DataFrame(data_dict)
conversion.to_csv("squirrel_count.csv")
