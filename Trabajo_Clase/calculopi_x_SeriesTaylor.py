acumulador = 0.0

contador = 0
division_actual = 1.0
es_suma = True

while division_actual > 0.00052:
    contador += 1
    division_actual = 1/contador
    
    if contador % 2 != 0:
        if es_suma:
            acumulador += division_actual
        else:
            acumulador -= division_actual
        es_suma = not es_suma
        
print("El cuarto del area es:", acumulador)
pi = acumulador * 4
    
print("Pi es igual a: ", pi)
            