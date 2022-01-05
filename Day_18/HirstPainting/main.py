import colorgram
# import os
# print(os.getcwd())
# here = os.path.dirname(os.path.abspath(__file__))
# filename = os.path.join(here, 'painting.jpg')

colours = colorgram.extract('./Day_18/HirstPainting/painting.jpg', 10)
print(colours)

