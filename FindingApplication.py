# -*- coding: cp1251 -*-
import requests
good_key = ["Id", "SefUrl", "CategoryCaption", "Caption"]
s = "https://apidata.mos.ru/v1/datasets/"
s += "/?api_key=a47e7dc029852f8972d61616d5cf5d36"
response = requests.post(s) #requests
print(response)
if response.status_code == 200:
    print("Successfull connect")
    r = response.json() #create a dictionary
 #   print(r)
    for one_res in r: 
        for key,value in one_res.items():
            if key in good_key:
                print(key, ":", value)
        print()
#    print(r)
 #   print(response.text)
    print(response.url) # link to website
