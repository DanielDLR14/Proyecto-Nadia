# Importando el módulo csv que nos permitirá trabajar con archivos CSV en Python.
import csv

# Abriendo el archivo CSV "wendys-menu.csv" en modo lectura y convirtiéndolo en
# una lista de diccionarios.
with open('wendys-menu.csv') as f:   # Abre el archivo CSV en modo lectura y lo asigna a la variable 'f'
    reader = csv.DictReader(f)       # Crea un objeto DictReader a partir del archivo CSV 'f'
    menu = [row for row in reader]   # Convierte el objeto DictReader en una lista de diccionarios llamada 'menu'

# Creando un diccionario para almacenar el total de calorías y el número de
# alimentos en cada categoría.
calorias_promedio = {}   # Crea un diccionario vacío llamado 'calorias_promedio'
for item in menu:        # Recorre cada elemento del 'menu' que es una lista de diccionarios
    categoria = item['Category']          # Obtiene la categoría del elemento actual
    calorias = float(item['Calories'])    # Obtiene la cantidad de calorías del elemento actual como un valor flotante
    # Si la categoría ya existe en el diccionario, actualizamos el total de
    # calorías y el número de alimentos para esa categoría.
    if categoria in calorias_promedio:    # Verifica si la categoría ya está en el diccionario 'calorias_promedio'
        calorias_promedio[categoria]['total_calorias'] += calorias   # Si está en el diccionario, actualiza el valor de calorías totales para esa categoría
        calorias_promedio[categoria]['num_alimentos'] += 1           # También actualiza el número de elementos en esa categoría
    # De lo contrario, agregamos una nueva entrada al diccionario con el total
    # de calorías y el número de alimentos para esa categoría.
    else:                                 # Si la categoría no está en el diccionario, la agrega
        calorias_promedio[categoria] = {'total_calorias': calorias, 'num_alimentos': 1}

# Calculando el promedio de calorías para cada categoría en el diccionario
# calorias_promedio.
for categoria, valores in calorias_promedio.items():  # Recorre el diccionario 'calorias_promedio' y obtiene la categoría y los valores asociados
    # Calculando el promedio redondeado a dos decimales.
    promedio = round(valores['total_calorias'] / valores['num_alimentos'], 2)   # Calcula el promedio de calorías por elemento en la categoría actual
    # Agregando el promedio al diccionario de esa categoría.
    calorias_promedio[categoria]['promedio_calorias'] = promedio  # Agrega el promedio de calorías para la categoría actual al diccionario 'calorias_promedio'

# Creando una lista de diccionarios
resultados = [{categoria: valores['promedio_calorias']}  # Crea una lista de diccionarios que contienen la categoría y el promedio de calorías para esa categoría
              for categoria, valores in calorias_promedio.items()]

print("[") # Imprime una apertura de corchete para la lista de resultados
for i, resultado in enumerate(resultados): # Itera sobre cada resultado en la lista de resultados
    categoria, promedio_calorias = list(resultado.items())[0] # Obtiene la categoría y el promedio de calorías para el resultado actual
    print("\n  {") # Imprime una apertura de llave para el resultado actual
    print(f"    '{categoria}': {promedio_calorias:.2f}") # Imprime la categoría y el promedio de calorías para el resultado actual, formateado para mostrar sólo dos decimales
    print("  }" if i == len(resultados) - 1 else "  },") # Imprime una cerradura de llave para el resultado actual, seguido de una coma si no es el último resultado, o una cerradura de corchete si es el último
print("]") # Imprime una cerradura de corchete para la lista de resultados

