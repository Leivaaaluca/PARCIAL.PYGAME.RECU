import pygame
import json
import os
from Constantes import *
from Funciones import *

pygame.init()
RUTA_RANKING = "ranking.json"

boton_volver = crear_elemento_juego("imagenes/textura_respuesta.jpg",100,40,10,10)
fondo =  pygame.transform.scale(pygame.image.load("imagenes/imagen_ranking.jpg"), PANTALLA)

def cargar_ranking() -> list:
    with open(RUTA_RANKING, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def guardar_ranking(ranking: list):
    with open(RUTA_RANKING, "w", encoding="utf-8") as archivo:
        json.dump(ranking, archivo, indent=4)

def agregar_puntaje(nombre: str, puntaje: int):
    ranking = cargar_ranking()
    ranking.append({"nombre": nombre, "puntaje": puntaje})

    
    ranking = sorted(ranking, key=lambda jugador: jugador["puntaje"], reverse=True)

    ranking = ranking[:10]

    guardar_ranking(ranking)
def mostrar_rankings(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], lista_rankings: list) -> str:
    retorno = "rankings"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_volver["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "menu"

    pantalla.blit(fondo, (0, 0))
    pantalla.blit(boton_volver["superficie"], boton_volver["rectangulo"])
    mostrar_texto(pantalla, "RANKING", (50, 50), FUENTE_GAMEOVER, COLOR_TITULO)
    mostrar_texto(boton_volver["superficie"], "VOLVER", (5, 5), FUENTE_RESPUESTA, COLOR_BLANCO)

    ranking = cargar_ranking()
    y = 130
    for i, jugador in enumerate(ranking):
        texto = f"{i+1}. {jugador['nombre']} = {jugador['puntaje']} pts"
        mostrar_texto(pantalla, texto, (60, y), FUENTE_RANKING, COLOR_BLANCO)
        y += 40

    return retorno
    