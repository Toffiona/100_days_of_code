# with open ("./Day_25/venv/weather_data.csv") as data:
#     weather_data = data.readlines()
    
# import csv


# with open ("./Day_25/venv/weather_data.csv") as data_file:
#     data = csv.reader(data_file)

#     temperature = []
#     for row in data:
#         temperature.append(row[1])
        
#     temp = temperature[1:]
#     temperature.clear()
#     for x in temp:
#         new_x = int(x)
#         temperature.append(new_x)
#     print(temperature)


import pandas

data = pandas.read_csv("./Day_25/venv/weather_data.csv")
#print(type(data))
#print(data)
# temp = (data["temp"])
# print(type(temp))
#print(data.to_dict())

# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

# # Use method in Pandas 
# print(data["temp"].mean())
# print(data["temp"].max())

# # OTHER WAY TO SELECT SERIES

# print(data.condition)

# GEt Data in row
#print(data[data.day == "Monday"])

#PRINT OUT THE ROW WITH THE MAX TEMP
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])
# print(data.temp)

#GET MONDAY TEMP & CONVERT INTO FARE
# monday = data[data.day == "Monday"]
# monday_temp_f = int(monday.temp) *1.8 + 32
# print(monday_temp_f)

#CREATE DATA FRAME & CONVERT to csv file
data_dict = {"students": ["Amy", "James", "Angela"], "Scores": [76, 80, 56]}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("./Day-25/venv/new_data.csv")