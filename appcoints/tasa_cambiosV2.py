import requests
from config import APIKEY

r = requests.get(f"https://rest.coinapi.io/v1/assets/?apikey={APIKEY}")

if r.status_code != 200:
    raise Exception("Error en consulta codigo de error:{}".format(r.status_code) )
                    
lista_general = r.json()
lista_criptos=[]
lista_no_criptos=[]

for item in lista_general:
    if item["type_is_crypto"] == 1:
        lista_criptos.append(item["asset_id"])
    else:
        lista_no_criptos.append(item["asset_id"])

print("lista_criptos: ",len(lista_criptos))
print("cantidad_no_criptos: ",len(lista_no_criptos))
                    
####################################################

moneda_cripto = input("ingrese una cripto moneda conocida: ").upper()


while moneda_cripto != "" and moneda_cripto.isalpha() == True:
    if moneda_cripto in lista_criptos: 
        r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={APIKEY}")

        respuesta = r.json()
        #ejercicio1: como capturamos el rate
        #ejercicio2: como capturar el error si los valores no son válidos
        #ejercicio3: creo un input para cargar la moneda digital

        if r.status_code == 200:
            print( "{:,.2f}€".format( respuesta["rate"]) )
            break
        else:
            print(respuesta["error"])

    moneda_cripto = input("ingrese una cripto moneda conocida: ").upper()
