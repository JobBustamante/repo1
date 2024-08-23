#Algoritmo para calcular el tiempo transcurrido entre dos horas H-1 y H-2, los tiempos se ingresan por teclado en horas y minutos:
#- Tener en cuenta:
#- Si la diferencia entre los tiempos (horas) es negativa, se debe calcular su valor absoluto, debido a que no hay tiempos negativos.

#Ex: de 1 a 2 pasó 1 hr

#Importar librería math para truncar los decimales de un número
import math
def tiempo_transcurrido(h1,h2,m1,m2):
  #Pasar todo a minutos
  total_minutos1 = (h1 * 60) + m1
  total_minutos2 = (h2 * 60) + m2
  total_mins = total_minutos2 - total_minutos1
  if total_mins < 0:
    total_mins = abs(total_mins)

  if total_mins > 0:
    #Si hay menos de 60 minutos colocar solo en minutos
    if total_mins < 60:
      tiempo_total = f"Pasaron {total_mins} minutos."
    #Sino colocar en horas y minutos
    if total_mins == 60:
      tiempo_total = f"Pasó 1 hora."
    if total_mins > 60:
      en_horas = math.trunc(total_mins/60)
      #Multiplicar 60 con el valor entero en horas y al total restarle lo anterior
      en_minutos = total_mins -(60 * en_horas)
      tiempo_total = f"Pasaron {en_horas} horas y {en_minutos} minutos"

  return tiempo_total

#Variable usuario
hora1 = int(input("Ingrese la/s primera/s hora/s: "))
min1 = int(input("Ingrese los primeros minutos: "))
hora2 = int(input("Ingrese la/s segunda/s hora/s: "))
min2 = int(input("Ingrese los segundos minutos: "))
print("Calcularemos el tiempo transcurrido...\n")
print(tiempo_transcurrido(hora1,hora2,min1,min2))
