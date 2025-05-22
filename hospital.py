print("Inicio del proceso de evaluación")

respuesta = input("¿Responde a estímulos? (s/n): ").lower()
if respuesta == 's':
    print("Valorar la necesidad de llevarlo al hospital más cercano")
    print("Fin")
else:
    print("Abrir la vía aérea")
    respuesta = input("¿Respira? (s/n): ").lower()
    if respuesta == 's':
        print("Permitirle posición de suficiente ventilación")
        print("Fin")
    else:
        print("Administrar 5 ventilaciones y llamar a ambulancia")
        respuesta = input("¿Tiene signos de vida? (s/n): ").lower()
        if respuesta == 's':
            respuesta = input("¿Llegó la ambulancia? (s/n): ").lower()
            if respuesta == 's':
                print("Fin")
            else:
                print("Reevaluar a la espera de la ambulancia")
        else:
            print("Administrar compresiones torácicas hasta que llegue la ambulancia")


