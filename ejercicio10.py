# Diseñe un algoritmo que pida por teclado la edad de una persona y la categorice de la siguiente manera:
#a. Si es menor de 18 años y mayor de 12 años (Adolescente)
#b. Si es menor o igual a 12 años (Niño)
#c. Si es mayor o igual a 18 años y menor de 24 años (Adulto)
#d. Si es mayor o igual a 24 años y menor a 65 (Adulto)
#e. Si es mayor o igual a 65 años (Adulto mayor)
#Para valores menores que cero informar al usuario que se encuentra fuera de rango.

def edad_persona(edad):
  if edad < 1:
    rango = "Está fuera del rango."
  if edad > 1 and edad <= 12:
    rango = "Niño"
  elif edad < 18 and edad > 12:
    rango = "Adolescente"
  elif (edad >= 18 and edad < 24) or (edad >= 24 and edad < 65):
    rango = "Adulto"
  elif edad >= 65:
    rango = "Adulto mayor"
  
  return rango

#Variable usuario
edad = int(input("Ingrese su edad: "))
print(edad_persona(edad))