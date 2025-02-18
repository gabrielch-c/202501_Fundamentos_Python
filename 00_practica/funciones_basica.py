def multiplicando(valor):
    result = []
    for i in range(valor + 1):
        result.append(i * 2)
    return result

result = multiplicando(7)
print(result)

def sumaRest(x,y):
    suma = x + y
    resta = x - y
    print(suma)
    return resta

resultado = sumaRest(3, 5)
print(resultado)


def sumLong(numeros):
    suma = sum(numeros)
    longitud = len(numeros)
    return suma - longitud

resultado = sumLong([1,2,3,4])
print(f"el resultado es {resultado}")


def listaMultiplicacion(numeros):
    if len(numeros) < 2:
        print(len(numeros))
        return []
    multiplicador = numeros[1]
    Lista_nueva = [x * multiplicador for x in numeros]
    print(Lista_nueva)
    return Lista_nueva

resultado = listaMultiplicacion([1,2,3,4])
print(resultado)

def valor_multiplicado_longitud(valor, longitud):
    listaNueva = [valor * longitud] * longitud
    return listaNueva

resultado = valor_multiplicado_longitud(5, 2)
print(resultado)