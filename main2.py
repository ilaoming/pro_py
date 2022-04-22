import random
import requests
import re
from datetime import datetime
import os, sys


#Key API access
COINMARKET_API_KEY = "89f98e0b-a119-494b-8334-a4a8602d7c24"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}

#get data from CoinMarketCap
data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()

#menu INICIO
optionLogin=["1","2"]

#menu HISTORIAL
optionHistorical=["1","2"]

#menu PRINCIPAL
optionMain=["1","2","3","4","5","6"]

regularExp = re.compile(r'^[0-9]+([,][0-9]+)?$')

userList = ["laoming","baki01"]
passwordList = ["5702471","123456"]
moneyList = [125,250]
coinList = []
coin = ""
newUser = ""
newPassword = ""
userLogin = ""
passwordLogin = ""
sendMoney = ""
receivedMoney = ""
option = ""
historical = []

#Recorre la data que trae del api de CoinMarketCap y almacena "Symbol" = (BTC,ETH,DOGE entre otros) en coinList
for symbol in data["data"]:
    coinList.append(symbol["symbol"])
    
#return true where user is valid    
def isUser(user):
    return user in userList

#return true where coin is valid    
def isCoin(coin):
    return coin in coinList

def optLogin(option):
    return option in optionLogin

def optMain(option):
    return option in optionMain
    
def optHistorical(option):
    return option in optionHistorical

def getPosition(value,list):
    index = list.index(value)
    return index

def separator():
    print("------------------------")
    
def options():
    print("1. Send money $")
    print("2. Received money $")
    print("3. View coin information")
    print("4. Deposit money")

    
    


separator()
print("1. Login")
print("2. Register")
separator()
option = input("Select: ")
separator()
    
while not optLogin(option):
    print("Invalid option")
    print("1. Login")
    print("2. Register")
    separator()
    option = input("Select: ")
else:
#-------------------------------------------
#                   LOGIN
#-------------------------------------------
    if (option == optionLogin[0]):
        userLogin = input("User: ")
        while not isUser(userLogin):
            separator()
            print("Invalid user")
            separator()
            userLogin = input("User: ")
        else:
            separator()
            passwordLogin = input("Password: ")
            index = getPosition(userLogin,userList)
            while not passwordLogin == passwordList[index]:
                separator()
                print("Invalid password")
                passwordLogin = input("Password: ")
            else:
                separator()
                print("Wellcome",userLogin)
                print("Your money: ",moneyList[index],"$")
                separator()
                options()
                separator()
                option = input("Select: ")
                
                while not optionMain(option):
                    separator()
                    print("Invalid option")
                    option = input("Select: ")
                    separator()
                else:
                    if (option == optionMain[0]):
                        print("OK")
                    
                while not optMain(option):
                    print("Invalid option")
                    separator()
                    options()
                    separator()
                    option = input("Select: ")
                else:
                    print("OK")
                    
#-------------------------------------------
#                   REGISTER
#-------------------------------------------           
    elif (option == optionLogin[1]):
        print("User registration")
        separator()
        newUser = input("Enter user: ")
        while isUser(newUser):
            print(newUser,"is already in use")
            newUser = input("Enter user: ")
            separator()
        else:
            newPassword = input("Enter password: ")
            confirmPassword = input("Confirm password: ")
            while newPassword != confirmPassword:
                separator()
                print("Passwords do not match")
                newPassword = input("Enter password: ")
                confirmPassword = input("Confirm password: ")
            else:
                randomMoney = random.randint(1, 1000)
                userList.append(newUser)
                passwordList.append(newPassword)
                moneyList.append(randomMoney)
                os.system('cls')
                separator()
                print("     LOGIN")
                separator()
                userLogin = input("User: ")
                while not isUser(userLogin):
                    separator()
                    print("Invalid user")
                    separator()
                    userLogin = input("User: ")
                else:
                    separator()
                    passwordLogin = input("Password: ")
                    index = getPosition(userLogin,userList)
                    while not passwordLogin == passwordList[index]:
                        separator()
                        print("Invalid password")
                        passwordLogin = input("Password: ")
                    else:
                        separator()
                        print("Wellcome",userLogin)
                        print("Your money: ",moneyList[index],"$")
                        separator()
                        options()
                        separator()
                        option = input("Select: ")
                        while not optMain(option):
                            print("Invalid option")
                            separator()
                            options()
                            separator()
                            option = input("Select: ")
                        else:
                            print("OK")

                
                                
            
            
        

    
    