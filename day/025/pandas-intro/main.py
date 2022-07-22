"""
data = []
with open("weather_data.csv") as file_weather_data:
    weather_data = file_weather_data.readlines()
print(weather_data)

# removing \n
for day in weather_data:
    stripped_day = day.strip()
    data.append(stripped_day)
print(data) 
"""

"""
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        for item in row:
            if item.isdigit():
                temperatures.append(int(item))
print(temperatures)
"""


import pandas

data = pandas.read_csv("weather_data.csv")
#print(data["temp"])

data_dict = data.to_dict()
#print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)


#AVERAGE value of temperatures in the table
# 1. sulution - pretty average
"""
# going through a list and adding value to the sum_of_temp
sum_of_temp = 0
for temp in temp_list:
    sum_of_temp += temp
"""

# 2. sulution - better
average_temp = sum(temp_list) / len(temp_list)
print(f"The average value of temperatures: {average_temp}")

# 3. sulution - the simplest
#print(data["temp"].mean())
print(f"The average value of temperatures: {data['temp'].mean()}")


#MAX value in the tamperatures
#print(data["temp"].max())
print(f"The average value of temperatures: {data['temp'].max()}")


#Get Data in Colums
# both methods work
#print(data["condition"])
#print(data.condition)


#Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)


#Get Mondays temperature and convert it to Farenheit
monday_farenheit_temp = int(monday.temp) * 1.8 + 32
print(monday_farenheit_temp)


#Create a dataframe from scratch and creating a new file with it
data_dict = {
    "student": ["Amy", "James", "Andrew"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
