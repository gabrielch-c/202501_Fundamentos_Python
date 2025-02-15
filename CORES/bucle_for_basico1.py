#Básico: imprime todos los números enteros del 0 al 100.

for indice in range(101):
    print(indice)

#Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500

for indice in range(0,502,2):
    print(indice)

#Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
for indice in range(101):
    if indice % 10 == 0:
        print("baby")
    elif indice % 5 == 0:
        print("ice ice")
    else:
        print(indice)

#Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
x = 0

for indice in range(0, 500001, 2):
    x += indice

print(x)

#Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
for indice in range(2024, 0, -3):
    print (indice)

#Contador dinámico
numInicial = 5
numFinal = 15
multiplo = 2

for indice in range(numInicial, numFinal + 1):
    if indice % multiplo == 0:
        print(indice)