
"""
 url shortcut Program

 Created by *Abdullah EL-Yamany*

 Youtube Channel => CodeRK
 Video Link => https://youtu.be/3FdBuVMTNwg
"""

from pystyle import *
import pyshorteners as short

print(Box.Lines("[+] Made by Abdullah Al-Yamany [+]"))
Write.Print("[+] This Program For short url \n", Colors.purple_to_red, interval=0.1)
print(Box.DoubleCube("Example [4]"))

url = Write.Input("[-] Write url For Short: ", Colors.blue_to_green, interval=0.05)
sh = short.Shortener()
Write.Print(sh.tinyurl.short(url), Colors.green, interval=0.15)


input('\n\nPass Enter_Key To Exit ...')
