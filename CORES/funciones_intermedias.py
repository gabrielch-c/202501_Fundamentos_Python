#1. Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [

{"nombre": "Ricky Martin", "pais": "Puerto Rico"},

{"nombre": "Chayanne", "pais": "Puerto Rico"}

]

ciudades = {

"México": ["Ciudad de México", "Guadalajara", "Cancún"],
"Chile": ["Santiago", "Concepción", "Viña del Mar"]

}

coordenadas = [

{"latitud": 8.2588997, "longitud": -84.9399704}

]

matriz[1][0] = 6
print(matriz)

cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)

ciudades["México"][2] = "Monterrey"
print(ciudades)

coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

#2. Iterar a través de una lista de diccionarios

cantantes = [

{"nombre": "Ricky Martin", "pais": "Puerto Rico"},

{"nombre": "Chayanne", "pais": "Puerto Rico"},

{"nombre": "José José", "pais": "México"},

{"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]


def iterarDiccionario(lista):
    for x in range (len(lista)):
        print(f"nombre - {lista[x]["nombre"]}, pais - {lista[x]["pais"]}")

resultado = iterarDiccionario(cantantes)
print(resultado)

#3. Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
    for item in range(len(lista)):
        print(f"{cantantes[item][llave]}")

resultadoNombre = iterarDiccionario2("nombre", cantantes)
print(resultadoNombre)

resultadoPais = iterarDiccionario2("pais", cantantes)
print(resultadoPais)

#4. Iterar a través de un diccionario con valores de lista

costa_rica = {

"ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

"comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}

def imprimirInformacion(diccionario):
    for llave, lista in diccionario.items():
        print(len(lista), llave)
        for i in lista:
            print(i)


resultado = imprimirInformacion(costa_rica)
print(resultado)
