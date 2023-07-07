
"""
 Speed Net Program

 Created by *Abdullah EL-Yamany*

 Youtube Channel => CodeRK
 Video Link => https://youtu.be/op0BsWNsATE
"""

from pystyle import *
import speedtest

print(Box.Lines("[+] Made by Abdullah Al-Yamany [+]"))
Write.Print("[+] This Program For Speed Net \n", Colors.purple_to_red, interval=0.1)
print(Box.DoubleCube("Example [5]"))


st = speedtest.Speedtest()

d_st = st.download()
u_st = st.upload()

d = round(d_st / (10**6), 2)
u = round(u_st / (10**6), 2)

Write.Print("[-] Internet Speed Is : \n", Colors.green, interval=0.1)
print("Downloading: ", d , " Mb/s")
print("Uploading: ", u , " Mb/s")

input('\n\nPass Enter_Key To Exit ...')
