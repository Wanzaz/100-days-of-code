import pandas

#TASK: From Primary Fur Color take count, color and make out of it DateFrame
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data["Primary Fur Color"].count())
squirrels_list = data["Primary Fur Color"].to_list()
# print(data["Primary Fur Color"].count() == "Grey")


gray = 0
black = 0
red = 0 #Cinnamon
for squirrel in squirrels_list:
    if squirrel == "Gray":
        gray += 1
    if squirrel == "Black":
        black += 1
    if squirrel == "Cinnamon":
        red += 1

# print(f"gray: {gray}, black: {black}, red: {red}")

squirrel_dict = {
    "Fur Color": ["gray", "black", "red"],
    "Count": [gray, black, red]
}

squirrel_data_frame = pandas.DataFrame(squirrel_dict)
squirrel_data_frame.to_csv("squirrel_count.csv")









