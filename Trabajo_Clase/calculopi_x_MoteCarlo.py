import random
import math

cuantos = 1000
cuantos_si = 0

for i in range(cuantos):
    x = random.random()
    y = random.random()
    
    y_calculada = math.sqrt(1-x*x)
    if y>y_calculada:
        None
    else:
        cuantos_si += 1
        
cuarto_de_area = float(cuantos_si) / float(cuantos)

print("El cuarto del area es:", cuarto_de_area)
pi = cuarto_de_area * 4
    
print("Pi es igual a: ", pi)   