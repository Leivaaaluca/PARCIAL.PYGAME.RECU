import pygame 
import random
from Constantes import *
from Menu import *
from Juego import *
from ajustes import *
from Rankings import *
from GameOver import *
from Funciones import crear_elemento_juego
from Funciones import guardar_preguntas_en_csv

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Quiz de Futbol")
icono = pygame.image.load("imagenes/icono.png")
pygame.display.set_icon(icono)
random.shuffle(lista_preguntas)
pantalla = pygame.display.set_mode(PANTALLA)
corriendo = True
datos_juego = {"puntuacion":0,"vidas":CANTIDAD_VIDAS,"nombre":"","tiempo_restante":TIEMPO_JUEGO,"correctas_seguidas": 0,"volumen_musica":50,"volumen_efectos": 50,"musica_activada":True,"indice":0}
pygame.mixer.music.load("sonidos/musica.mp3")  
pygame.mixer.music.set_volume(datos_juego["volumen_musica"] / 100)  
pygame.mixer.music.play(-1) 
RUTA_CSV = "preguntas.csv" 
lista_preguntas = cargar_preguntas_desde_csv(RUTA_CSV)


lista_rankings = []
reloj = pygame.time.Clock()
ventana_actual = "menu"

bandera_juego = False

comodines = Comodines()
boton_bomba = crear_elemento_juego("imagenes/textura_respuesta.jpg", 90, 50, 20, 300)
boton_x2 = crear_elemento_juego("imagenes/textura_respuesta.jpg", 90, 50, 20, 360)
boton_doble = crear_elemento_juego("imagenes/textura_respuesta.jpg", 90, 50, 20, 420)
boton_pasar = crear_elemento_juego("imagenes/textura_respuesta.jpg", 90, 50, 20, 480)

juego_iniciado = False

while corriendo:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get()

    if ventana_actual == "menu":
        juego_iniciado = False 
        ventana_actual = mostrar_menu(pantalla, cola_eventos)
    elif ventana_actual == "salir":
        corriendo = False
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(pantalla, cola_eventos, lista_rankings)
    elif ventana_actual == "ajustes":
        ventana_actual = mostrar_ajustes(pantalla, cola_eventos, datos_juego)
    elif ventana_actual == "juego":
        if not juego_iniciado:
            reiniciar_estadisticas(datos_juego)
            comodines = Comodines()
            random.shuffle(lista_preguntas)
            bandera_juego = True
            juego_iniciado = True
        ventana_actual = mostrar_juego(
            pantalla, cola_eventos, datos_juego, lista_preguntas, comodines,
            boton_bomba, boton_x2, boton_doble, boton_pasar
        )
    elif ventana_actual == "terminado":
        nueva_ventana = mostrar_fin_juego(pantalla, cola_eventos, datos_juego)
        if nueva_ventana != "terminado" and bandera_juego:
            bandera_juego = False
            if datos_juego["nombre"].strip() != "":
                agregar_puntaje(datos_juego["nombre"], datos_juego["puntuacion"])
                datos_juego["nombre"] = ""

            guardar_preguntas_en_csv(RUTA_CSV, lista_preguntas)

        ventana_actual = nueva_ventana
    pygame.display.flip()

pygame.quit()