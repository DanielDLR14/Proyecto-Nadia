def leer_clientes():
    # Crea un diccionario vacío para almacenar la información de los clientes
    clientes = {}

    # Abre el archivo "clientes.txt" en modo lectura
    with open("clientes.txt", "r") as archivo:

        # Itera sobre cada línea del archivo
        for linea in archivo:

            # Divide cada línea en campos separados por "|" y almacena los campos en una lista llamada "data"
            data = linea.strip().split("|")

            # Almacena la primera columna (id del cliente) en una variable llamada "id_cliente"
            id_cliente = data[0]

            # Concatena las columnas 2 y 3 (nombre y apellido del cliente) y almacena el resultado en una variable llamada "nombre_cliente"
            nombre_cliente = data[1] + " " + data[2]

            # Reemplaza "Nombre Apellido" por "Cliente" en el nombre del cliente
            nombre_cliente = nombre_cliente.replace(
                "Nombre Apellido", "Cliente")

            # Agrega el par clave-valor "id_cliente:nombre_cliente" al diccionario de clientes
            clientes[id_cliente] = nombre_cliente

    # Devuelve el diccionario de clientes
    return clientes


def modificar_telefonos():
    # Obtiene el diccionario de clientes llamando a la función "leer_clientes()"
    clientes = leer_clientes()

    # Abre el archivo "telefonos.txt" en modo lectura y escritura
    with open("telefonos.txt", "r+") as archivo:

        # Lee todas las líneas del archivo y almacena cada línea como un elemento de una lista llamada "contenido"
        contenido = archivo.readlines()

        # Establece el cursor del archivo al inicio
        archivo.seek(0)

        # Itera sobre cada línea de la lista "contenido"
        for linea in contenido:

            # Divide cada línea en campos separados por ":" y almacena los campos en una lista llamada "data"
            data = linea.strip().split(":")

            # Almacena el primer campo (número de teléfono) en una variable llamada "telefono"
            telefono = data[0]

            # Almacena el segundo campo (id del cliente) en una variable llamada "id_cliente"
            id_cliente = data[1]

            # Almacena el tercer campo (tipo de plan) en una variable llamada "tipo_plan"
            tipo_plan = data[2]

            # Si el id del cliente está en el diccionario de clientes
            if id_cliente in clientes:

                # Almacena el nombre del cliente correspondiente al id del cliente en una variable llamada "nombre_cliente"
                nombre_cliente = clientes[id_cliente]

                # Escribe una nueva línea en el archivo "telefonos.txt" que contenga el número de teléfono, el id del cliente, el nombre del cliente y el tipo de plan
                archivo.write(
                    f"{telefono}:{id_cliente}:{nombre_cliente}:{tipo_plan}\n")

            # Si el id del cliente no está en el diccionario de clientes
            else:

                # Imprime un mensaje de error que indica que el cliente no se encontró
                print(f"Error: no se encontró el cliente con ID {id_cliente}")

        # Trunca el archivo a la posición actual del cursor (es decir, elimina todo el contenido después de la última línea escrita)

        archivo.truncate()


modificar_telefonos()
