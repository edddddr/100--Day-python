# with open('weather-data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open('weather-data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatres = []
#     for row in data:
#         temperatres.append(row[1])
    
#     print(temperatres)


import pandas 

# data = pandas.read_csv('weather-data.csv')
# print(data)
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# data[data.temp.max()]


# print(data[data.temp == data.temp.max()])

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250623.csv")
grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    "Fur Color" : ["Grey", "Red", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")