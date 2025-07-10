import random
from Constantes import *
import pygame

def cargar_preguntas_desde_csv(ruta_csv: str) -> list:
    preguntas = []
    with open(ruta_csv, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines() 
        for linea in lineas[1:]:
            datos = [dato.strip() for dato in linea.split(",")]
            
     
            pregunta = {
                "pregunta": datos[0],
                "respuesta_1": datos[1],
                "respuesta_2": datos[2],
                "respuesta_3": datos[3],
                "respuesta_4": datos[4],
                "correcta":int(datos[5]),
                "porcentaje_aciertos": float(datos[6]) if len(datos) > 6 else 0.0,
                "aciertos": int(datos[7]) if len(datos) > 7 else 0,
                "fallos": int(datos[8]) if len(datos) > 8 else 0,
                "veces_preguntada": int(datos[9]) if len(datos) > 9 else 0,
            }
            preguntas.append(pregunta)
    return preguntas


class Comodines:
    def __init__(self):
        self.bomba = True
        self.bomba_usada = False

        self.puntos_x2 = False
        self.x2_usado = False

        self.doble_disponible = True
        self.doble_activado = False   

        self.pasar = True
        self.pasar_usado = False

        self.respuestas_ocultas = []

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()] 
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height

def crear_elemento_juego(textura: str, ancho: int, alto: int, pos_x: int, pos_y: int) -> dict:
    elemento_juego = {}
    elemento_juego["superficie"] = pygame.transform.scale(pygame.image.load(textura), (ancho, alto))
    elemento_juego["rectangulo"] = pygame.Rect(pos_x, pos_y, ancho, alto)
    return elemento_juego

def crear_lista_respuestas(textura: str, ancho: int, alto: int, pos_x: int, pos_y: int):
    lista_respuestas = []
    for i in range(4):
        respuesta = crear_elemento_juego(textura, ancho, alto, pos_x, pos_y)
        lista_respuestas.append(respuesta)
        pos_y += 80
    return lista_respuestas

def crear_botones_menu() -> list:
    lista_botones = []
    pos_x = 125
    pos_y = 115
    for i in range(4):
        boton = crear_elemento_juego("imagenes/textura_respuesta.jpg", ANCHO_BOTON, ALTO_BOTON, pos_x, pos_y)
        pos_y += 80
        lista_botones.append(boton)
    return lista_botones

def limpiar_superficie(elemento_juego: dict, textura: str, ancho: int, alto: int):
    elemento_juego["superficie"] = pygame.transform.scale(pygame.image.load(textura), (ancho, alto))

def guardar_preguntas_en_csv(ruta_csv: str, preguntas: list):
    with open(ruta_csv, "w", encoding="utf-8") as archivo:
        archivo.write("pregunta,respuesta_1,respuesta_2,respuesta_3,respuesta_4,correcta,porcentaje_aciertos,aciertos,fallos,veces_preguntada\n")
        for pregunta in preguntas:
            linea = f'{pregunta["pregunta"]},{pregunta["respuesta_1"]},{pregunta["respuesta_2"]},{pregunta["respuesta_3"]},{pregunta["respuesta_4"]},{pregunta["correcta"]},{pregunta["porcentaje_aciertos"]:.2f},{pregunta["aciertos"]},{pregunta["fallos"]},{pregunta["veces_preguntada"]}\n'
            archivo.write(linea)

def verificar_respuesta(datos_juego: dict, pregunta_actual: dict, respuesta: int, comodines=None) -> bool:
    pregunta_actual["veces_preguntada"] += 1

    if pregunta_actual["correcta"] == respuesta:
        pregunta_actual["aciertos"] += 1
        pregunta_actual["porcentaje_aciertos"] = (pregunta_actual["aciertos"] * 100) / pregunta_actual["veces_preguntada"]
        puntos = PUNTUACION_ACIERTO
        if comodines and comodines.puntos_x2:
            puntos *= 2
            comodines.puntos_x2 = False

        datos_juego["puntuacion"] += puntos
        datos_juego["correctas_seguidas"] += 1

        if datos_juego["correctas_seguidas"] >= 5:
            datos_juego["tiempo_restante"] += 10
            datos_juego["correctas_seguidas"] = 0

        return True

    else:
        pregunta_actual["fallos"] += 1
        pregunta_actual["porcentaje_aciertos"] = (pregunta_actual["aciertos"] * 100) / pregunta_actual["veces_preguntada"]

        if comodines and comodines.doble_activado:
            if respuesta not in comodines.respuestas_ocultas:
                comodines.respuestas_ocultas.append(respuesta)
            comodines.doble_activado = False
            return None

        if respuesta not in comodines.respuestas_ocultas:
            comodines.respuestas_ocultas.append(respuesta)

        datos_juego["correctas_seguidas"] = 0
        datos_juego["puntuacion"] -= PUNTUACION_ERROR
        datos_juego["vidas"] -= 1
        return False


def reiniciar_estadisticas(datos_juego: dict):
    datos_juego["vidas"] = CANTIDAD_VIDAS
    datos_juego["puntuacion"] = 0
    datos_juego["nombre"] = ""
    datos_juego["tiempo_restante"] = TIEMPO_JUEGO

def pasar_pregunta(lista_preguntas: list, indice: int, cuadro_pregunta: dict, lista_respuestas: list) -> dict:
    pregunta_actual = lista_preguntas[indice]
    limpiar_superficie(cuadro_pregunta, "imagenes/textura_pregunta.jpg", ANCHO_PREGUNTA, ALTO_PREGUNTA)
    for i in range(len(lista_respuestas)):
        limpiar_superficie(lista_respuestas[i], "imagenes/textura_respuesta.jpg", ANCHO_BOTON, ALTO_BOTON)
    return pregunta_actual

def mezclar_lista(lista_preguntas: list) -> None:
    random.shuffle(lista_preguntas)

    def __init__(self):
        self.bomba = True
        self.puntos_x2 = False
        self.doble_chance = True
        self.pasar = True