
import sys

#definición por diccionario
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

# se asocia a sys.argv[1] el valor de corte

umbral = int(sys.argv[1])

# Crea un nuevo diccionario 

# Se realiza una formula de una linea donde quedarán los valores 
ventas_filtradas = {mes: valor_venta for mes, valor_venta in ventas.items() if valor_venta > umbral}

# Imprime resultado
print(ventas_filtradas)