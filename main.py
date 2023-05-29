from primer_parcial import *

# Mostrar menú de opciones
def main():

    while True:
        print("Menú de opciones:")
        print("1. Mostrar la lista de todos los jugadores del Dream Team")
        print("2. Seleccionar un jugador y mostrar su estadistica")
        print("3. Exportar a csv el ejercicio #2")
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
                imprimir_dato(listar_jugadores_dream_team(lista_jugadores))
                
            case 2:
                imprimir_dato(mostrar_informacion_del_jugador(lista_jugadores))
                
            case 3:
                contenido = guardar_ejercicio_2(lista_jugadores)
                rutacsv = "ejercicio2guardadofinal.csv"
                
                guardar_archivo(rutacsv, contenido)
            
            case 4:
                imprimir_dato(mostrar_logros_del_jugador(lista_jugadores, True))
                
            case 5:
                imprimir_dato(promedio_sub_clave(lista_jugadores, "promedio_puntos_por_partido"))
                imprimir_dato(lista_jugadores_alfabeticamente(lista_jugadores, "nombre"))
                
            case 6:
                imprimir_dato(mostrar_logros_del_jugador(lista_jugadores, False))
                
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
                pass
                
            case 23:
                pass
            
            case _:
                print("EROR el numero no esta en la lista")
            
        clear_console()
            
rutaJSON = 'dt.json'

lista_jugadores = leer_archivo(rutaJSON)

main()