# Importa el módulo sys para acceder a los argumentos de línea de comandos
 
import sys


ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}


umbral = int(sys.argv[1])


ventas_filtradas = {}


for mes, valor_venta in ventas.items(): 
    
    if valor_venta > umbral:

        ventas_filtradas[mes] = valor_venta


print(ventas_filtradas)