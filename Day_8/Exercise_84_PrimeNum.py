#Write your code below this line 👇
'''
def prime_checker(number):
    if number == 1:
        print(f"{number} is not prime number")
    if number == 2:
        print(f"{number} is the prime number")
    elif number > 2:
        for x in range(2, number):
            if number % x == 0:
                print(f"{number} is not the prime number")
                break            
            
            if x == number - 1: 
                print(f"{number} is the prime number")

'''

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    
    if is_prime == False:
        print("It is not a prime number")

    if is_prime == True:
        print("It is the prime number")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number = n)