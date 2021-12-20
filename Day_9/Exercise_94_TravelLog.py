travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_name, visits_num, cities_name):
    new_element = {}
    new_element["country"] = country_name
    new_element["visits"] = visits_num
    new_element["cities"] = cities_name
    
    travel_log.append(new_element)


# travel_log.append(add_new_country["country"])



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Japan", 5, ["tokyo", "hokaido"])
print(add_new_country)
print(travel_log)