import pygame
pygame.init()

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
ANCHO = 500
ALTO = 550
PANTALLA = (ANCHO,ALTO)
FPS = 30



BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_PUNTUACIONES = 2
BOTON_SALIR = 3

ANCHO_PREGUNTA = 350
ALTO_PREGUNTA = 150
ANCHO_BOTON = 200
ALTO_BOTON = 60
COLOR_TITULO = (255, 215, 0) 

COLOR_BOTON_HOVER = (100, 100, 100)
TAMAÑO_BOTON_VOLUMEN = (60,60)
TAMAÑO_BOTON_VOLVER = (100,40)
CLICK_SONIDO = pygame.mixer.Sound("sonidos/click.mp3")
ERROR_SONIDO = pygame.mixer.Sound("sonidos/error.mp3")
FUENTE_PREGUNTA = pygame.font.Font("fuentes/Neuropol.otf",25)
FUENTE_RESPUESTA = pygame.font.Font("fuentes/BebasNeue-Regular.ttf",30)
FUENTE_TEXTO = pygame.font.Font("fuentes/Nulshock Bd.otf",20)
FUENTE_VOLUMEN = pygame.font.SysFont("Arial",50,True)
FUENTE_GAMEOVER = pygame.font.Font("fuentes/PLANK.TTF",65)
FUENTE_BOTONES = pygame.font.Font("fuentes/911porschav3.ttf",30)
FUENTE_STATS = pygame.font.Font("fuentes/Neuropol.otf", 36)
FUENTE_TITULO = pygame.font.Font("fuentes/Game Of Squids.ttf",43)
FUENTE_AJUSTES = pygame.font.Font("fuentes/911porschav3.ttf",25)
FUENTE_RANKING = pygame.font.Font("fuentes/Game Of Squids.ttf",30)


CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25
TIEMPO_JUEGO = 120