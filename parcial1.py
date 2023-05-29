"""
Joaquin Casasola / parcial_1
1E
"""
import re
import json

def lee_json(ruta: str) -> list:
    """
    - Lee archivo json\n
    <-Recibe una ruta de archivo str\n
    ->Retorna una lista
    """
    with open(ruta, 'r', encoding = "utf-8") as archivo:
        dato = json.load(archivo)
    return dato["jugadores"]


def buscar_jugador_por_nombre(string:str)->str:
    """
    - Buscar un jugador por su nombre\n
    <-Recibe un string\n
    ->Retorna un string 
    """
    if(re.search(r"^[M-m]ic.+|[J-j]ord.+$", string) != None):
        string = "Michael Jordan"

    elif(re.search(r"^[M-m]ag.+|[J-j]ohn.+$", string) != None):
        string = "Magic Johnson"

    elif(re.search(r"^[L-l]ar.+|[B-b]ird.+$", string) != None):
        string = "Larry Bird"

    elif(re.search(r"^[C-c]harl.+|[B-b]ark.+$", string) != None):
        string = "Charles Barkley"

    elif(re.search(r"^[S-s]cot.+|[P-p]ip.+$", string) != None):
        string = "Scottie Pippen"

    elif(re.search(r"^[D-d]av.+|[R-r]ob.+$", string) != None):
        string = "David Robinson"

    elif(re.search(r"^[P-p]at.+|[E-e]wi.+$", string) != None):
        string = "Patrick Ewing"

    elif(re.search(r"^[K-k]ar.+|[M-m]al.+$", string) != None):
        string = "Karl Malone"

    elif(re.search(r"^[J-j]oh.+|[S-s]to.+$", string) != None):
        string = "John Stockton"

    elif(re.search(r"^[C-c]ly.+|[D-d]re.+$", string) != None):
        string = "Clyde Drexler"
    
    elif(re.search(r"^[C-c]hrist.+|[L-l]aet.+$", string) != None):
        string = "Christian Laettner"

    elif(re.search(r"^[C-c]hr.+|[M-m]ul.+$", string) != None):
        string = "Chris Mullin"

    else:
        string = "[ERROR]: No se a podido encontra ese jugador"
    
    return string


#1
"""
Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
Nombre Jugador - Posición. Ejemplo:
Michael Jordan - Escolta
"""
def muestra_lista_jugadores(lista:list)-> str:
    """
    - Muestra el nombre y la posicion de todos los jugadores\n
    <-Recibe una lista\n
    ->Retorna un mensaje 
    """
    mensaje = ""
    for jugador in lista:
        nombre_jugador = jugador["nombre"]
        posicion = jugador["posicion"]
        mensaje += "----------------\n{0} - {1}\n".format(nombre_jugador, posicion)
    return mensaje


#2
"""
Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas, incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
"""
lista_indice = []
def muestra_estadisticas_por_indice(lista:list, indice:int)-> str:
    """
    - Muestra las estadisticas del jugador con el indice elegido\n
    <-Recibe una lista y un indice\n
    ->Retorna un mensaje 
    """
    lista_indice.append(indice)
    for i in range(len(lista)):
        if(i == indice):
            nombre = lista[i]["nombre"]
    estadistica = ""
    for clave,valor in lista[indice]["estadisticas"].items():
        clave = clave.replace("_"," ")
        estadistica += "----------------\n{0}: {1}\n".format(clave, valor)
    mensaje = "\nLas estadisticas de {0}:\n{1}".format(nombre, estadistica)
    return mensaje


#3
"""
Después de mostrar las estadísticas de un jugador seleccionado por el usuario, permite al usuario guardar las estadísticas de ese jugador en un archivo CSV. El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas, 
"""
def guarda_CSV_estadisticas(lista:list,indice:int):
    """
    + Guarda archivo CSV del las estadisticas del anterior jugador elegido\n
    <-Recibe un string\n 
    ->Devuelve el archivo CSV
    """
    mensaje = ""
    for clave,valor in lista[indice]["estadisticas"].items():
        clave = clave.replace("_"," ")
        mensaje += "{0},{1}\n".format(clave, valor)
    nombre = Lista_dreamteam[indice]["nombre"].replace(" ","_")
    with open("estadisticas_{0}.csv".format(nombre), "w") as archivo:
        archivo.writelines(mensaje)


#4
"""
Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.
"""
def muestra_logros_segun_nombre(lista:list, nombre:str)-> str:
    """
    - Muestra los logros del jugador elegido\n
    <-Recibe una lista y un nombre\n
    ->Retorna un mensaje 
    """
    nombre_jugador = buscar_jugador_por_nombre(nombre)
    if(re.search(r"[ERROR].+",nombre_jugador) != None):
        return nombre_jugador
    else:
        logros = ""
        for jugador in lista:
            if(jugador["nombre"] == nombre_jugador):
                logros += (("\n").join(jugador["logros"]))
        mensaje = "\nLos logros de {0} son: \n{1}".format(nombre_jugador,logros)
        return mensaje 


#5
"""
Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente. 
"""
def muestra_promedio_puntos_por_partido(lista:list)-> str:
    """
    - Muestra el promedio de puntos por partido del equipo\n
    <-Recibe una lista\n
    ->Retorna un mensaje 
    """
    Lista_promedios = []
    rango = len(lista)
    suma_promedios = 0
    for jugador in lista:
        Lista_promedios.append("\n{0} - {1}".format(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"]))
        suma_promedios += jugador["estadisticas"]["promedio_puntos_por_partido"]
    
    promedios = ""
    Flag = True
    while(Flag):
        Flag = False
        for i in range(rango-1):
            if(Lista_promedios[i][1] > Lista_promedios[i+1][1]):
                Lista_promedios[i],Lista_promedios[i+1] = Lista_promedios[i+1],Lista_promedios[i]
                Flag = True
    for promedio in Lista_promedios:
        promedios += promedio

    promedio_general = suma_promedios/rango
    promedio_general = "-----------------------\nPromedio del equipo: {0:.2f}".format(promedio_general)
    mensaje = "{0}\n{1}".format(promedios,promedio_general)
    return mensaje


#6
"""
Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.
"""
def muestra_salon_fama(lista:list, nombre:str)-> str:
    """
    - Muestra si el jugador elegido es miembro del Salón de la Fama\n
    <-Recibe una lista y un nombre\n
    ->Retorna un mensaje 
    """
    patron = r"Baloncesto$"
    nombre = buscar_jugador_por_nombre(nombre)
    if(re.search(r"[ERROR].+",nombre) != None):
        return nombre
    else:
        Es_salon_de_fama = ""
        for jugador in lista:
            if(jugador["nombre"] == nombre):
                if(re.search(patron, jugador["logros"][-1])):
                    Es_salon_de_fama = "si es miembro del Salón de la Fama"
                else:
                    Es_salon_de_fama = "es miembro del Salón de la Fama Universitario"
        mensaje = "\n{0} {1}".format(nombre, Es_salon_de_fama)
        return mensaje


#7
"""
Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
"""
def muestra_jugador_con_mayor_rebotes(lista:list)-> str:
    """
    - Muestra el jugador con la mayor cantidad de rebotes totales\n
    <-Recibe una lista\n
    ->Retorna un mensaje 
    """
    jugador_con_mayor_rebotes = None
    for jugador in lista:
        if(jugador_con_mayor_rebotes == None or jugador["estadisticas"]["rebotes_totales"] > jugador_con_mayor_rebotes["estadisticas"]["rebotes_totales"]):
            jugador_con_mayor_rebotes = jugador
    mensaje = "\n- El jugador con mas rebotes es {0}, con {1} rebotes".format(jugador_con_mayor_rebotes["nombre"], jugador_con_mayor_rebotes["estadisticas"]["rebotes_totales"])
    return mensaje


#8
"""
Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
"""
def muestra_jugador_con_mayor_tiros_campo(lista:list)-> str:
    """
    - Muestra el jugador con el mayor porcentaje de tiros de campo\n
    <-Recibe una lista\n
    ->Retorna un mensaje 
    """
    jugador_con_mayor_tiros_campo = None
    for jugador in lista:
        if(jugador_con_mayor_tiros_campo == None or jugador["estadisticas"]["porcentaje_tiros_de_campo"] > jugador_con_mayor_tiros_campo["estadisticas"]["porcentaje_tiros_de_campo"]):
            jugador_con_mayor_tiros_campo = jugador
    mensaje = "\n- El jugador con mas porcentaje de tiros de campo es {0}, con un {1}% de tiros".format(jugador_con_mayor_tiros_campo["nombre"], jugador_con_mayor_tiros_campo["estadisticas"]["porcentaje_tiros_de_campo"])
    return mensaje


#9
"""
Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
"""
def muestra_jugador_con_mayor_asistencias(lista:list)-> str:
    """
    - Muestra el jugador con la mayor cantidad de asistencias totales\n
    <-Recibe una lista\n
    ->Retorna un mensaje 
    """
    jugador_con_mayor_tiros_campo = None
    for jugador in lista:
        if(jugador_con_mayor_tiros_campo == None or jugador["estadisticas"]["asistencias_totales"] > jugador_con_mayor_tiros_campo["estadisticas"]["asistencias_totales"]):
            jugador_con_mayor_tiros_campo = jugador
    mensaje = "\n- El jugador con mas asistencias es {0}, con {1} asistencias".format(jugador_con_mayor_tiros_campo["nombre"], jugador_con_mayor_tiros_campo["estadisticas"]["asistencias_totales"])
    return mensaje


#10
"""
Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.
"""
def muestra_jugadores_promedio_puntos_por_partido(lista:list, valor:int)-> str:
    """
    - Muestra los jugadores que han promediado más puntos por partido que el valor ingresado\n
    <-Recibe una lista y un valor\n
    ->Retorna un mensaje 
    """
    Lista_promedios_mayores = []
    for jugador in lista:
        if(jugador["estadisticas"]["promedio_puntos_por_partido"] > valor):
            promedio_puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]
            Lista_promedios_mayores.append("-----------\n{0} - {1} pts\n-----------".format(jugador["nombre"], promedio_puntos))

    mensaje = ""
    for promedio in Lista_promedios_mayores:
        mensaje += promedio        
    return mensaje


#11
"""
Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.
"""
def muestra_jugadores_promedio_rebotes_por_partido(lista:list, valor:int)-> str:
    """
    - Muestra los jugadores que han promediado más rebotes por partido que el valor ingresado\n
    <-Recibe una lista y un valor\n
    ->Retorna un mensaje 
    """
    Lista_promedios_mayores = []
    for jugador in lista:
        if(jugador["estadisticas"]["promedio_rebotes_por_partido"] > valor):
            promedio_rebotes = jugador["estadisticas"]["promedio_rebotes_por_partido"]
            Lista_promedios_mayores.append("-----------\n{0} - {1} rebotes\n-----------".format(jugador["nombre"], promedio_rebotes))

    mensaje = ""
    for promedio in Lista_promedios_mayores:
        mensaje += promedio        
    return mensaje


#12
"""
Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.
"""
def muestra_jugadores_promedio_asistencias_por_partido(lista:list, valor:int)-> str:
    """
    - Muestra los jugadores que han promediado más asistencias por partido que el valor ingresado\n
    <-Recibe una lista y un valor\n
    ->Retorna un mensaje 
    """
    Lista_promedios_mayores = []
    for jugador in lista:
        if(jugador["estadisticas"]["promedio_asistencias_por_partido"] > valor):
            promedio_asistencias = jugador["estadisticas"]["promedio_asistencias_por_partido"]
            Lista_promedios_mayores.append("-----------\n{0} - {1} asistencias\n-----------".format(jugador["nombre"], promedio_asistencias))

    mensaje = ""
    for promedio in Lista_promedios_mayores:
        mensaje += promedio        
    return mensaje


#13
"""
Calcular y mostrar el jugador con la mayor cantidad de robos totales.
"""
def muestra_jugador_con_mayor_robos(lista:list)-> str:
    """
    - Muestra el jugador con la mayor cantidad de robos totales\n
    <-Recibe una lista\n
    ->Retorna un mensaje 
    """
    jugador_con_mayores_robos = None
    for jugador in lista:
        if(jugador_con_mayores_robos == None or jugador["estadisticas"]["robos_totales"] > jugador_con_mayores_robos["estadisticas"]["robos_totales"]):
            jugador_con_mayores_robos = jugador
    mensaje = "\n- El jugador con mas robos es {0}, con {1} robos".format(jugador_con_mayores_robos["nombre"], jugador_con_mayores_robos["estadisticas"]["robos_totales"])
    return mensaje


#14
"""
Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.
"""
def muestra_jugador_con_mayor_bloqueos(lista:list)-> str:
    """
    - Muestra el jugador con la mayor cantidad de bloqueos totales\n
    <-Recibe una lista\n
    ->Retorna un mensaje 
    """
    jugador_con_mayores_bloqueos = None
    for jugador in lista:
        if(jugador_con_mayores_bloqueos == None or jugador["estadisticas"]["bloqueos_totales"] > jugador_con_mayores_bloqueos["estadisticas"]["bloqueos_totales"]):
            jugador_con_mayores_bloqueos = jugador
    mensaje = "\n- El jugador con mas bloqueos es {0}, con {1} bloqueos".format(jugador_con_mayores_bloqueos["nombre"], jugador_con_mayores_bloqueos["estadisticas"]["bloqueos_totales"])
    return mensaje


#15
"""
Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.
"""
def muestra_jugadores_porcentaje_tiros_libres(lista:list, valor:int)-> str:
    """
    - Muestra los jugadores que hayan tenido un porcentaje de tiros libres superior a el valor ingresado\n
    <-Recibe una lista y un valor\n
    ->Retorna un mensaje 
    """
    Lista_porcentajes_mayores = []
    for jugador in lista:
        if(jugador["estadisticas"]["porcentaje_tiros_libres"] > valor):
            porcentaje_tiros_libres = jugador["estadisticas"]["porcentaje_tiros_libres"]
            Lista_porcentajes_mayores.append("-----------\n{0} - {1}%\n-----------".format(jugador["nombre"], porcentaje_tiros_libres))

    mensaje = ""
    for promedio in Lista_porcentajes_mayores:
        mensaje += promedio        
    return mensaje


#16
"""
Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.
"""
def muestra_promedio_puntos_por_partido_excluyendo_menor_puntos(lista:list)-> str:
    """
    - Calcula el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido\n
    <-Recibe una lista\n
    ->Retorna un mensaje 
    """
    cantidad = len(lista)
    suma_promedios = 0
    for jugador in lista:
        suma_promedios += jugador["estadisticas"]["promedio_puntos_por_partido"]
    promedio_total_equipo = suma_promedios/cantidad
    jugador_con_menor_puntos = None
    for jugador in lista:
        if(jugador_con_menor_puntos == None or jugador["estadisticas"]["promedio_puntos_por_partido"] < jugador_con_menor_puntos["estadisticas"]["promedio_puntos_por_partido"]):
            jugador_con_menor_puntos = jugador
    menos_puntos = jugador_con_menor_puntos["estadisticas"]["promedio_puntos_por_partido"]

    promedio_del_equipo_sin_el_menor = promedio_total_equipo - menos_puntos
    mensaje = "\n- El promedio de puntos por partido del equipo sin {0} (con {1:.1f} pts) es: {2:.2f} pts".format(jugador_con_menor_puntos["nombre"],jugador_con_menor_puntos["estadisticas"]["promedio_puntos_por_partido"],promedio_del_equipo_sin_el_menor)
    return mensaje


#17
"""
Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
"""
def muestra_jugador_con_mayor_logros(lista:list)-> str:
    """
    - Muestra el jugador con la mayor cantidad de logros obtenidos\n
    <-Recibe una lista\n
    ->Retorna un mensaje 
    """
    jugador_con_mas_logros = None
    for jugador in lista:
        if(jugador_con_mas_logros == None or len(jugador["logros"]) > len(jugador_con_mas_logros["logros"])):
            jugador_con_mas_logros = jugador
    logros = "\n"
    for logro in jugador_con_mas_logros["logros"]:
        logros += "- {0}\n".format(logro)
    mensaje = "\n- El jugador con mas logros obtenidos es {0}, con {1} logros:\n {2}".format(jugador_con_mas_logros["nombre"], len(jugador_con_mas_logros["logros"]), logros)
    return mensaje


#18
"""
Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.
"""
def muestra_jugadores_porcentaje_tiros_triples(lista:list, valor:int)-> str:
    """
    - Muestra los jugadores que hayan tenido un porcentaje de tiros triples superior a el valor ingresado\n
    <-Recibe una lista y un valor\n
    ->Retorna un mensaje 
    """
    Lista_porcentajes_mayores = []
    for jugador in lista:
        if(jugador["estadisticas"]["porcentaje_tiros_triples"] > valor):
            porcentaje_tiros_triples = jugador["estadisticas"]["porcentaje_tiros_triples"]
            Lista_porcentajes_mayores.append("-----------\n{0} - {1}%\n-----------".format(jugador["nombre"], porcentaje_tiros_triples))
    
    mensaje = ""
    for porcentaje in Lista_porcentajes_mayores:
        mensaje += porcentaje        
    return mensaje


#19
"""
Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
"""
def muestra_jugador_con_mayor_temporadas_jugadas(lista:list)-> str:
    """
    - Muestra el jugador con la mayor cantidad de temporadas jugadas\n
    <-Recibe una lista\n
    ->Retorna un mensaje 
    """
    jugador_con_mas_temporadas = None
    for jugador in lista:
        if(jugador_con_mas_temporadas == None or jugador["estadisticas"]["temporadas"] > jugador_con_mas_temporadas["estadisticas"]["temporadas"]):
            jugador_con_mas_temporadas = jugador
        

    mensaje = "\n- El jugador con mas temporadas es {0}, con {1} temporadas".format(jugador_con_mas_temporadas["nombre"], jugador_con_mas_temporadas["estadisticas"]["temporadas"])
    return mensaje


#20
"""
Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.
"""
def muestra_jugadores_porcentaje_tiros_campo(lista:list, valor:int)-> str:
    """
    - Muestra los jugadores que hayan tenido un porcentaje de tiros de campo superior a el valor ingresado\n
    <-Recibe una lista y un valor\n
    ->Retorna un mensaje 
    """
    Lista_jugador_porcentajes_mayores = []
    for jugador in lista:
        if(jugador["estadisticas"]["porcentaje_tiros_de_campo"] > valor):
            Lista_jugador_porcentajes_mayores.append(jugador)

    rango = len(Lista_jugador_porcentajes_mayores)
    Flag = True
    while(Flag):
        Flag = False
        for i in range(rango-1):
            if(Lista_jugador_porcentajes_mayores[i]["posicion"][0] > Lista_jugador_porcentajes_mayores[i+1]["posicion"][0]):
                Lista_jugador_porcentajes_mayores[i],Lista_jugador_porcentajes_mayores[i+1] = Lista_jugador_porcentajes_mayores[i+1],Lista_jugador_porcentajes_mayores[i]
                Flag = True

    mensaje = ""
    for jugador in Lista_jugador_porcentajes_mayores:
        mensaje += "({0}) {1} - {2}%\n".format(jugador["posicion"],jugador["nombre"],jugador["estadisticas"]["porcentaje_tiros_de_campo"])
    return mensaje


#23
"""
Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking
Puntos, Rebotes, Asistencias, Robos
Exportar a csv.
"""
def muestra_posicion_en_ranking(lista:list)-> str:
    """
    - Muestra la posición en cada uno de los rankings\n
    <-Recibe una lista\n
    ->Retorna un mensaje 
    """
    Lista_ordenada_por_puntos = lista[:]
    Lista_ordenada_por_rebotes = lista[:]
    Lista_ordenada_por_asistencias = lista[:]
    Lista_ordenada_por_robos = lista[:]

    # Ordeno por puntos
    rango = len(lista)
    Flag = True
    while(Flag):
        Flag = False
        for i in range(rango-1):
            if(Lista_ordenada_por_puntos[i]["estadisticas"]["puntos_totales"] < Lista_ordenada_por_puntos[i+1]["estadisticas"]["puntos_totales"]):
                Lista_ordenada_por_puntos[i],Lista_ordenada_por_puntos[i+1] = Lista_ordenada_por_puntos[i+1],Lista_ordenada_por_puntos[i]
                Flag = True

    # Ordeno por rebotes
    Flag = True
    while(Flag):
        Flag = False
        for i in range(rango-1):
            if(Lista_ordenada_por_rebotes[i]["estadisticas"]["rebotes_totales"] < Lista_ordenada_por_rebotes[i+1]["estadisticas"]["rebotes_totales"]):
                Lista_ordenada_por_rebotes[i],Lista_ordenada_por_rebotes[i+1] = Lista_ordenada_por_rebotes[i+1],Lista_ordenada_por_rebotes[i]
                Flag = True

    # Ordeno por asistencias
    Flag = True
    while(Flag):
        Flag = False
        for i in range(rango-1):
            if(Lista_ordenada_por_asistencias[i]["estadisticas"]["asistencias_totales"] < Lista_ordenada_por_asistencias[i+1]["estadisticas"]["asistencias_totales"]):
                Lista_ordenada_por_asistencias[i],Lista_ordenada_por_asistencias[i+1] = Lista_ordenada_por_asistencias[i+1],Lista_ordenada_por_asistencias[i]
                Flag = True

    # Ordeno por robos
    Flag = True
    while(Flag):
        Flag = False
        for i in range(rango-1):
            if(Lista_ordenada_por_robos[i]["estadisticas"]["robos_totales"] < Lista_ordenada_por_robos[i+1]["estadisticas"]["robos_totales"]):
                Lista_ordenada_por_robos[i],Lista_ordenada_por_robos[i+1] = Lista_ordenada_por_robos[i+1],Lista_ordenada_por_robos[i]
                Flag = True
 
    with open("ranking_estadisticas.csv", "w") as archivo:
        titulos = ["nombre","puntos totales","rebotes totales","asistencias totales","robos totales"]
        archivo.write(",".join(titulos))
        archivo.write("\n")

        for jugador in lista:
            nombre = jugador["nombre"]
            posicion_puntos = Lista_ordenada_por_puntos.index(jugador) + 1
            posicion_rebotes = Lista_ordenada_por_rebotes.index(jugador) + 1
            posicion_asistencias = Lista_ordenada_por_asistencias.index(jugador) + 1
            posicion_robos = Lista_ordenada_por_robos.index(jugador) + 1

            linea = "{0},{1},{2},{3},{4}\n".format(nombre, posicion_puntos, posicion_rebotes, posicion_asistencias, posicion_robos)
            archivo.write(linea)

ruta = "C:\\Users\\Admin\\Desktop\\Prog. y Lab. 1\\Primer_parcial.py\\Data_parcial1.json"
Lista_dreamteam = lee_json(ruta)

Flag = True
while Flag:
    print("\nMenú de opciones:")
    print("1. Mostrar el nombre y la posicion de todos los jugadores\n")

    print("2. Mostrar las estadisticas del jugador con un indice elegido\n")

    print("3. Guardar archivo CSV del las estadisticas del anterior jugador elegido\n")

    print("4. Mostrar los logros de un jugador elegido\n")

    print("5. Mostrar el promedio de puntos por partido del equipo\n")

    print("6. Mostrar si un jugador elegido es miembro del Salón de la Fama\n")

    print("7. Mostrar el jugador con la mayor cantidad de rebotes totales\n")

    print("8. Mostrar el jugador con el mayor porcentaje de tiros de campo\n")

    print("9. Mostrar el jugador con la mayor cantidad de asistencias totales\n")

    print("10. Mostrar los jugadores que han promediado más puntos por partido que un valor ingresado\n")

    print("11. Mostrar los jugadores que han promediado más rebotes por partido que el valor ingresado\n")

    print("12. Mostrar los jugadores que han promediado más asistencias por partido que el valor ingresado\n")
    
    print("13. Mostrar el jugador con la mayor cantidad de robos totales\n")

    print("14. Mostrar el jugador con la mayor cantidad de bloqueos totales\n")

    print("15. Mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a el valor ingresado\n")

    print("16. Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido\n")

    print("17. Mostrar el jugador con la mayor cantidad de logros obtenidos\n")

    print("18. Mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a el valor ingresado\n")

    print("19. Mostrar el jugador con la mayor cantidad de temporadas jugadas\n")

    print("20. Mostrar los jugadores que hayan tenido un porcentaje de tiros de campo superior a el valor ingresado\n")

    print("23. Exportar CSV con la posición de los jugadores en cada uno de los rankings (Puntos, Rebotes, Asistencias, Robos)\n")

    print("0. Salir del programa")

    Respuesta_txt = input("\nIngrese la opcion elegida: ")
    patron = r"^[0-9]$|^1[0-9]$|^20$|^23$"
    if(re.match(patron, Respuesta_txt) != None):
        Respuesta_int = int(Respuesta_txt)
    else:
        print("\n[ERROR]: Ingrese un numero (del 0 al 23 exceptuando 21 y 22)\n")
        continue


    match(Respuesta_int):
        case 1:
            print(muestra_lista_jugadores(Lista_dreamteam))
        case 2:
            indice = input("Ingrese el numero de indice de el jugador:")
            patron = r"^[\d]+$"
            if(re.match(patron, indice)!= None and int(indice) <= 11):
                print(muestra_estadisticas_por_indice(Lista_dreamteam, int(indice)))
            else:
                print("\n[ERROR]: Indice invalido (0 a 11)")
        case 3:
            if(len(lista_indice) != 0):
                indice = lista_indice[-1]
                guarda_CSV_estadisticas(Lista_dreamteam, indice)
                print("Archivo exportado con exito!")
            else:
                print("\n[ERROR]: Debe seleccionar el punto previo antes (punto 2)")
        case 4:
            nombre = input("Ingrese el nombre del jugador: ")
            if(nombre.isalpha() != False or " " in nombre):
                print(muestra_logros_segun_nombre(Lista_dreamteam, nombre))
            else:
                print("\n[ERROR]:Solo ingrese letras")
        case 5:
            print(muestra_promedio_puntos_por_partido(Lista_dreamteam))
        case 6:
            nombre = input("Ingrese el nombre del jugador: ")
            if(nombre.isalpha() != False):
                print(muestra_salon_fama(Lista_dreamteam, nombre))
            else:
                print("\n[ERROR]:Solo ingrese letras")
        case 7:
            print(muestra_jugador_con_mayor_rebotes(Lista_dreamteam))

        case 8:
            print(muestra_jugador_con_mayor_tiros_campo(Lista_dreamteam))

        case 9:
            print(muestra_jugador_con_mayor_asistencias(Lista_dreamteam))

        case 10:
            valor = input("Ingrese un valor: ")
            patron = r"^[\d]+$"
            if(re.match(patron, valor)!= None and int(valor) <= 30.1):
                valor = int(valor)
                print("\nPoromedio Puntos por partido:")
                print(muestra_jugadores_promedio_puntos_por_partido(Lista_dreamteam,valor))
            else:
                print("\n[ERROR]: Ingrese un valor numerico valido (menor a 30.1)")

        case 11:
            valor = input("Ingrese un valor: ")
            patron = r"^[\d]+$"
            if(re.match(patron, valor)!= None and int(valor) <= 11.7):
                valor = int(valor)
                print("\nPoromedio Rebotes por partido:")
                print(muestra_jugadores_promedio_rebotes_por_partido(Lista_dreamteam,valor))
            else:
                print("[ERROR]: Ingrese un valor numerico valido (menor a 11.7)")

        case 12:
            valor = input("Ingrese un valor: ")
            patron = r"^[\d]+$"
            if(re.match(patron, valor)!= None and int(valor) <= 11.2):
                valor = int(valor)
                print("\nPoromedio Asistencias por partido:")
                print(muestra_jugadores_promedio_asistencias_por_partido(Lista_dreamteam,valor))
            else:
                print("\n[ERROR]: Ingrese un valor numerico valido (menor a 11.2)")

        case 13:
            print(muestra_jugador_con_mayor_robos(Lista_dreamteam))

        case 14:
            print(muestra_jugador_con_mayor_bloqueos(Lista_dreamteam))

        case 15:
            valor = input("Ingrese un valor: ")
            patron = r"^[\d]+$"
            if(re.match(patron, valor)!= None and int(valor) <= 88.6):
                valor = int(valor)
                print("\nPorcentaje Tiros libres:")
                print(muestra_jugadores_porcentaje_tiros_libres(Lista_dreamteam,valor))
            else:
                print("\n[ERROR]: Ingrese un valor numerico valido (menor a 88.6)")

        case 16:
            print(muestra_promedio_puntos_por_partido_excluyendo_menor_puntos(Lista_dreamteam))

        case 17:
            print(muestra_jugador_con_mayor_logros(Lista_dreamteam))

        case 18:
            valor = input("Ingrese un valor: ")
            patron = r"^[\d]+$"
            if(re.match(patron, valor)!= None and int(valor) <= 48.5):
                valor = int(valor)
                print("\nPorcentaje Tiros triples:")
                print(muestra_jugadores_porcentaje_tiros_triples(Lista_dreamteam,valor))
            else:
                print("\n[ERROR]: Ingrese un valor numerico valido (menor a 48.5)")

        case 19:
            print(muestra_jugador_con_mayor_temporadas_jugadas(Lista_dreamteam))

        case 20:
            valor = input("Ingrese un valor: ")
            patron = r"^[\d]+$"
            if(re.match(patron, valor)!= None and int(valor) <= 54):
                valor = int(valor)
                print("\nPorcentaje Tiros de campo:")
                print(muestra_jugadores_porcentaje_tiros_campo(Lista_dreamteam,valor))
            else:
                print("\n[ERROR]: Ingrese un valor numerico valido (menor a 54)")

        case 23:
            muestra_posicion_en_ranking(Lista_dreamteam)
            print("""\nArchivo exportado con exito!
                                ⢀⣠⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣀⠀⠀⠀⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣷⣆⣴⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡿⠋⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⡟⠁⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠟⠁⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⡇⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠯⠟⡿⠛⠧⠀⠀⠀⢠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⡿⠛⠋⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀ ⣠⣴⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣦⣤  ⠀⣀⣤⡄
⠀⠀⢀⣀⣴⣾⣿⣿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⡿⠋⠀
⢸⣿⣿⣿⣿⣿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡿⠛⠉⠀⠀⠀
⠀⠙⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """)

        case 0:
            break   