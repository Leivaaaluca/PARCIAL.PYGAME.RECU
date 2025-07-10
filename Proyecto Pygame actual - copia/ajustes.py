import pygame
from Constantes import *
from Funciones import *

pygame.init()

boton_suma = crear_elemento_juego("imagenes/mas.webp", 60, 60, 420, 200)
boton_resta = crear_elemento_juego("imagenes/menos.webp", 60, 60, 20, 200)
boton_volver = crear_elemento_juego("imagenes/textura_respuesta.jpg", 100, 40, 10, 10)
boton_musica = crear_elemento_juego("imagenes/muteo.png", 150,150, 180, 250)
fondo = pygame.transform.scale(pygame.image.load("imagenes/ajustes_foto.jpg"), PANTALLA)

def mostrar_ajustes(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juegos: dict) -> str:
    retorno = "ajustes"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                retorno = "menu"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_suma["rectangulo"].collidepoint(evento.pos):
                    if datos_juegos["volumen_musica"] < 100:
                        datos_juegos["volumen_musica"] += 5
                        CLICK_SONIDO.play()
                        pygame.mixer.music.set_volume(datos_juegos["volumen_musica"] / 100)
                    else:
                        ERROR_SONIDO.play()
                
                elif boton_resta["rectangulo"].collidepoint(evento.pos):
                    if datos_juegos["volumen_musica"] > 0:
                        datos_juegos["volumen_musica"] -= 5
                        CLICK_SONIDO.play()
                        pygame.mixer.music.set_volume(datos_juegos["volumen_musica"] / 100)
                    else:
                        ERROR_SONIDO.play()
                
                elif boton_musica["rectangulo"].collidepoint(evento.pos):
                    datos_juegos["musica_activada"] = not datos_juegos["musica_activada"]
                    CLICK_SONIDO.play()
                    if datos_juegos["musica_activada"]:
                        pygame.mixer.music.set_volume(datos_juegos["volumen_musica"] / 100)
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                
                elif boton_volver["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    retorno = "menu"
    
    pantalla.blit(fondo, (0, 0))

    pantalla.blit(boton_suma["superficie"], boton_suma["rectangulo"])
    pantalla.blit(boton_resta["superficie"], boton_resta["rectangulo"])
    pantalla.blit(boton_volver["superficie"], boton_volver["rectangulo"])
    pantalla.blit(boton_musica["superficie"], boton_musica["rectangulo"])
    
    mostrar_texto(pantalla, "VOLUMEN", (70, 100), FUENTE_GAMEOVER, COLOR_BLANCO)
    mostrar_texto(pantalla, f"{datos_juegos['volumen_musica']}%", (200, 200), FUENTE_VOLUMEN, COLOR_BLANCO)
    mostrar_texto(boton_volver["superficie"], "VOLVER", (5, 5), FUENTE_RESPUESTA, COLOR_BLANCO)
    
 

    return retorno