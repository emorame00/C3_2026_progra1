'''
Condicional simple
if condición: 
    código a ejecutar SI se cumple la condición 

if age > 18:  # 12 > 18: False
    print("Es mayor de edad") 
'''

'''
Condicional doble
if condición: 
    código a ejecutar SI se cumple la condición 
else: 
    código a ejecutar si NO se cumple la condición


if age >= 18:  # 18 >= 18: True
    print("Es mayor de edad") 
else:
    print("Es menor de edad")
'''

'''
Condicional múltiple
if condición: 
    código a ejecutar SI se cumple la condición 
elif condición: 
    código a ejecutar SI se cumple la condición
else: 
    código a ejecutar si NO se cumplen las condicionales previas
'''

age = 100


if age < 0:                     
    print("Error: La edad debe ser un número positivo")
elif age == 0:
    print("Es un bebé")
elif age < 12:                  
    print("Es un infante")
elif age < 18:                  
    print("Es adolescente")
elif age < 65:                  
    print("Es adulto")
else:                  
    print("Es adulto mayor")


'''
Ejercicio: Modifique el programa anterior para: 
    - edad < 65 muestre es un adulto
    - edad mayor o igual a 65 muestre es un adulto mayor 
    - edad un número negativo muestre Error: La edad debe ser un número positivo 
'''