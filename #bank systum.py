#bank systum 
import requests



users={1:{"name":"harsh","btcb":0,"usd":180,"username":"a@gmail.com","password":"qwerty"},
       2:{"name":"muskan","btcb":0,"usd":180,"username":"sotuop@gmail.com","password":"sotuop"},
       3:{"name":"ani","btcb":0,"usd":180,"username":"h@gmail.com","password":"anirudh"}}
ids=None 
while ids==None:
    uname=input("enter username:") 
    passd=input("enter password:")
    for i in range(1,4):
        if uname == users[i]["username"] and passd == users[i]["password"]:
                ids = i
                break
print(f"hey{users[ids]['name']}") 

