
"""
 Sign in Users

 Created by *Abdullah EL-Yamany*

 Youtube Channel => CodeRK
 Video Link => https://youtu.be/ef0gYGs98W0
"""

from pystyle import *

print(Box.Lines("[+] Made by Abdullah Al-Yamany [+]"))
Write.Print("[+] This Program For Login Page \n", Colors.purple_to_red, interval=0.1)
Write.Print("[+] Write UserName and Password \n\n", Colors.purple_to_red, interval=0.1)
print(Box.DoubleCube("Example [1]"))

while True:
    username = Write.Input("Enter UserName: ", Colors.blue_to_green, interval=0.1)
    password = Write.Input("Enter Password: ", Colors.blue_to_green, interval=0.1)
    if username == 'ELyamane' and password == '123456':
        Write.Print("[+] Welcome Admin \n", Colors.green, interval=0.1)
        break
    else :
        Write.Print("[-] Error Try Again \n\n", Colors.red, interval=0.1)


input('\nPass Enter_Key To Exit ...')
