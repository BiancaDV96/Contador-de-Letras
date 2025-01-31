#Paso 1: Solicitar entrada al usuario

from faulthandler import cancel_dump_traceback_later


palabra_ingresada = input("Por favor ingrese una palabra")

#Paso 2: Contar la cantidad de letras

cant_letras = len(palabra_ingresada)


#Paso 3: Mostrar al usuario el resultado

print("La palabra ingresada tiene", cant_letras,"letras")