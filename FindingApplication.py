# -*- coding: cp1251 -*-
import requests

def delete_api(req):
    answ = req[:-42]
    return answ

def finding(good_key, bad_key, orig_link,api_key):
    print("Input word for finding")
    word = input()
    req = orig_link+api_key
    response = requests.post(req) #requests
    #print(response)
    if response.status_code == 200:
        print("Successfull connect")
        r = response.json() #create a dictionary
 #   print(r)
        for one_res in r: 
           for key,value in one_res.items():
              if word in str(value) and key in good_key:
                  for keys,value1 in one_res.items():
                      if keys in good_key:
                          print(keys, ":", value1)
 #          print()
        print(response.url) # link to website
    return 0

def alldata(good_key, bad_key, orig_link,api_key):
    print()

good_key = ["Id", "SefUrl", "CategoryCaption", "Caption"]
bad_key = ["Number", "global_id"]
orig_link = "https://apidata.mos.ru/v1/datasets/"
api_key = "/?api_key=a47e7dc029852f8972d61616d5cf5d36" #my API-key
#print(len(api_key))
print('[0] all database', '[1] finding by word', '[2] Exit', sep = '\n')
print('select the desired item')
x = int(input())
if x == 1:
    finding(good_key, bad_key, orig_link,api_key)
elif x == 0:
    alldata(good_key, bad_key, orig_link,api_key)
    print(1)
req = orig_link+api_key
response = requests.post(req) #requests
#print(response)
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

print('Table: ', end = '\n\n\n\n')
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
            if (key in bad_key):
                print()
            else:
                print(value)
else:
    print("Error")