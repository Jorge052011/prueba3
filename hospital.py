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

        signos_vida = input("¿Tiene signos de vida? (s/n): ").lower()
        while signos_vida == 's':
            print("reevaluar a la espera  ")
            ambulancia = input("¿Llegó la ambulancia? (s/n): ").lower()
            if ambulancia == 's':
                print("Fin")
                break
            else:
                print("administrar compresiones toracicas   ")
                ambulancia = input("¿llegó la ambulancia? (s/n): ").lower()

        while signos_vida != 's':
            print("Administrar compresiones torácicas hasta que llegue la ambulancia")
            ambulancia1 = input("¿Llegó la ambulancia? (s/n): ").lower()
            if ambulancia1 != 's':
                signos_vida = input("tiene signos de vida?")
                ambulancia1 = input("llego la ambulancia?").lower
                elif ambulancia1 = 's':
                    print("fin")
                    break
