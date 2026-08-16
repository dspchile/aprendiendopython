#Sistema para cálculo de ciclo menstrual
#Versión 1.0.0 - Daniel Sandoval Parra, Disponible como @dspchile en GitHub
#Primera parte: Recolección de datos
import datetime
from datetime import date
from datetime import datetime, timedelta
print("Bienvenido al sistema de evaluación del ciclo menstrual.")
print("")
print("Para inciar, se requiere la información sobre la duración de tu ciclo.")
print("¿Sabes cuántos días dura regularmente tu ciclo menstrual?")
PROCESO = input("0 -> SÍ y 1 -> NO: ")
if PROCESO == "0":
    print("")
    D = input("Por favor, indica cuántos días dura regularmente tu ciclo menstrual: ")
else: 
    print("")
    print("¡No te preocupes, se puede calcular!")
    print("")
    print("Se requiere información sobre la fecha de tus últimas dos menstruaciones")
    print("")
    print("Dicta por partes la fecha de tu ANTEPENÚLTIMA menstruación: ")
    DIA1 = input("Día (número): ")
    MES1 = input("Mes (número): ")
    ANO1 = input("Año: ")
    DIA1 = int(DIA1)
    MES1 = int(MES1)
    ANO1 = int(ANO1)
    FECHA1 = date(ANO1, MES1, DIA1)
print("")
print("Ahora, dicta por partes la fecha de tu ÚLTIMA menstruación: ")
DIA2 = input("Día (número): ")
MES2 = input("Mes (número): ")
ANO2 = input("Año: ")
DIA2 = int(DIA2)
MES2 = int(MES2)
ANO2 = int(ANO2)
FECHAINICIO = date(ANO2, MES2, DIA2)
print("")
print("Calculando...")
if PROCESO == "1":
    D = (FECHAINICIO - FECHA1)
    D = D.days
else: 
    print("")
FECHAACTUAL = date.today()
DIASCORRIDOS = FECHAACTUAL - FECHAINICIO
DIASCORRIDOS = DIASCORRIDOS.days
D = str(D)
DIASCORRIDOS = str(DIASCORRIDOS)
print("Estamos calculando sobre un ciclo menstrual de " + D + " días. Han corrido, hasta ahora, " + DIASCORRIDOS + " días del ciclo.")
DIASCORRIDOS = int(DIASCORRIDOS)
D = int(D)
print("")
print("")
#Variables del sistema
#A - FASE
#B - OVULACIÓN 
#C - PRÓXIMA MENSTRUACIÓN
#Cálculo anticipado de variables.
#Variables A: FASE
if 0 <= DIASCORRIDOS < (D-14):
    FASE = "Preovulatoria"
elif DIASCORRIDOS == (D-14):
    FASE = "Día de ovulación"
else: 
    FASE = "Postovulatoria"
#Variables B: OVULACIÓN Y VENTANA FÉRTIL
LAPSO = (D-14)-DIASCORRIDOS
LAPSO = int(LAPSO)
FECHAOVULACION = FECHAACTUAL + timedelta(days=LAPSO)
FECHAINICIOVENTANA = FECHAOVULACION + timedelta(days=-2)
FECHAFINVENTANA = FECHAOVULACION + timedelta(days=2)
FECHAINICIOVENTANA = FECHAINICIOVENTANA.strftime(("%d-%m-%Y"))
FECHAFINVENTANA = FECHAFINVENTANA.strftime(("%d-%m-%Y"))
FECHAINICIOVENTANAPRES = str(FECHAINICIOVENTANA)
FECHAFINVENTANAPRES = str(FECHAFINVENTANA)
VENTANA = "entre el " + FECHAINICIOVENTANAPRES + " y el " + FECHAFINVENTANAPRES
#Variable C: PRÓXIMA MENSTRUACIÓN
FECHAPROX = FECHAINICIO + timedelta(days=D)
FECHAPROX = FECHAPROX.strftime("%d-%m-%Y")
DIASFALTANTES = D - DIASCORRIDOS
while True:
    print("Menú:")
    print("1 -> Conocer FASE")
    print("2 -> Conocer FECHA DE OVULTACIÓN Y VENTANA FÉRTIL")
    print("3 -> Conocer FECHA DE PRÓXIMA MENSTRUACIÓN")
    print("0 -> SALIR")
    DECISION = input("Introduce el número: ")
    if DECISION == "1":
        print(" ")
        print(" ")
        print("Estás en la fase: " + FASE + ".")
        print(" ")
        print("Volviendo al menú...")
        print(" ")
        continue
    elif DECISION == "2":
        print(" ")
        print(" ")
        FECHAOVULACION = FECHAOVULACION.strftime("%d-%m-%Y")
        FECHAOVULACION = str(FECHAOVULACION)
        print("Vas a ovular el " + FECHAOVULACION + " con una ventana fértil " + VENTANA)
        print(" ")
        print("Volviendo al menú...")
        print(" ")
        continue
    elif DECISION == "3":
        print(" ")
        print(" ")
        FECHAPROX = str(FECHAPROX)
        DIASFALTANTES = str(DIASFALTANTES)
        print("Tu próxima menstruación comenzará el " + FECHAPROX + " en " + DIASFALTANTES + " días faltantes.")
        print(" ")
        print("Volviendo al menú...")
        print(" ")
        continue
    elif DECISION == "0":
        print("Gracias por usar el programa.")
        break
    else:
        print("Error en la introducción de número. Volviendo al menú...")
        print(" ")
        continue
print("Daniel Sandoval Parra, 2026.")

