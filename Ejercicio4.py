print("Ingresa la cantidad de partidas ganadas, perdidas y empatadas")
pg = int(input("Ganadas: "))
pe = int (input("Empatadas: "))
pp = int (input("Perdidas: "))

ppg = pg*3
ppp = pp*0
ppe = pe*1

t = ppg+ppp+ppe

print("Puntos de partidas ganadas: ", ppg)
print("Puntos de partidas empatadas: ", ppe)
print("-------------------------------------")
print("Total: ", t)