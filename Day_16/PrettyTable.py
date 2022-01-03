# import PrettyTable class from prettytable module
from prettytable import PrettyTable


# Create an object named "table" from prettytable class
table = PrettyTable()
# use add_collumn method to add attributes to the object "table"
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)

# Change the object's attributes by align the letters to left
table.align = "l"
print(table.align)
print(table)

table.align = "r"
print(table)