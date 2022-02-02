import random
from playsound import playsound


numero = random.randint(1,100)
Intentos = []
mayor = 100
menor = 1
i =  1
ganador = "Ganador.mp3"


print("\x1b[0;34m"+"Cargando el juego")
print("\x1b[0;37m"+"He pensado un numero del intervalo [", menor ,",", mayor ,"]")
while (intento := int(input("Adivine el numero \U0001F52E:"))) != numero:
    i += 1
    Intentos.append(intento) 
    print("\x1b[0;31m"+"Te has equivocado")
    if intento > numero:
        if intento > mayor:
            print("\x1b[0;37m"+"Ahora el intervalo es [", menor ,",", mayor,"]")
        else:
            mayor = intento
            print("\x1b[0;37m"+"Ahora el intervalo es [", menor ,",", mayor,"]")
    else:
        if intento < menor:
            print("\x1b[0;37m"+"Ahora el intervalo es [", menor ,",", mayor ,"]")
        else:
            menor = intento
            print("\x1b[0;37m"+"Ahora el intervalo es [", menor ,",", mayor ,"]")


Intentos.append(intento)

if len(Intentos) <= 5:
    emoji = "\U0001F38A"
elif len(Intentos) >= 6 and len(Intentos) <10:
    emoji = "\U0001F603"
else:
    emoji = "\U0001F4A4"

print("\x1b[0;32m"+"Has adivinado, te tomo ",i,"intentos",emoji)
print("\x1b[0;37m"+"Tu historial de intentos es: ", Intentos)
playsound(ganador)