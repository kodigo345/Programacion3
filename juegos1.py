import ahorcado2
import adivinanza2

print("°°°°°°°°°°°°°°°°°°°°°°°°°")
print("Elija su juego")
print("°°°°°°°°°°°°°°°°°°°°°°°°°")

print("(1) Ahorcado (2) Adivinanza")

juego = int(input("Seleccione el juego:  "))

if(juego==1):
    print("Jugando ahorcado")
    ahorcado.jugar_ahorcado()
elif(juego==2):
    print("Jugando adivinanza")
    adivinanza.jugar_adivinanza()