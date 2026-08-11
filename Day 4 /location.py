import phonenumbers
from phonenumbers import geocoder, carrier

number = input("Enter phone number with country code: ")

try:
    phone = phonenumbers.parse(number)

    print("\nPhone Information")
    print("-----------------")
    print("Country/Region :", geocoder.description_for_number(phone, "en"))
    print("Carrier        :", carrier.name_for_number(phone, "en"))
    print("Valid Number   :", phonenumbers.is_valid_number(phone))

except Exception:
    print("Invalid phone number.")

# thia is the next step for you to run your code in git bash 
# NIF0825200+janme@NIF0825200 MINGW64 ~/OneDrive/Desktop/hiii (main)
# $ pip install phonenumbers
# Collecting phonenumbers
#   Downloading phonenumbers-9.0.36-py2.py3-none-any.whl.metadata (10 kB)
# Downloading phonenumbers-9.0.36-py2.py3-none-any.whl (2.6 MB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.6/2.6 MB 2.7 MB/s eta 0:00:00
# Installing collected packages: phonenumbers
# Successfully installed phonenumbers-9.0.36

# [notice] A new release of pip is available: 25.0.1 -> 26.2.1
# [notice] To update, run: python.exe -m pip install --upgrade pip
# NIF0825200+janme@NIF0825200 MINGW64 ~/OneDrive/Desktop/hiii (main)
# $ python location.py
# Enter phone number with country code:
