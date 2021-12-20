print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))

tip = int(input("What percentage of tip you would like to give? 10, 12 or 15?"))
num_of_people = int(input("How many people to split the bill"))

each_person_bill = round(((total_bill + total_bill * tip / 100) / num_of_people),2)
final_amount = "{:.2f}".format(each_person_bill)
print(f"Each person should pay ${final_amount}")