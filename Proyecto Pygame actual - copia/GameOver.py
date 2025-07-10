import pygame
from Constantes import *
from Funciones import *

pygame.init()

fuente = pygame.font.SysFont("Arial Narrow", 40)
cuadro = crear_elemento_juego("imagenes/textura_respuesta.jpg", 250, 50, 130, 350)
gameover = FUENTE_GAMEOVER
fondo = pygame.transform.scale(pygame.image.load("imagenes/fondo_gameover.jpg"), PANTALLA)


def mostrar_fin_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
    retorno = "terminado"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"

        elif evento.type == pygame.KEYDOWN:
            bloc_mayus = pygame.key.get_mods() & pygame.KMOD_CAPS
            letra_presionada = pygame.key.name(evento.key)

            if evento.key == pygame.K_RETURN and datos_juego["nombre"].strip() != "":
                retorno = "menu"  

            elif evento.key == pygame.K_BACKSPACE and len(datos_juego["nombre"]) > 0:
                datos_juego["nombre"] = datos_juego["nombre"][:-1]
                limpiar_superficie(cuadro, "imagenes/textura_respuesta.jpg", 250, 50)

            elif evento.key == pygame.K_SPACE:
                datos_juego["nombre"] += " "

            elif len(letra_presionada) == 1 and letra_presionada.isprintable():
                if len(datos_juego["nombre"]) < 15:
                    if bloc_mayus != 0:
                        datos_juego["nombre"] += letra_presionada.upper()
                    else:
                        datos_juego["nombre"] += letra_presionada.lower()

   
    pantalla.blit(fondo, (0, 0))


    puntos = FUENTE_STATS.render(f"Puntos: {datos_juego['puntuacion']}", True, COLOR_BLANCO)
    vidas = FUENTE_STATS.render(f"Vidas restantes: {datos_juego['vidas']}", True, COLOR_BLANCO)
    ingresar_nombre = FUENTE_STATS.render("Ingresa tu nombre y presiona ENTER:", True, COLOR_BLANCO)

    titulo = FUENTE_GAMEOVER.render("GAME OVER", True, COLOR_ROJO)
    titulo_borde = FUENTE_GAMEOVER.render("GAME OVER", True, COLOR_NEGRO)
    pantalla.blit(titulo_borde, ((PANTALLA[0] - titulo.get_width()) // 2 + 2, 52))
    pantalla.blit(titulo, ((PANTALLA[0] - titulo.get_width()) // 2, 50))

    pantalla.blit(puntos, ((PANTALLA[0] - puntos.get_width()) // 2, 150))
    pantalla.blit(vidas, ((PANTALLA[0] - vidas.get_width()) // 2, 200))
    pantalla.blit(ingresar_nombre, ((PANTALLA[0] - ingresar_nombre.get_width()) // 2, 280))


    pantalla.blit(cuadro["superficie"], cuadro["rectangulo"])
    mostrar_texto(cuadro["superficie"], datos_juego["nombre"], (10, 5), FUENTE_STATS, COLOR_BLANCO)

    return retorno