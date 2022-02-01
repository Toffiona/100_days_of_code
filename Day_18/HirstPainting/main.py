import colorgram
# import os
# print(os.getcwd())
# here = os.path.dirname(os.path.abspath(__file__))
# filename = os.path.join(here, 'painting.jpg')

colors = colorgram.extract('./Day_18/HirstPainting/painting.jpg', 25)
#print(colors)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

[(250, 251, 247), (199, 168, 94), (227, 239, 232), (129, 179, 191), (163, 58, 78), (234, 221, 121), (49, 113, 167), (241, 217, 222), (104, 87, 83), (143, 187, 119), (239, 245, 249), (216, 151, 171), (67, 125, 76), (94, 124, 180), (85, 165, 94), (190, 71, 90), (161, 34, 49), (142, 119, 116), (221, 173, 182), (175, 205, 174), (163, 202, 211), (204, 116, 48), (75, 60, 56), (67, 56, 52), (176, 190, 213)]