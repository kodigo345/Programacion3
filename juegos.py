import ahorcado
import adivinanza

print("°°°°°°°°°°°°°°°°°°°°°°°°°")
print("Elija su juego")
print("°°°°°°°°°°°°°°°°°°°°°°°°°")

print("(1) Ahorcado (2) Adivinanza")

juego = int(input("Seleccione el juego:  "))

if(juego==1):
    print("Ahorcado")
elif(juego==2):
    print("Jugando adivinanza")