import requests
from .utils import *


moneda_cripto = input("ingrese una cripto moneda conocida: ").upper()


while moneda_cripto != "" and moneda_cripto.isalpha() == True:

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




"""
print("codigo de respuesta:",r.status_code)
print("cabecera:",r.headers["content-type"])
print("enconding:",r.encoding)
print("respuesta en string:",r.text)
print(type(r.text))
print("respuesta en json:",r.json())
print(type(r.json()))
"""
