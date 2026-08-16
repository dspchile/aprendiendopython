#EJERCICIO 003 PROGRA100
#DANIEL ALBERTO SANDOVAL PARRA
#Codename: Lumbrera Py-Rebeca
print("Bienvenido al sistema de cálculo de promedio ponderado.")
print(" ")
print("Lumbrera Py-Rebeca, Daniel Sandoval Parra")
print(" ")
print("El sistema soporta hasta 4 notas distintas. Deben tener punto decimal (Ej: seis siete => 6.7)")
#Definir casos
numnotas = int(input("Indica el número de notas que tiene la asignatura: "))
if numnotas == 1:
    notaunica = float(input("Introduce tu nota única: "))
    pp = round(notaunica, 1)
    print(f"Tu promedio ponderado es: {pp}.")
elif numnotas == 2:
    #Definir n1 y n2
    n1 = float(input("Introduce tu nota 1: "))
    p1 = float(input("Introduce el valor en porcentaje de la nota 1 (XX)%: "))
    n2 = float(input("Introduce tu nota 2: "))
    p2 = float(input("Introduce el valor en porcentaje de la nota 2 (XX)%: "))
    pp = round(0.01*n1*p1 + 0.01*n2*p2,1)
    if p1 + p2 != 100:
        print("Error: Los porcentajes no suman 100%.")
    else: 
        print(f"Tu promedio ponderado es {pp}.")
elif numnotas == 3:
    n1 = float(input("Introduce tu nota 1: "))
    p1 = float(input("Introduce el valor en porcentaje de la nota 1 (XX)%: "))
    n2 = float(input("Introduce tu nota 2: "))
    p2 = float(input("Introduce el valor en porcentaje de la nota 2 (XX)%: "))
    n3 = float(input("Introduce tu nota 3: "))
    p3 = float(input("Introduce el valor en porcentaje de tu nota 3 (XX)%: "))
    pp = round(0.01*n1*p1 + 0.01*n2*p2 + 0.01*n3*p3,1)
    if p1 + p2 + p3 != 100:
        print("Error: Los porcentajes no suman 100%.")
    else: 
        print(f"Tu promedio ponderado es {pp}.")
elif numnotas == 4:
    n1 = float(input("Introduce tu nota 1: "))
    p1 = float(input("Introduce el valor en porcentaje de la nota 1 (XX)%: "))
    n2 = float(input("Introduce tu nota 2: "))
    p2 = float(input("Introduce el valor en porcentaje de la nota 2 (XX)%: "))
    n3 = float(input("Introduce tu nota 3: "))
    p3 = float(input("Introduce el valor en porcentaje de tu nota 3 (XX)%: "))
    n4 = float(input("Introduce tu nota 4: "))
    p4 = float(input("Introduce el valor en porcentaje de tu nota 4 (XX)%: "))
    pp = round(0.01*n1*p1 + 0.01*n2*p2 + 0.01*n3*p3 + 0.01*n4*p4,1)
    if p1 + p2 + p3 + p4 != 100:
        print("Error: Los porcentajes no suman 100%.")
    else: 
        print(f"Tu promedio ponderado es {pp}.")
else:
    print("Error: La capacidad del sistema es superada por la cantidad de notas.")