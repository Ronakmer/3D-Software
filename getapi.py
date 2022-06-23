from re import A
import socket
from getmac import get_mac_address as gma
import requests






hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)   
# print(gma())
# print("Your Computer Name is:" + hostname)   
# print("Your Computer IP Address is:" + IPAddr) 




n=input("Enter Your Name=")
u=input("Enter Your User Name=")
a=input("Enter Your address=")
p=input("Enter Your phone number=")
e=input("Enter Your email=")
pas=input("Enter Your Password=")
print("=================================")
print("Your Name=",n)
print("Your User Name=",u)
print("Your Address=",a)
print("Your Phone Number=",p)
print("Your E-mail=",e)
print("Your Password =",pas)

print("Your ip address=",IPAddr)
mac=gma()
print("Your mac address=",mac)






# url = "http://127.0.0.1:8000/api/all"


# # api_url1 = "project/getapi.py"
# data={
#     "name":a,
#     "address":b,
#     "phonenumber":c,
#     "email":d,
#     "ip":IPAddr,
#     "mac":mac
# }
# re = requests.post(url=url,data=data)
# re.json()



import json 
import requests 

# api_url = "http://127.0.0.1:8000/api/create/"
# todo = {
#         "name": "xyz",
#         "phone_number": "/95378402362",
#         "gmail": "names@gmail.com",
#         "address": "rajkot"
#     }
# headers =  {"Content-Type":"application/json"}
# response = requests.post(api_url, data=json.dumps(todo), headers=headers)
# print(response.json())


# response.status_code


def add_data(): 
    URL="http://127.0.0.1:8000/api/create/" 
    data= {
        "name": n,
        "username":u,
        "phone_number": p,
        "gmail": e,
        "address": a,
        "password":pas,
        
    } 
    # json_data=json.dumps(data) 
    #     r=requests.post(url=URL, data=json_data)
    #     print(r.json()) 
    
    r=requests.post(url=URL, data=data) 
    # data=r.json() 
    print(r.json()) 
    
add_data()



# api_url = "http://127.0.0.1:8000/all"
# response = requests.get(api_url)
# response.json()
# print(response.json())