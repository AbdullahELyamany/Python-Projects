

"""
 Multiplication Table Program

 Created by *Abdullah EL-Yamany*

 Youtube Channel => CodeRK
 Video Link => https://youtu.be/8_R6yWE1cRE
"""

from pystyle import *

print(Box.Lines("[+] Made by Abdullah Al-Yamany [+]"))
Write.Print("[+] This Program For Multiplication Table \n", Colors.purple_to_red, interval=0.1)
print(Box.DoubleCube("Example [3]"))

while True:
    try:
        num = int(Write.Input("Enter a Number: ", Colors.blue_to_purple, interval=0.03))
        for i in range(1, 13):
            if i in range(1, 10) and num*i in range(1, 10):
                print(f"{num} ×  {i} =  {num * i}")
            elif i in range(1, 10):
                print(f"{num} ×  {i} = {num * i}")
            else:
                print(f"{num} × {i} = {num * i}")
        break
    except ValueError:
        Write.Print("[+] Error!!, Enter Only Number.\n\n", Colors.red, interval=0.1)

'''
1 * 1 = 1
1 * 2 = 2
1 * 12 = 12
'''

input('\nPass Enter_Key To Exit ...')
