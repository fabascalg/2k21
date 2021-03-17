"""
    Ejercicio 4
"""


def TestType(data, tipo):
    test = isinstance(data, tipo)
    result = ""
    if test:
        result = f"El tipo coincide: {type(data)}"
    else:
        result = f"El tipo NO coincide: {type(data)}"
    return result


mi_lista = ["Hola mundo", 77]
titulo = "Master en Python"
numero = 100
verdadero = True
array_de_constantes = (10,"hola",False)

print(TestType(mi_lista, list))
print(TestType(titulo, str))
print(TestType(numero, int))
print(TestType(verdadero, bool))
print(TestType(array_de_constantes, list))