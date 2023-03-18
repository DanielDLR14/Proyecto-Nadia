# Importar módulos necesarios
import re  # módulo de expresiones regulares para validar la entrada del usuario
import json  # módulo para trabajar con archivos JSON

# Pedir cantidad de estudiantes
while True:
    try:
        print("="*50)
        n = int(input("Ingrese la cantidad de estudiantes: "))  # pedir al usuario que ingrese un número
        print("="*50)
        break  # salir del ciclo si se ingresa un número válido
    except ValueError:  # manejar el error si el usuario ingresa algo que no es un número
        print("Por favor, ingrese un número válido.")

# Crear diccionario de estudiantes
estudiantes = {}  # crear un diccionario vacío para almacenar los datos de los estudiantes
for i in range(n):  # iterar la cantidad de veces especificada por el usuario
    print("="*50)
    print(f"Ingrese los datos del estudiante {i+1}")  # mostrar el número de estudiante actual
    print("="*50)
    
    # Solicitar datos del estudiante
    while True:
        nombre = input("Nombre: ")  # pedir al usuario que ingrese el nombre del estudiante
        if nombre.isdigit():  # verificar si el nombre contiene solo dígitos
            print("Por favor, ingrese un nombre válido.")
        else:
            break  # salir del ciclo si se ingresa un nombre válido

    while True:
        try:
            edad = int(input("Edad: "))  # pedir al usuario que ingrese la edad del estudiante
            break  # salir del ciclo si se ingresa un número válido
        except ValueError:  # manejar el error si el usuario ingresa algo que no es un número
            print("Por favor, ingrese un número válido.")

    while True:
        matricula = input("Matrícula (XX-XXXX): ")  # pedir al usuario que ingrese la matrícula del estudiante
        if not re.match(r'\d{2}-\d{4}', matricula):  # verificar si la matrícula tiene el formato correcto
            print("La matrícula debe tener el formato XX-XXXX")
        else:
            break  # salir del ciclo si se ingresa una matrícula válida

    estudiantes[nombre] = {  # agregar los datos del estudiante al diccionario
        'Edad': edad,
        'Matrícula': matricula
    }

# Guardar datos en archivo JSON
with open('estudiantes.json', 'w') as f:  # abrir un archivo JSON en modo escritura
    json.dump(estudiantes, f)  # escribir los datos del diccionario en el archivo

# Loop para buscar estudiantes y mostrar detalles
while True:
    print("\n" + "="*50)
    print("Buscar Estudiante".center(50))
    print("="*50)
    
    # Solicitar nombre del estudiante
    nombre = input("Ingrese el nombre del estudiante para mostrar detalles: ")
    
    # Verificar si el nombre existe en el diccionario de estudiantes
    if nombre in estudiantes:
        # Si el nombre existe, imprimir los detalles del estudiante
        print("\n" + "="*50)
        print(f"Detalles de {nombre}".center(50))
        print("="*50)
        print(f"Edad: {estudiantes[nombre]['Edad']}")
        print(f"Matrícula: {estudiantes[nombre]['Matrícula']}")
        
        # Preguntar al usuario si desea buscar detalles de otro estudiante
        respuesta = input("\n¿Desea buscar detalles de otro estudiante? (sí/no): ").strip().lower()
        
        # Validar la respuesta del usuario
        while respuesta not in ['sí', 'si', 'no']:
            respuesta = input("\nPor favor, responda 'si' o 'no': ").strip().lower()
            
        # Si la respuesta es 'no', terminar el programa
        if respuesta in ['no']:
            print("\n" + "="*50)
            print("Programa cerrado".center(50))
            print("="*50)
            break
    else:
        # Si el nombre no existe, imprimir un mensaje de error
        print("\n" + "="*50)
        print("No hay estudiantes con ese nombre".center(50))
        print("="*50)


