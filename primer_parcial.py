'''
Alumno: Valverde, Cristian Jorge
Division: H
Tutor: Villegas, Octavio.
'''

import re
import json
import os

def clear_console()-> None:
    """
    Esta función borra la pantalla de la consola en Python esperando la entrada del usuario y luego
    llamando al comando 'cls' para borrar la pantalla.
    
    
    
    
    """
    _ = input('Press a key to continue...')
    os.system('cls')

def imprimir_dato(dato):
    print(dato)

def leer_archivo(ruta:str):
    """
    Esta función lee un archivo JSON y devuelve un diccionario de jugadores.
    """
    with open(ruta, 'r', encoding='utf-8') as archivo:
        diccionario_heroes = json.load(archivo)
    return diccionario_heroes["jugadores"]

def mostrar_lista_jugadores(jugadores:list):
    """
    La función toma una lista de diccionarios que contienen información de los jugadores y devuelve una
    cadena con los nombres de los jugadores separados por un carácter de nueva línea.
    """
    lista_jugadores = list()
    
    for jugador in jugadores:
        lista_jugadores.append(jugador["nombre"])
    
    return "\n".join(lista_jugadores)
        
def ordenar_lista(lista_original:list, flag_orden=True)->list:
    lista_izquierda = list()
    lista_derecha = list()
    
    if len(lista_original) <= 1:
        return lista_original
    else:
        pivot = lista_original[0]

        for elemento in lista_original[1:]:
            if flag_orden:
                if elemento > pivot:
                    lista_derecha.append(elemento)
                else:
                    lista_izquierda.append(elemento)
            else:
                if elemento < pivot:
                    lista_derecha.append(elemento)
                else:
                    lista_izquierda.append(elemento)

    lista_izquierda = ordenar_lista(lista_izquierda, flag_orden)
    lista_izquierda.append(pivot)
    lista_derecha = ordenar_lista(lista_derecha, flag_orden)
    lista_izquierda.extend(lista_derecha)
    
    return lista_izquierda
# --------------------------------------------------------------------------------
#1
def listar_jugadores_dream_team(jugadores:list)-> str:
    """
    La función toma una lista de jugadores y devuelve una cadena formateada con sus nombres y
    posiciones.
    
    Parametro:
        jugadores: lista de jugadores
        
    Retorna:
        str: una cadena formateada con sus nombres y posiciones
    """
    if jugadores:
        datos_del_jugador = ""
        for jugador in jugadores:
            datos_del_jugador += "Nombre: {0} - Posicion: {1}\n".format(jugador["nombre"], jugador["posicion"])
        return datos_del_jugador
    
    else:
        "Lista vacia"

#2
def mostrar_informacion_del_jugador(jugadores:list)-> list:
    """
    La función muestra una lista de jugadores y sus índices, solicita al usuario que seleccione un
    jugador por índice y devuelve las estadísticas del jugador.
    
    Parametros:
        jugadores: lista de jugadores
        
    Retorna:
        list: una lista de estadísticas para un jugador seleccionado de una lista de jugadores. Si la
        lista de entrada está vacía, devuelve una cadena que indica que la lista está vacía.
    """
    if jugadores:
        indice = 0
        estadisticas = list()
        
        for jugador in jugadores:
            cadena = "{0} - {1}".format(indice, jugador["nombre"])
            print(cadena)
            indice += 1

        while True:
            indice_ingresado = input("Ingrese el índice del 0 al 11 para mostrar la información del jugador: ")
            if re.match(r'[0-9]|1[0-1]', indice_ingresado):
                indice_ingresado = int(indice_ingresado)
                if indice_ingresado <= len(jugadores):
                    estadisticas.append(jugadores[indice_ingresado]["estadisticas"])
                    break
                else:
                    print("El número ingresado está fuera del rango esperado.")
            else:
                print("Entrada no válida. Debe ingresar un número del 0 al 11.")

        return estadisticas

    else:
        return "Lista vacía"

# 3
def guardar_archivo(ruta:str, contenido:str)-> bool:
    """
    La función "guardar_archivo" crea un archivo con la ruta dada y escribe en él el contenido dado,
    devolviendo True si tiene éxito y False en caso contrario.
    """
    with open(ruta, "w+") as archivo:
        archivo_creado = archivo.write(contenido)
        if archivo_creado:
            print("Se creó el archivo: {0}".format(ruta))
            return True
        else:
            print("Error al crear el archivo: {0}".format(ruta))
            return False

def guardar_ejercicio_2(jugadores:list)->str:
    lista_claves = list()
    lista_valores = list()
    
    lista_informacion = mostrar_informacion_del_jugador(jugadores)
    # es 1 elemento solo = diccionario
    for elemento in lista_informacion:
        for clave, valor in elemento.items():
            lista_claves.append(clave)
            lista_valores.append(str(valor))
            
    join_claves = ",".join(lista_claves)
    join_valores = ",".join(lista_valores)
    
    mostrar = "{0}\n{1}".format(join_claves,join_valores)
    
    return mostrar
            

# 4, 6
def mostrar_logros_del_jugador(jugadores:list)->str:
    """
    Esta función toma una lista de jugadores y solicita al usuario que ingrese el nombre de un jugador,
    luego devuelve los logros de ese jugador.
    
    Parametro:
        jugadores: lista de jugadores
        
    Retorna:
        str: una cadena formateada con los logros de ese jugador.
    """
    if jugadores:
        mostrar_lista = mostrar_lista_jugadores(jugadores)
        print(mostrar_lista)
        
        nombre_ingresado = input("Ingrese el nombre del jugador que aparece en la lista: ")
        nombre_ingresado = nombre_ingresado.title()
        
        if re.search(r'[A-Za-z ]+', nombre_ingresado):
            for jugador in jugadores:
                if nombre_ingresado in jugador["nombre"]:
                    logros = jugador["logros"]

        return "\n".join(logros)
    
    else:
        return "Lista vacia"

# 5
def promedio_sub_clave(jugadores:list[dict],sub_clave:str)->float:
    """
    Esta función calcula el promedio de una sub clave que se debe encontrar en la lista de jugadores y devuelve el
    resultado.
    
    Parametro:
        jugadores: lista de jugadores
        sub_clave: espacio utilizado para cualquier clave que esta dentro de "estadisticas"
        
    Retorna:
        float: el promedio segun indicado en el segundo parametro de la funcion
    """
    if jugadores:
        acumulador = 0
        contador = 0
    
        for jugador in jugadores:
            acumulador += jugador["estadisticas"][sub_clave]
            contador +=1
        
        if contador > 0:
            promedio = acumulador / contador
        else:
            return "No se encontro la sub clave"
        
        return promedio
    
    else:
        return "Lista vacia"

def lista_jugadores_alfabeticamente(jugadores:list)->list:
    """
    Esta función toma una lista de diccionarios que contienen información de jugadores y devuelve una
    lista de nombres de jugadores ordenados alfabéticamente.
    
    Parametro:
        jugadores: lista de jugadores
        
    Retorna:
        list: lista de nombres de jugadores ordenados alfabéticamente
    """
    if jugadores:
        lista_nombres = list()
        
        for jugador in jugadores:
            lista_nombres.append(jugador["nombre"])
        
        nombres_ordenados = ordenar_lista(lista_nombres, True)
        
        return nombres_ordenados
    
    else:
        return "Lista vacia"

# 7, 8 y 9, 13, 14, 19
def jugador_con_mayor_cantidad_de_sub_clave(jugadores:list, sub_clave:str)->str:
    """
    Calcula y muestra el jugador con la mayor cantidad de rebotes totales.

    Parametros:
        jugadores: lista de jugadores
        sub_clave: corresponde a una clave que se encuentre dentro de "estadisticas"

    Retorna:
        str: Una cadena que indica el nombre del jugador con la mayor cantidad de algo segun la "sub_clave" ingresada y su cantidad correspondiente.
    """
    if jugadores:
        sub_clave_refaccionada = sub_clave.replace("_", " ")
        maxima_cantidad = 0
        nombre_jugador = None
        
        for jugador in jugadores:
            cantidad_sub_clave = jugador["estadisticas"][sub_clave]
            if cantidad_sub_clave > maxima_cantidad:
                maxima_cantidad = cantidad_sub_clave
                nombre_jugador = jugador["nombre"]
        
        if nombre_jugador != None:
            mensaje = "El jugador con la mayor cantidad de {0} es {1} con {2}".format(sub_clave_refaccionada,nombre_jugador, maxima_cantidad)
        else:
            mensaje = "No se encontró ningún jugador con la estadística solicitada"
        
        return mensaje
    
    else:
        return "Lista vacia"
        
# 10, 11, 12, 15, 18
def listar_jugadores_mayor_al_promedio(jugadores:list, sub_clave:str)->list:
    """
    Esta función toma una lista de jugadores y una subclave como entrada, solicita al usuario un valor y
    devuelve una lista de jugadores cuyas estadísticas para la subclave dada son mayores que el valor
    ingresado por el usuario.
    
    Parametros:
        jugadores: lista de jugadores
        sub_clave: corresponde a una clave que se encuentre dentro de "estadisticas"
        
    Retorna:
        list: lista de jugadores cuyas estadísticas para la subclave dada son mayores que el valor
        ingresado por el usuario
    """
    if jugadores:
        lista_jugadores_mayor = list()
        
        valor_ingresado = input("Ingrese un valor: ")
        if re.match(r'[0-9]|1[0-1]', valor_ingresado):
            valor_ingresado = int(valor_ingresado)

        for jugador in jugadores:
            if jugador["estadisticas"][sub_clave] > valor_ingresado:
                lista_jugadores_mayor.append(jugador["nombre"])

        return lista_jugadores_mayor
    
    else:
        return "Lista vacia"

# 16
def promedio_excluyendo_al_menor_cantidad_puntos_por_partido(jugadores:list):
    """
    Esta función calcula el promedio de puntos por juego para una lista de jugadores, excluyendo al
    jugador con el promedio más bajo.
    """
    if jugadores:
        lista_promedio_de_puntos = list()
        for jugador in jugadores:
            lista_promedio_de_puntos.append(jugador["estadisticas"]["promedio_puntos_por_partido"])
            
        lista_promedio_de_puntos_ordenada = ordenar_lista(lista_promedio_de_puntos, True)
        # print(lista_promedio_de_puntos_ordenada[0]) #elemento eliminado
        
        lista_promedio_de_puntos_ordenada.remove(lista_promedio_de_puntos_ordenada[0])
        # print(lista_promedio_de_puntos_ordenada) #lista sin el elemento eliminado
        
        if lista_promedio_de_puntos_ordenada:
            suma = sum(lista_promedio_de_puntos_ordenada)
            promedio = suma / len(lista_promedio_de_puntos_ordenada)
            
        return promedio #20.99
    
    else:
        return "Lista vacia"
    

# 17
def jugador_con_mayor_cantidad_logros(jugadores:list)->str:
    """
    Esta función devuelve el nombre del jugador con el mayor número de logros obtenidos.
    """
    if jugadores:
        for i in range(len(jugadores)):
            if i == 0 or len(jugadores[i]["logros"]) > len(jugador_max):
                jugador_max = jugadores[i]["logros"]
                i_max = i
                
        jugador_retornado = jugadores[i_max]["nombre"]
        mensaje_retorno = "el jugador con el mayor número de logros obtenidos es {0}".format(jugador_retornado)
        return mensaje_retorno
    
    else:
        return "Lista vacia"

# 20
def jugadores_ordenados_por_posicion_e_ingreso_del_usuario(jugadores:list):
    if jugadores:
        return jugadores
    
    else:
        return "Lista Vacia"



# Mostrar menú de opciones
def main():

    while True:
        print("Menú de opciones:")
        print("1. Mostrar la lista de todos los jugadores del Dream Team")
        print("2. Seleccionar un jugador y mostrar su estadistica")
        print("3. ")
        print("4. Ingresar el nombre del jugador para ver sus logros")
        print("5. Promedio de puntos por partido del Dream Team")
        print("6. Mostrar si el jugador ingresado es miembro del salon de la fama")
        print("7. Mostrar el jugador con la mayor cantidad de rebotes totales")
        print("8. Mostrar el jugador con el mayor porcentaje de tiros de campo")
        print("9. Mostrar el jugador con la mayor cantidad de asistencias totales")
        print("10. Listar jugadores mayor al promedio ingresado de 'mas puntos por partido'")
        print("11. Listar jugadores mayor al promedio ingresado de 'mas rebotes por partido'")
        print("12. Listar jugadores mayor al promedio ingresado de 'mas asistencias por partido'")
        print("13. Mostrar jugador con la mayor cantidad de robos totales")
        print("14. Mostrar jugador con la mayor cantidad de bloqueos totales")
        print("15. Listar jugadores mayor al promedio ingresado de 'porcentaje de tiros libres'")
        print("16. Mostrar el promedio de puntos por partido, excluyendo al menor")
        print("17. Mostrar el jugador con la mayor cantidad de logros obtenidos")
        print("18. Listar jugadores mayor al promedio ingresado de 'porcentaje de tiros triples'")
        print("19. Mostrar jugador con la mayor cantidad de temporadas jugadas")
        print("20. Jugadores ordenados por posicion en la cancha, con mayor porcentaje de tiros de campo superior al numero ingresado por el usuario")
        print("23. BONUS")
        

        opcion = input("\nIngrese la opción deseada: ")
        if re.match('[0-9]|1[0-9]|20|23', opcion):
            opcion = int(opcion)
        match opcion:
            
            case 1:
                lista = listar_jugadores_dream_team(lista_jugadores)
                imprimir_dato(lista)
                
            case 2:
                resultdo = mostrar_informacion_del_jugador(lista_jugadores)
                imprimir_dato(resultdo)
                
            case 3:
                contenido = guardar_ejercicio_2(lista_jugadores)
                rutacsv = "ejercicio2guardadofinal.csv"
                
                guardar_archivo(rutacsv, contenido)
            
            case 4:
                imprimir_dato(mostrar_logros_del_jugador(lista_jugadores))
                
            case 5:
                imprimir_dato(promedio_sub_clave(lista_jugadores, "promedio_puntos_por_partido"))
                imprimir_dato(lista_jugadores_alfabeticamente(lista_jugadores))
                
            case 6:
                logros = mostrar_logros_del_jugador(lista_jugadores)
                if "Miembro del Salon de la Fama del Baloncesto" == logros:
                    imprimir_dato("El jugador es 'Miembro del Salon de la Fama del Baloncesto'")
                else:
                    imprimir_dato("El jugador no es 'Miembro del Salon de la Fama del Baloncesto'")
                
            case 7:
                imprimir_dato(jugador_con_mayor_cantidad_de_sub_clave(lista_jugadores, "rebotes_totales"))
            
            case 8:
                imprimir_dato(jugador_con_mayor_cantidad_de_sub_clave(lista_jugadores, "porcentaje_tiros_de_campo"))
            
            case 9:
                imprimir_dato(jugador_con_mayor_cantidad_de_sub_clave(lista_jugadores, "asistencias_totales"))
                
            case 10:
                imprimir_dato(listar_jugadores_mayor_al_promedio(lista_jugadores, "promedio_puntos_por_partido"))
                
            case 11:
                imprimir_dato(listar_jugadores_mayor_al_promedio(lista_jugadores, "promedio_rebotes_por_partido"))
                
            case 12:
                imprimir_dato(listar_jugadores_mayor_al_promedio(lista_jugadores, "promedio_asistencias_por_partido"))
                
            case 13:
                imprimir_dato(jugador_con_mayor_cantidad_de_sub_clave(lista_jugadores, "robos_totales"))

            case 14:
                imprimir_dato(jugador_con_mayor_cantidad_de_sub_clave(lista_jugadores, "bloqueos_totales"))

            case 15:
                imprimir_dato(listar_jugadores_mayor_al_promedio(lista_jugadores, "porcentaje_tiros_libres"))
            
            case 16:
                imprimir_dato(promedio_excluyendo_al_menor_cantidad_puntos_por_partido(lista_jugadores))
            
            case 17:
                imprimir_dato(jugador_con_mayor_cantidad_logros(lista_jugadores))
            
            case 18:
                imprimir_dato(listar_jugadores_mayor_al_promedio(lista_jugadores, "porcentaje_tiros_triples"))
                
            case 19:
                imprimir_dato(jugador_con_mayor_cantidad_de_sub_clave(lista_jugadores, "temporadas"))
            
            case 20:
                imprimir_dato(jugadores_ordenados_por_posicion_e_ingreso_del_usuario(lista_jugadores))
                
            case 23:
                pass
            
        clear_console()
            
rutaJSON = 'dt.json'

lista_jugadores = leer_archivo(rutaJSON)

main()