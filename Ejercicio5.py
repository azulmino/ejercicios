import math

print("Ingresar GB")

GB = float(input())

MG = GB*1024
MD = MG/1.44

print(MD)
print("Discos necesarios: ", math.ceil(MD))