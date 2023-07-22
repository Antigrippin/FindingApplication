# -*- coding: cp1251 -*-
import requests

def delete_api(req):
    answ = req[:-42]
    return answ

good_key = ["Id", "SefUrl", "CategoryCaption", "Caption"]
bad_key = ["Number", "global_id"]
orig_link = "https://apidata.mos.ru/v1/datasets/"
api_key = "/?api_key=a47e7dc029852f8972d61616d5cf5d36"
print(len(api_key))
req = orig_link+api_key
response = requests.post(req) #requests
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
    print(response.url) # link to website


req = delete_api(req)
print('Req now : ', req)
print('Введите ID для перехода:')
req_id = input()


req += req_id + api_key
response = requests.post(req)
if response.status_code == 200:
    print("Successfull connect")
    print(response.text)
  # r = response.json() #create a dictionary
   # print(r)
 #   for one_res in r: 
 #       for key,value in one_res.items():
  #          if key in good_key:
 #               print(key, ":", value)
 #       print()
    print(response.url) # link to website

print('Таблица: ', end = '\n\n\n\n')
req = delete_api(req)
req += "/rows" + api_key
print('\nreq = ', req, end = '\n\n')
response = requests.post(req)
if response.status_code == 200:
    r = response.json()
    for one_req in r:
        print(one_req)
        break;
    for one_req in r:
        for key,value in one_req.items():
            if (key in bad_key) == False:
                print(value)
else:
    print("Error")