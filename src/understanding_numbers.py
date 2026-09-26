#NUMEROS
#ENTEROS = integers
"""
los numeros enteros los podemos sumar
(+) ,restar (-) multiplicar(*)
y dividir (/)
"""
print(2+3)
print(-15+12)
print(3-2)
print(2*3)
print(3/2)
number_1 = 5
number_2 = 10
print(number_1+number_2)

# Division entera //
# Potencias **n
print(3**2)
print(3**3)
print(10**6)
print(10%2)

age = 18
print(age)
name = "iancarlo"
print(name,age)


# Floats 
"""
python llama floats a cualquier numero con
punto decimal 
son los que tienen punto decimal 
"""
print(0.1+0.1)
print(0.2-0.2)
print(2*0.1)
print(2*0.2)

# imprimir la edad de alguien 

age = 34 # variable del tipo entero
# message = "charly tiene " + age + "años" (error)
message = "charly tiene " + str(age) + "años"
message_f = f"charly tiene {age} años."
print(message)
print(message_f)

"""
typeerror python no puede reconocer el tipo de 
informacion que se esta utiliando
"""
print(type(age))
print(type(0.1))
print(type(message_f))

