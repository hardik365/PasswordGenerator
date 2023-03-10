#Hardik Shahu
#Password Generator

import random

#List of pos chars we can use to make our passwords (Feel free to edit this string to match your needs!)
possChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-=+/?:"


#welcome messsage for the user
start = input("Welcome to password generator!\nPress any key to begin! ")

#So they only enter positive number
while(True == True):
    numberOfPass = int(input("Please enter the number of passwords you'd like: "))
    
    if(numberOfPass <= 0 ):
        print("Error, you entered a negative value, please try again with only positives! ")
    else:
        break

#Checks that they enter higher value for the upper bound 
while(True == True):

    #So they only enter positive number
    while(True == True):
        lengthLower = int(input("Please enter the minimum length of each password: "))
        
        if(lengthLower <= 0 ):
            print("Error, you entered an invalid value, please try again with only positives! ")
        else:
            break
    #So they only enter positive number
    while(True == True):
        lengthUpper = int(input("Please enter the maximum length of each password: "))
       
        if(lengthUpper <= 0 ):
            print("Error, you entered an invalid value, please try again with only positives! ")
        else:
            break

    if(lengthUpper < lengthLower):
        print("Error, you entered higher value for lower bound than upperbound ") 
    else:
        break     


print("Your passwords are: ")

for i in range(numberOfPass):
    password = ""
    length = random.randint(lengthLower, lengthUpper)

    for j  in range(length):
        password += random.choice(possChars)
    
    print(password)