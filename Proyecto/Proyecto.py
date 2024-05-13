#Funcion para el area del rectangulo.
def calcular_area_rectangulo():
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = base * altura
    print(f"El área del rectángulo es: {area}")

#Funcion para el area del triangulo. 
def calcular_area_triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = 0.5 * base * altura
    print(f"El área del triángulo es: {area}")

#Funcion para el area del circulo. 
def calcular_area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    area = 3.14159 * radio ** 2
    print(f"El área del círculo es: {area}")

#Menu de opciones.
def mostrar_menu():
    print("Seleccione una figura geométrica:")
    print("A) Rectángulo")
    print("B) Triángulo")
    print("C) Círculo")
    print("D) Salir")

#Ejecucion del programa.
def main():
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Ingrese una opción (A/B/C/D): ").upper()

        if opcion == 'A':
            calcular_area_rectangulo()
        elif opcion == 'B':
            calcular_area_triangulo()
        elif opcion == 'C':
            calcular_area_circulo()
        elif opcion == 'D':
            continuar = False
            print("¡Hasta luego!")
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()