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
    
#return true si el usuario es valido 
def isUser(user):
    return user in userList

#return true si la moneda es valida
def isCoin(coin):
    return coin in coinList

#return true si la opcion en el login es valida 
def optLogin(option):
    return option in optionLogin

#return true si la opcion en el menu principal es valida 
def optMain(option):
    return option in optionMain

#return true si la opcion en el historial principal es valida 
def optHistorical(option):
    return option in optionHistorical

#obtine la posicion de un valor en la lista indicada, recibe dos parametros un valor a encontrar y una lista donde se buscara.
def getPosition(value,list):
    index = list.index(value)
    return index

#imprime guiones
def separator():
    print("------------------------")

#imprime el testo del menu principal    
def options():
    print("1. Send money $")
    print("2. Received money $")
    print("3. View coin information")
    print("4. Deposit money")

    
    

# Menu de login o registro
separator()
print("1. Login")
print("2. Register")
separator()
option = input("Select: ") #almacena la opcion seleccionada
separator()
    
while not optLogin(option): #entra en este bucle si la opcion seleccionada no es valida
    print("Invalid option")
    print("1. Login")
    print("2. Register")
    separator()
    option = input("Select: ") #almacena la opcion seleccionada nuevamente
else: #en caso contrario significa que la opcion es valida y seguimos con las siguientes validaciones
#-------------------------------------------
#                   LOGIN
#-------------------------------------------
    if (option == optionLogin[0]): #si la opcion seleccionada es "1" (optionLogin[0] = "1")
        userLogin = input("User: ") #almacenamos el usuario
        while not isUser(userLogin): #entra en este bucle si el usuario ingresado es invalido
            separator()
            print("Invalid user")
            separator()
            userLogin = input("User: ") #almacenamos el usuario nuevamente
        else: #en caso contrario significa que el usuario es valido y seguimos con las siguientes validaciones
            separator()
            passwordLogin = input("Password: ") #almacenamos la contraseña
            index = getPosition(userLogin,userList) #obtenemos la ubicacion del usuario en la lista de usuarios (userList) para saber cual es su contraseña
            while not passwordLogin == passwordList[index]: #entra en este bucle si la contraseña ingresada es incorrecta
                separator() 
                print("Invalid password")
                passwordLogin = input("Password: ") #almacenamos la contraseña nuevamente
            else: #en caso contrario significa que la contraseña es valida y seguimos con las siguientes validaciones
                separator()
                print("Wellcome",userLogin) #bienvenida al usuario 
                print("Your money: ",moneyList[index],"$") #mostramos el dinero actual del usuario
                separator()
                options() #motramos el menu principal
                separator()
                option = input("Select: ") #almacena la opcion seleccionada
                
                while not optMain(option): #entra en este bucle si la opcion seleccionada no es valida
                    separator()
                    print("Invalid option")
                    option = input("Select: ")  #almacena la opcion seleccionada nuevamente
                    separator()
                else:  #en caso contrario significa que la opcion  es valida y seguimos con las siguientes validaciones
                    
#-------------------------------------------
#                   1. Send money $
#------------------------------------------- 
                    if (option == optionMain[0]): #si la opcion seleccionada es "1" (optionMain[0] = "1")
                        print("OK",optionMain[0])
                    
#-------------------------------------------
#                   2. Received money $
#------------------------------------------- 
                    elif (option == optionMain[1]): #si la opcion seleccionada es "2" (optionMain[1] = "2")
                        print("OK",optionMain[1])
                    
#-------------------------------------------
#                   3. View coin information
#------------------------------------------- 
                    elif (option == optionMain[2]): #si la opcion seleccionada es "3" (optionMain[2] = "3")
                        print("OK",optionMain[2])

#-------------------------------------------
#                   4. Deposit money"
#------------------------------------------- 
                    elif (option == optionMain[3]): #si la opcion seleccionada es "4" (optionMain[3] = "4")
                        print("OK",optionMain[3])
                    
#-------------------------------------------
#                   REGISTER
#-------------------------------------------           
    elif (option == optionLogin[1]): #si la opcion seleccionada es "2" (optionLogin[1] = "2")
        print("User registration")
        separator()
        newUser = input("Enter user: ") #almacena el nuevo usuario
        while isUser(newUser): #entra a este bucle si el usuario ya se encuentra en uso
            print(newUser,"is already in use")
            newUser = input("Enter user: ") #almacena el nuevo usuario nuevamente
            separator()
        else: #en caso contrario significa que el usuario registrado es valido
            newPassword = input("Enter password: ") #almacena la contraseña
            confirmPassword = input("Confirm password: ") #almacena la confirmacion de contraseña
            while newPassword != confirmPassword: #entra este bucle si la contraseña y la confirmacion no coinciden 
                separator()
                print("Passwords do not match")
                newPassword = input("Enter password: ") #almacena la contraseña nuevamente
                confirmPassword = input("Confirm password: ") #almacena la confirmacion de contraseña nuevamente
            else: #en caso contrario significa que las contraseñas coinciden 
                randomMoney = random.randint(1, 1000) #generamos un saldo aleatorio para el usuario
                userList.append(newUser) #guardamaos el nuevo usuario en la lista
                passwordList.append(newPassword) #guardamos la contraseña en la lista
                moneyList.append(randomMoney) #guardamos el saldo aleatorio para el usuario
                os.system('cls') #limpiamos la consola
                separator()
                print("     LOGIN") #cuando el usuario ya se haya creado, solicitamos el login nuevamente.
                separator()
                userLogin = input("User: ") #almacena el usuario
                while not isUser(userLogin): #entra en este bucle si el usuario es invalido
                    separator()
                    print("Invalid user")
                    separator()
                    userLogin = input("User: ") #almacena el usuario nuevamente
                else: #en caso contrario significa que el usuario es valido y seguimos con las siguientes validaciones
                    separator()
                    passwordLogin = input("Password: ") #almacena la contraseña
                    index = getPosition(userLogin,userList) #obtenemos la ubicacion del usuario en la lista de usuarios (userList) para saber cual es su contraseña
                    while not passwordLogin == passwordList[index]: #entra en este bucle si la contraseña ingresada es incorrecta
                        separator()
                        print("Invalid password")
                        passwordLogin = input("Password: ") #almacenamos la contraseña nuevamente
                    else: #en caso contrario significa que la contraseña es valida y seguimos con las siguientes validaciones
                        separator()
                        passwordLogin = input("Password: ") #almacenamos la contraseña nuevamente
                        print("Wellcome",userLogin) #bienvenida al usuario
                        print("Your money: ",moneyList[index],"$") #mostramos el dinero actual del usuario
                        separator()
                        options() #motramos el menu principal
                        separator()
                        option = input("Select: ") #almacena la opcion seleccionada
                        while not optMain(option):  #entra en este bucle si la opcion seleccionada no es valida
                            print("Invalid option")
                            separator()
                            options()
                            separator()
                            option = input("Select: ") #almacena la opcion seleccionada nuevamente
                        else: #en caso contrario significa que la opcion  es valida y seguimos con las siguientes validaciones
                            print("OK") 

                
                                
            
            
        

    
    