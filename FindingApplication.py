import requests
x = input()
s = "https://apidata.mos.ru/v1/datasets/658/?api_key=a47e7dc029852f8972d61616d5cf5d36"
#s += x
response = requests.get(s)
print(response)
if response.status_code == 200:
    print(requests.get(s))
    print(response.text)
    print(response.url)
