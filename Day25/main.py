#with open("./weather_data.csv") as file:
#    data = file.read()
#data = data.split()
#print(data)

#import csv

#with open("./weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for raw in data:
#        if raw[1] != "temp":
#            temperatures.append(int(raw[1]))
#print(temperatures)
#import pandas

#data = pandas.read_csv("weather_data.csv")
#print(data["temp"])
#data_dict = data.to_dict()
#print(data_dict)
#temperatures_list = data["temp"].to_list()
#print(temperatures_list)
#summ = 0
#for temp in temperatures_list:
#    summ += temp

#avr_temp = summ/len(temperatures_list)
#print(int(avr_temp))
#print("{:.2f}".format(avr_temp))

#print(data["temp"].mean())
#print(data["temp"].min())
#print(data["temp"].max())

#get ata in raw
#max = data["temp"].max()
#print(data[data.temp == max])

#def f(x):
#    x = x * 1.8 + 32
#    return float(x)


#monday = data[data.day == "Monday"]
#print(monday.condition)
#farenheit = f(monday.temp)
#print(farenheit)


#create a DataFrame from scratch
#data_dict = {
#    "student": ["Irina", "Ioana", "Diana"],
#    "scores": [56, 67, 87],
#            }
#data = pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("NYC_Squirrel_Data.csv")
color_data = data["Primary Fur Color"]
color_list = []
color_data1 = color_data.duplicated()
for n in range(1, len(color_data1)):
    if color_data1[n] == False:
        color_list.append(color_data[n])
count_list = []
for color in color_list:
    count = 0
    for data in color_data:
        if data == color:
            count += 1
    count_list.append(count)
data_dict = {
     'Fur color': color_list,
     'Count': count_list,
    }
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


# Nr2
#Central Park Squirrel Data Analysis
#import pandas

#data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
#red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
#black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
#print(grey_squirrels_count)
#print(red_squirrels_count)
#print(black_squirrels_count)

#data_dict = {
#    "Fur Color": ["Gray", "Cinnamon", "Black"],
#    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
#}

#df = pandas.DataFrame(data_dict)
#df.to_csv("squirrel_count.csv")


