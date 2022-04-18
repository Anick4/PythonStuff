from random import *

name = input('Dime tu nombre ')
number = round(uniform(1, 100))

print(f'{name}, he pensado un número entre el 1 y el 100 y tienes solo 8 intentos para adivinarlo')
trials = 8
print(number)
while trials >= 0:
    n = float(input(f'Inténtalo, te quedan {trials} intentos '))
    trials -= 1
    if trials == 0:
        print('No te quedan intentos')
        break
    if n == number:
        print('Resuelto')
        break
    if n < 1 or n > 100:
        print('Numero no permitido')
        continue
    if n < number:
        print('Has elegido un número menor al que yo he pensado')
        continue
    if n > number:
        print('Has elegido un número mayor al que yo he pensado')
        continue




