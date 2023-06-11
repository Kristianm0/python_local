#Juego de piedra papel o tijera ✊ ✌️ 🫲

# Importamos la libreria random para que elija una opcion.
import random

#Creamos la opciones de la computadora.
# Es un variable con texto.
options = (
    """ ✊ Piedra", 
        🫲 Papel", 
        ✌️ Tijera """)

# Creamos un medidor de los puntos de la computadora y del usuario con variables que comienzen en 0.
computer_wins = 0
user_wins = 0

# Creamos la variable que almacene los raounds.
rounds = 1


## Ciclo
# Creamos los whiles  para que repita el juego.
while True: 
    # Este print para dividir la pantalla.
    print("*"*10)
    # Print para mostrar las partidas ganadas de cada usuario.
    print("ROUND", rounds)
    print("Computadora ->", computer_wins)
    print("Usuario -> ", user_wins)
    print("*"*10)


    #Pedimos y mostramos las opciones
    user_option = input("Elige: Piedra ✊, Papel 🫲 o tijera ✌️ => ")
    # Pasamos el mensaje del usuario a lower para que el if no se confunda.
    user_option = user_option.lower()
    # Llamaos a la funcion random.choice
    computer_option = random.choice(options)

    # Le mostramos al usuario los resultados
    # Divimos la pnatalla
    print("")
    print("-"*10)
    # Mostramos una guia al usuario de como va el juego.
    print("Contrincantes")
    print("User option ->", user_option)
    print(f"Computer option -> {computer_option}")
    print("")

    ## Condicionales 

    # Si la opcion de user es igual a la de la computador, es empate.
    if user_option == computer_option:
        print(("Empate."))
    
    # Le decimos si user no pone alguna de las opciones le mandamos el mensaje de que esta mal.
    if not user_option not in options:
        print("Esa opcion no es validad, trata de nuevo")
        continue




    ## Le decimos si es user es igual a esta opcion X, y la computadora es iguala Z  opcion el resultado es Y.

    #Le decimos que si la palabra piedra es igual a la palabra tijera, la piedra gana.
    elif user_option == "piedra":
        if computer_option == "tijera":
            #escribimos el resultado en pantalla.
            print("Piedra gana a tijera, user gano")
            #le sumamos al el punto o numero correpondiente a la variable del usuario el cual gano.
            user_wins +=1
        else: 
            print("Papel gana a piedra")
            print("Computer gano")
            computer_wins +=1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("Papel gana a piedra ")
            print("user gano")
            user_wins +=1
        else: 
            print("tijera gana a papel")
            print("computer gano")
            computer_wins +=1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("tijera gana a papel")
            print("user gano")
            user_wins +=1
        else:
            print("piedra gana a tijera")
            print("computer gano")
            computer_wins +=1
    # Vamos contando los rounds
    rounds +=1

        
    if computer_wins == 2:
        print(" Gano la computadora 🤣🤣🤣")
        print("Computadora ->", computer_wins)
        print("Usuario -> ", user_wins)
        break
    if user_wins == 2:
        print(" Ganastes, el usuario gano")
        print("Computadora ->", computer_wins)
        print("Usuario -> ", user_wins)
        break
