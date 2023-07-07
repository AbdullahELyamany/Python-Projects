

"""
 A program to suggest a strong password using Python

 Created by *Abdullah EL-Yamany*

 Video Link => https://youtu.be/OlZoEMdM530
"""


import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

characters_number =input("How Many Characters for the Password: ")

while True :
    try :
         characters_number = int(characters_number)         
         if characters_number < 6 :
             print("you need at least 6 caracters")
             characters_number = input("Please Enter the Number again: ")
         else :
             break
    except :
        print("Please Enter numbers only")         
        characters_number =input("How Maany Characters for the Password: ")

random.shuffle(s1)
random.shuffle(s2) 
random.shuffle(s3) 
random.shuffle(s4)

part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))

password = []

for i in range (part1) :
     password.append(s1[i])
     password.append(s2[i])      

for i in range (part2) :
     password.append(s3[i])
     password.append(s4[i])

random.shuffle(password)

print(''.join(password))
