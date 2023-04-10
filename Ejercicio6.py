import math

print ("Ingrese: ")
xa = float(input("Coordenadas de X de A: "))
ya = float(input("Coordenadas de Y de A: "))

xb = float(input("Coordenadas de X de B: "))
yb = float(input("Coordenadas de Y de B: "))

D = ( (xa-xb)**2 + (ya-yb)**2 )**0.5

print("La distancia es: ", D)