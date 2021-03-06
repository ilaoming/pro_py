import requests
import re
from datetime import datetime

#Declaracion de variables
monedas_list=[]

#lista usuarios disponibles
usuarios_list=["jose21","1211","rojas21","baki01","jor41","744744","jesus2215"]

#montos disponibles para los usuarios
montos_list=["500","125","300","236","450","21","19"]

#menu INICIO
menu_opcion_list=["1"]

#menu HISTORIAL
menu_historial=["1","2"]

#menu PRINCIPAL
menu_opcion_list2=["1","2","3","4","5","6"]

#opciones disponibles para el menu principal
nom_opciones=["Recibir cantidad","Transferir monto","Mostrar Balance de una moneda","Mostrar balance general","Mostrar historico de transacciones"]


exp_regular = re.compile(r'^[0-9]+([,][0-9]+)?$')

moneda = ""
usuario_login = ""
opcion = ""
opcion2 = "" 
cantidad = ""
historial = []




#Key API
COINMARKET_API_KEY = "89f98e0b-a119-494b-8334-a4a8602d7c24"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}
#Obtiene la data de CoinMarketCap
data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()


#Recorre la data que trae del api de CoinMarketCap y almacena "Symbol" = (BTC,ETH,DOGE entre otros) en monedas_list
for cripto in data["data"]:
    monedas_list.append(cripto["symbol"])
    
# Retorna true si encuentra un usuario valido en usuarios_list
def esusuario(usuario):
    return usuario in usuarios_list

# Retorna true si encuentra un symbol valido en monedas_list
def esmoneda(cripto):
    return cripto in monedas_list

# Retorna true si encuentra una opcion valida en el menu
def opcion_valida(opcion):
    return opcion in menu_opcion_list

# Retorna true si encuentra una opcion valida en el menu
def opcion_valida2(opcion):
    return opcion in menu_opcion_list2

# Retorna true si encuentra una opcion valida en el menu
def opcion_valida3(opcion):
    return opcion in menu_historial

# Retorna los datos almacenados en nom_opciones[] o en otras palabras imprime los valores de nom_opciones[]
def menu_opciones_text():
    for x in range(len(nom_opciones)):
        print(x+1,".",nom_opciones[x])

#Retorna el valor actual de la moneda indicada en el parametro
def datos(nom_moneda):
    for element in data["data"]:
        if (element["symbol"] == nom_moneda):
            print("Symbol: ",element["symbol"])
            print("Nombre: ",element["name"])
            print("Precio en Dolares: ",element["quote"]["USD"]["price"]," USD")

#Imprime todas las monedas disponibles en CoinMarket, en USD            
def data_monedas():
    for element in data["data"]:
            print("Symbol: ",element["symbol"])
            print("Nombre: ",element["name"])
            print("Precio en Dolares: ",element["quote"]["USD"]["price"]," USD")
            print("------------------------------------------------------------------") 
            


#----------------------------------------------------------------------------------------------------------------------------------
#                                                       MENU INGRESO
#----------------------------------------------------------------------------------------------------------------------------------

#Menu de opciones N.1 (INGRESO)
print("Seleccione :\n1.Iniciar Sessi??n\n--------------------------")
opcion = input("Seleccione una opcion: ")
print("--------------------------")

#Valida si la opcion existe                    
while not opcion_valida(opcion):
    print("Opcion NO valida")
    print("Seleccione :\n1.Iniciar Sessi??n\n--------------------------")
    opcion = input("Seleccione una opcion: ")
    print("--------------------------")
else:
    if (opcion == menu_opcion_list[0]):
#Valida si el usuario existe                    
        usuario_login = input("Ingrese su usuario para el ingreso: ")
        while not esusuario(usuario_login):
            print("--------------------------")
            print("Usuario invalido")
            usuario_login = input("Ingrese su usuario para el ingreso: ")
        else:
            print("Bienvenido -", usuario_login)
            posicion = usuarios_list.index(usuario_login)
            print("Su saldo es:",montos_list[posicion])
            
#Menu de opcines N. 2 (INTERACCION CON EL USUARIO)
            print("--------------------------")
            menu_opciones_text()
            print("--------------------------")
            opcion2 = input("Seleccione una opcion: ")
            while not opcion_valida2(opcion2):
                print("--------------------------")
                print("Opcion NO valida")
                menu_opciones_text()
                print("--------------------------")
                opcion2 = input("Seleccione una opcion: ")
            else:
                
                
#----------------------------------------------------------------------------------------------------------------------------------
#                                                       OPCION 1 DEL MENU
#----------------------------------------------------------------------------------------------------------------------------------
               
#Valida si la opcion seleccionada es 1                
                if (opcion2 == menu_opcion_list2[0]):
                    print("--------------------------")
                    usuario_envia = input("Ingrese el codigo de quien envia: ")
#Valida si el usuario existe                    
                    while not esusuario(usuario_envia):
                        print("--------------------------")
                        print("Codigo invalido")
                        usuario_envia = input("Ingrese el codigo de quien envia: ")
                    else:
#Valida que el codigo del remitente y destinatario sean diferentes 
                        while (usuario_login == usuario_envia): 
                            print("---------------------------")   
                            print("El codigo del usuario que envia debe ser diferente al suyo")
                            usuario_envia = input("Ingrese el codigo de quien envia: ")    
                        else:
#Valida si el codigo del remitente existe
                            while not esusuario(usuario_envia):
                                print("--------------------------")
                                print("Codigo invalido")
                                usuario_envia = input("Ingrese el codigo de quien envia: ")
                            else:
#Valida si la moneda ingresada existe en CoinMarket
                                print("--------------------------")
                                moneda = input("Indique el nombre de la moneda: ") 
                                while not esmoneda(moneda):
                                    print("--------------------------")
                                    print("Moneda Invalida.")
                                    moneda = input("Indique el nombre de la moneda: ")   
                                else:
#Expresion regular para solo recibir numeros
                                    print("--------------------------")
                                    cantidad = input("Indique la cantidad a recibir: ")
                                    esnumero =  re.match(exp_regular,cantidad)
#Valida si la cantidad ingresada es un numero
                                    while not esnumero:
                                        print("--------------------------")
                                        print("Error Ingrese un valor numerico")
                                        cantidad = input("Indique la cantidad: ")
                                        esnumero =  re.match(exp_regular,cantidad)
                                    else:
#Obtiene la ubicacion del dinero tanto como para el remitente y destinatario
                                        posicion = usuarios_list.index(usuario_login)
                                        posicion_envia = usuarios_list.index(usuario_envia)
#Valida que el remitente tenga fondos suficientes
                                        while float(cantidad) > float(montos_list[posicion_envia]):
                                            print("--------------------------")
                                            print("Fondos insuficientes")
                                            cantidad = input("Indique la cantidad a recibir: ")
                                            esnumero =  re.match(exp_regular,cantidad)
                                            while not esnumero:
                                                print("--------------------------")
                                                print("Error Ingrese un valor numerico")
                                                cantidad = input("Indique la cantidad: ")
                                                esnumero =  re.match(exp_regular,cantidad)
                                        else:
#Valida que la cantidad ingresada sea un numero
                                            while not esnumero:
                                                print("--------------------------")
                                                print("Error Ingrese un valor numerico")
                                                cantidad = input("Indique la cantidad: ")
                                                esnumero =  re.match(exp_regular,cantidad)
                                            else:
                                                montos_list[posicion] = float(montos_list[posicion]) + float(cantidad)
                                                montos_list[posicion_envia] = float(montos_list[posicion_envia]) - float(cantidad)
#Imprime los nuevos saldos.                         
                                                print("------------------------------------------------------------------")
                                                print("Usuario:",usuario_login,"\nSaldo anterior:",(float(montos_list[posicion])-float(cantidad)),"\nNuevo saldo:",montos_list[posicion])
                                                print("------------------------------------------------------------------")
                                                print("Usuario:",usuario_envia,"\nSaldo anterior:",(float(montos_list[posicion_envia]) + float(cantidad)),"\nNuevo saldo:",montos_list[posicion_envia])
                                                print("------------------------------------------------------------------")
                                                
                                                print("1. Mostrar historial \n2.Salir")
                                                opcion3= input("Ingrese una opcion:")
 #Valida que la cantidad ingresada sea valida
                                                while not opcion_valida3(opcion3):
                                                    print("--------------------------")
                                                    print("Opciono NO valida")
                                                    print("1. Mostrar historial \n2.Salir")
                                                    opcion3= input("Ingrese una opcion:")
                                                else:
                                                    if (opcion3 == menu_historial[0]):
                                                        print("Fecha:",datetime.today(),"\nMoneda:",moneda,"\nTipo de operacion:",nom_opciones[0],"\nCodigo de usuario",usuario_login,"\nCantidad recibida",cantidad,"\nSaldo anterior:",(float(montos_list[posicion])-float(cantidad)),"\nNuevo saldo:",montos_list[posicion])
                                                    else:
                                                        print("Adios -",usuario_login)
                                                    
                                                    
                
                
#----------------------------------------------------------------------------------------------------------------------------------
#                                                       OPCION 2 DEL MENU
#----------------------------------------------------------------------------------------------------------------------------------
               
#Valida si la opcion seleccionada es 2                
                elif (opcion2 == menu_opcion_list2[1]):
                    print("--------------------------")
                    usuario_envia = input("Ingrese el codigo de quien recibe: ")
#Valida si el usuario existe                    
                    while not esusuario(usuario_envia):
                        print("--------------------------")
                        print("Codigo invalido")
                        usuario_envia = input("Ingrese el codigo de quien recibe: ")
                    else:
#Valida que el codigo del remitente y destinatario sean diferentes 
                        while (usuario_login == usuario_envia):
                            print("--------------------------")    
                            print("El codigo del usuario quien recibe debe ser diferente al suyo")
                            usuario_envia = input("Ingrese el codigo de quien recibe: ")    
                        else:
#Valida si el codigo del destinatario existe
                            while not esusuario(usuario_envia):
                                print("--------------------------")
                                print("Codigo invalido")
                                usuario_envia = input("Ingrese el codigo de quien recibe: ")
                            else:
#Valida si la moneda ingresada existe en CoinMarket
                                print("--------------------------")
                                moneda = input("Indique el nombre de la moneda: ") 
                                while not esmoneda(moneda):
                                    print("--------------------------")
                                    print("Moneda Invalida.")
                                    moneda = input("Indique el nombre de la moneda: ")   
                                else:
#Expresion regular para solo recibir numeros
                                    print("--------------------------")
                                    cantidad = input("Indique la cantidad a enviar: ")
                                    esnumero =  re.match(exp_regular,cantidad)
#Valida si la cantidad ingresada es un numero
                                    while not esnumero:
                                        print("--------------------------")
                                        print("Error Ingrese un valor numerico")
                                        cantidad = input("Indique la cantidad: ")
                                        esnumero =  re.match(exp_regular,cantidad)
                                    else:
#Obtiene la ubicacion del dinero tanto como para el remitente y destinatario
                                        posicion = usuarios_list.index(usuario_login)
                                        posicion_envia = usuarios_list.index(usuario_envia)
#Valida que el remitente tenga fondos suficientes
                                        while float(cantidad) > float(montos_list[posicion]):
                                            print("--------------------------")
                                            print("Fondos insuficientes")
                                            cantidad = input("Indique la cantidad a enviar: ")
                                            esnumero =  re.match(exp_regular,cantidad)
                                        else:
#Valida si la cantidad ingresada sea un numero
                                            while not esnumero:
                                                print("--------------------------")
                                                print("Error Ingrese un valor numerico")
                                                cantidad = input("Indique la cantidad: ")
                                                esnumero =  re.match(exp_regular,cantidad)
                                            else:
                                                montos_list[posicion] = float(montos_list[posicion]) - float(cantidad)
                                                montos_list[posicion_envia] = float(montos_list[posicion_envia]) + float(cantidad)
#Imprime los nuevos saldos. 
                                                print("------------------------------------------------------------------")
                                                print("Usuario:",usuario_login,"\nSaldo anterior:",(float(montos_list[posicion])+float(cantidad)),"\nNuevo saldo:",montos_list[posicion])
                                                print("------------------------------------------------------------------")
                                                print("Usuario:",usuario_envia,"\nSaldo anterior:",(float(montos_list[posicion_envia]) - float(cantidad)),"\nNuevo saldo:",montos_list[posicion_envia])
                                                print("------------------------------------------------------------------")
                                                
                                                print("--------------------------")
                                                print("1. Mostrar historial \n2.Salir")
                                                opcion3= input("Ingrese una opcion:")
 #Valida que la opcion ingresada sea valida
                                                while not opcion_valida3(opcion3):
                                                    print("--------------------------")
                                                    print("Opciono NO valida")
                                                    print("1. Mostrar historial \n2.Salir")
                                                    opcion3= input("Ingrese una opcion:")
                                                else:
                                                    if (opcion3 == menu_historial[0]):
                                                        print("--------------------------")
                                                        print("Fecha:",datetime.today(),"\nMoneda:",moneda,"\nTipo de operacion:",nom_opciones[1],"\nCodigo de usuario",usuario_login,"\nCantidad enviada",cantidad,"\nSaldo anterior:",(float(montos_list[posicion])+float(cantidad)),"\nNuevo saldo:",montos_list[posicion])
                                                    else:
                                                        print("Adios -",usuario_login)


#----------------------------------------------------------------------------------------------------------------------------------
#                                                       OPCION 3 DEL MENU
#----------------------------------------------------------------------------------------------------------------------------------
                                                        
#Muestra el balance en dolares de la moneda ingresada
                elif opcion2 == menu_opcion_list2[2]:
                    print("--------------------------")
                    moneda = input("Indique el nombre de la moneda: ")
                    while not esmoneda(moneda):
                        print("--------------------------")
                        print("Moneda Invalida.")
                        moneda = input("Indique el nombre de la moneda a verificar: ")
                    else:
                        posicion = usuarios_list.index(usuario_login)
                        print("------------------------------------------------------------------") 
                        print("Su saldo actual en",moneda,"es:",montos_list[posicion],"USD")
                        print("------------------------------------------------------------------") 
                        datos(moneda)
                        
#----------------------------------------------------------------------------------------------------------------------------------
#                                                       OPCION 4 DEL MENU
#----------------------------------------------------------------------------------------------------------------------------------
#Muestra el balance general en dolares de todas las monedas disponebles en CoinMarket
                elif opcion2 == menu_opcion_list2[3]:
                    print("------------------------------------------------------------------")
                    print("BALANCE GENERAL")
                    print("------------------------------------------------------------------") 
                    data_monedas()

#----------------------------------------------------------------------------------------------------------------------------------
#                                                       OPCION 5 DEL INGRESO
#----------------------------------------------------------------------------------------------------------------------------------
                elif opcion2 == menu_opcion_list2[4]:
                    if (len(historial)>0):
                        print("--------------------------")
                        print(historial)
                    else:
                        print("--------------------------")
                        print("No hay historial disponible")