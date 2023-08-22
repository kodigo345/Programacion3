import random
def jugar_adivinanza():
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("Bienvenido al juego de adivinanza")
    print()
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")

    numero_secreto=random.randrange(1,101)
    puntaje=1000

    print("Seleccione el nivel de dificultad")
    print("(1) Fácil (2) Medio (3) Dificil")

    nivel = int(input("Ingrese nivel de dificultad: "))
    if(nivel==1):
      total_intentos = 20
    elif(nivel==2):
      total_intentos = 10
    else:
      total_intentos = 5

    for iteracion in range (1, total_intentos +1):
      print("Intento: {} de {}".format(iteracion,total_intentos))
      entrada=input("Digite un número entre 1 y 100: ")
      entrada=int(entrada)
      print("Digitaste...",entrada)
      if(entrada<1 or entrada>100):
        print("Ingresar un número entre 1 y 100: ")
        continue

      acertaste=entrada==numero_secreto #Iguales
      mayor=entrada>numero_secreto #Entrada es mayor
      menor=entrada<numero_secreto #Entrada es menor

      if(acertaste):
        print("Felicitaciones, adivinaste el número y ganaste {} puntos".format(puntaje))
        break
      elif(mayor):
        print("Lo siento, el número que ingresaste es mayor al secreto")
      else:
        print("Lo siento, el número que ingresaste es menor al secreto")

      puntos_perdidos=abs(numero_secreto-entrada)
      puntaje=puntaje-puntos_perdidos

    print("Fin del juego")
