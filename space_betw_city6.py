
"""
 Space Between City Program

 Created by *Abdullah EL-Yamany*

 Youtube Channel => CodeRK
 Video Link => https://youtu.be/lkpB_aRks0U
"""

from pystyle import *
from geopy.distance import geodesic

print(Box.Lines("[+] Made by Abdullah Al-Yamany [+]"))
Write.Print("[+] This Program For Space Between City \n", Colors.purple_to_red, interval=0.1)
print(Box.DoubleCube("Example [6]"))

Write.Print("[+] Space Between Cities Is: ", Colors.purple_to_red, interval=0.1)
first_place = (24.08889, 32.89972)  # Enter the coordinates of the second city
second_place = (29.06528, 31.09944) # Enter the coordinates of the first city

dis = int(geodesic(first_place, second_place).km)
print(dis, "km")

input('\n\nPass Enter_Key To Exit ...')
