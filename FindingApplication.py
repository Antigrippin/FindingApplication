# -*- coding: cp1251 -*-
import requests
good_key = ["Id", "SefUrl", "CategoryCaption", "Caption"]
x = input()
print(x)
s = "https://apidata.mos.ru/v1/datasets/"
if len(x) != 0:
    s += x
s += "/?api_key=a47e7dc029852f8972d61616d5cf5d36"
response = requests.post(s) #запрос
print(response)
if response.status_code == 200:
    print("Successfull connect")
    r = response.json() #создание словаря
 #   print(r)
    for one_res in r: 
        for key,value in one_res.items():
            if key in good_key:
                print(key, ":", value)
        print()
#    print(r)
 #   print(response.text)
    print(response.url) # вывод ссылки на данные
