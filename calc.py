
"""
 Calculate Program

 Created by *Abdullah EL-Yamany*

 Youtube Channel => CodeRK
 Video Link => https://youtu.be/cFdGmt6PPYo
"""

from pystyle import *

print(Box.Lines("[+] Made by Abdullah Al-Yamani [+]"))
Write.Print("[+] This Program For Calculator \n", Colors.purple_to_red, interval=0.1)
print(Box.DoubleCube("Example [2]"))

while True:
    n1 = int(Write.Input("[+] Enter First Number: ", Colors.blue_to_green, interval=0.02))
    op = Write.Input("Enter Operator [+] [-] [*] [/] [%] [//]: ", Colors.orange, interval=0.02)
    n2 = int(Write.Input("[+] Enter Second Number: ", Colors.blue_to_green, interval=0.02))

    if op == '+':
        Write.Print(f"{n1} + {n2} = {n1 + n2}\n\n", Colors.green, interval=0.1)
        break
    elif op == '-':
        Write.Print(f"{n1} - {n2} = {n1 - n2}\n\n", Colors.green, interval=0.1)
        break
    elif op == '*':
        Write.Print(f"{n1} * {n2} = {n1 * n2}\n\n", Colors.green, interval=0.1)
        break
    elif op == '/':
        Write.Print(f"{n1} / {n2} = {n1 / n2}\n\n", Colors.green, interval=0.1)
        break
    elif op == '%':
        Write.Print(f"{n1} % {n2} = {n1 % n2}\n\n", Colors.green, interval=0.1)
        break
    elif op == '//':
        Write.Print(f"{n1} // {n2} = {n1 // n2}\n\n", Colors.green, interval=0.1)
        break
    else:
        Write.Print("\nPlease Write Just: +  -  *  /  %  //\n\n", Colors.red, interval=0.05)

input('\nPass Enter_Key To Exit ...')
