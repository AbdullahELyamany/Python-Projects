
"""
 Locate the phone number

 Created by *Abdullah EL-Yamany*

 Channal => Korsat X Parmaga 
 Link Video => https://youtu.be/K0Sb-4H0Fzg
#=======================
"""

import phonenumbers
from phonenumbers import geocoder, carrier, timezone
print("Please Enter +Code_Country and Phone_Number")
phone = input('Enter Your Phone Number: ')

try:
    phone_num = phonenumbers.parse(phone, None)  # "EG"
    print(phone_num)
    
    location = geocoder.description_for_number(phone_num, "en")
    print(f"Phone Location: \"{location}\"")
    
    company_name = carrier.name_for_number(phone_num, "en")
    print(f"Company Name: \"{company_name}\"")
    
    phone_time_zone = timezone.time_zones_for_number(phone_num)
    print(f"Time Zone Of Phone: \"{phone_time_zone}\"")

except:
    print("An error occurred")






