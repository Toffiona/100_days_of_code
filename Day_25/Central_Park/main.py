import pandas

data = pandas.read_csv("./Day_25/Central_Park/2018_Central_Park_Squirrel_Data.csv")
# print(data)

color_dict = {"Fur Color": [], "count": []}
color_list = data["Primary Fur Color"].to_list()
# print(color_list)

for color in color_list:
    count = 0
    if color not in color_dict["Fur Color"]:
        color_dict["Fur Color"].append(color)
        count += 1
        color_dict["count"].append(count)
    else:
        color_index = color_dict["Fur Color"].index(color)
        color_dict["count"][color_index] += 1       


print(color_dict)

data_frame = pandas.DataFrame(color_dict)
data_frame.to_csv("./Day_25/Central_Park/new_data.csv")




