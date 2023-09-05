import requests
a = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = a.json()
amount = int(input("Enter your amount(in USD) to buy bitcoin: "))
btcRate = data["bpi"]["USD"]["rate"]
btcRate=btcRate.replace(",","")
btcRate = float(btcRate)
print(f"Rate of 1 Bitcoin is ${btcRate}")
btcSold = amount/btcRate
print(f"You can buy {btcSold} Bitcoin in ${amount} amount") 
print("you are elon musk")


