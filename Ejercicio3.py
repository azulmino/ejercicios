print("ingresar el numero de respuestas correctas, incorrectas y en blanco")
pc = int(input("Correctas: "))
pi = int(input("Incorrectas: "))
pb = int (input("En blanco: "))

ppc = pc*3
ppi = pc* -1
ppb = pb* 0

pf = ppc+ppi+ppb

print("Puntos respuestas correctas: ", ppc)
print("Puntos respuestas Incorrectas: ", ppi)
print("El puntaje final es: ", pf)