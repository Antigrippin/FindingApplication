# -*- coding: cp1251 -*-
import requests
import pandas as pd
import openpyxl

#Location of the responce: your program folder
#responce for example 1 : 'answer1.xlsx'
#responce for example 2: 'answer2.xlsx'

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
    req = delete_api(req)
    return req

def alldata(good_key, bad_key, orig_link,api_key):
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
    print()
    req = delete_api(req)
    return req

good_key = ["Id", "SefUrl", "CategoryCaption", "Caption"]
bad_key = ["Number", "global_id"]
orig_link = "https://apidata.mos.ru/v1/datasets/"
api_key = "/?api_key=a47e7dc029852f8972d61616d5cf5d36" #my API-key
print('[0] all database', '[1] finding by word', '[2] find by ID', '[3] Exit', sep = '\n') #choosing 
print('select the desired item')
x = int(input())
if x == 1:
    req = finding(good_key, bad_key, orig_link,api_key)
elif x == 0:
    req = alldata(good_key, bad_key, orig_link,api_key)
elif x == 2:
    req = orig_link
elif x == 3:
    exit()

print('Введите ID для перехода:')
req_id = input()


req += req_id + "/rows" + api_key
response = requests.post(req)
if response.status_code == 200:
    print('Succesfull conect')
    r = response.json()
    df = pd.DataFrame.from_dict(data=r)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_column', None)
    pd.set_option('display.max_colwidth', None)

    print ('\n\n\n')
    df.pop('global_id')
    df.pop('Number') 
    df1 = df.to_dict()
    for key, values in df1.items():
        df2 = values
    #df1.pop('Cells', None)
    df3 = []
    for key,values in df2.items():
        df3.append(values)
    #print(df3)
    answ = pd.DataFrame(df3)
    answ.to_excel('./answer2.xlsx')

else:
    print(response)
    print("Error, Information is too big")