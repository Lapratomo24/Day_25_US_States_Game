import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data)

grey_count = data[data["Primary Fur Color"] == "Gray"]
print(len(grey_count))
cinnamon_count = data[data["Primary Fur Color"] == "Cinnamon"]
print(len(cinnamon_count))
black_count = data[data["Primary Fur Color"] == "Black"]
print(len(black_count))

data_dict = {
    "squirrels": ["Gray", "Cinnamon", "Black"],
    "count": [2473, 392, 103]
}

conversion = pandas.DataFrame(data_dict)
conversion.to_csv("squirrel_count.csv")
