import pygame
import random
from Constantes import *
from Funciones import *
from Preguntas import *
pygame.init()

fondo_pantalla = pygame.transform.scale(pygame.image.load("imagenes/fondo.jpg"), PANTALLA)
cuadro_pregunta = crear_elemento_juego("imagenes/textura_pregunta.jpg", ANCHO_PREGUNTA, ALTO_PREGUNTA, 80, 80)
lista_respuestas = crear_lista_respuestas("imagenes/textura_respuesta.jpg", ANCHO_BOTON, ALTO_BOTON, 125, 245)

evento_tiempo = pygame.USEREVENT 
pygame.time.set_timer(evento_tiempo, 1000)

class Comodines:
    def __init__(self):
        self.bomba = True
        self.bomba_usada = False

        self.puntos_x2 = False
        self.x2_usado = False

        self.doble_chance = False 
        self.doble_usada = False

        self.pasar = True
        self.pasar_usado = False

        self.respuestas_ocultas = []

def mostrar_juego(pantalla, cola_eventos, datos_juego, lista_preguntas, comodines, boton_bomba, boton_x2, boton_doble, boton_pasar) -> str:
    retorno = "juego"
    pregunta_actual = lista_preguntas[datos_juego["indice"]]

    if datos_juego["vidas"] == 0 or datos_juego["tiempo_restante"] == 0:
        return "terminado"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            return "salir"
        
        elif evento.type == evento_tiempo:
            datos_juego["tiempo_restante"] -= 1

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_bomba["rectangulo"].collidepoint(evento.pos) and comodines.bomba:
                comodines.bomba = False
                comodines.bomba_usada = True
                opciones = [1, 2, 3, 4]
                opciones.remove(pregunta_actual["correcta"])
                comodines.respuestas_ocultas = random.sample(opciones, 2)

            elif boton_x2["rectangulo"].collidepoint(evento.pos) and not comodines.puntos_x2 and not comodines.x2_usado:
                comodines.puntos_x2 = True
                comodines.x2_usado = True

            elif boton_doble["rectangulo"].collidepoint(evento.pos) and comodines.doble_disponible and not comodines.doble_activado:
                comodines.doble_activado = True  
                comodines.doble_disponible = False

            elif boton_pasar["rectangulo"].collidepoint(evento.pos) and comodines.pasar:
                comodines.pasar = False
                comodines.pasar_usado = True
                datos_juego["indice"] += 1
                if datos_juego["indice"] >= len(lista_preguntas):
                    datos_juego["indice"] = 0
                    mezclar_lista(lista_preguntas)
                pregunta_actual = pasar_pregunta(lista_preguntas, datos_juego["indice"], cuadro_pregunta, lista_respuestas)
                comodines.respuestas_ocultas = []

            else:
                for i in range(len(lista_respuestas)):
                    if lista_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                        if (i + 1) in comodines.respuestas_ocultas:
                            break

                        respuesta = i + 1
                        resultado = verificar_respuesta(datos_juego, pregunta_actual, respuesta, comodines)

                        if resultado == True:
                            CLICK_SONIDO.play()
                        elif resultado == False:
                            ERROR_SONIDO.play()

                        if resultado is None:
                            break

                        datos_juego["indice"] += 1
                        if datos_juego["indice"] >= len(lista_preguntas):
                            datos_juego["indice"] = 0
                            mezclar_lista(lista_preguntas)

                        pregunta_actual = pasar_pregunta(lista_preguntas, datos_juego["indice"], cuadro_pregunta, lista_respuestas)
                        comodines.respuestas_ocultas = []
                        break

    pantalla.blit(fondo_pantalla, (0, 0))
    limpiar_superficie(cuadro_pregunta, "imagenes/textura_pregunta.jpg", ANCHO_PREGUNTA, ALTO_PREGUNTA)
    mostrar_texto(cuadro_pregunta["superficie"], pregunta_actual["pregunta"], (15, 15), FUENTE_PREGUNTA, COLOR_BLANCO)
    pantalla.blit(cuadro_pregunta["superficie"], cuadro_pregunta["rectangulo"])

    for boton, label, usado in [
    (boton_bomba, "BOMBA", comodines.bomba_usada),
    (boton_x2, "X2", comodines.x2_usado),
    (boton_doble, "DOBLE", not comodines.doble_disponible),
    (boton_pasar, "PASAR", comodines.pasar_usado)
    ]:
        pantalla.blit(boton["superficie"], boton["rectangulo"])
        mostrar_texto(pantalla, label, (boton["rectangulo"].x + 15, boton["rectangulo"].y + 15), FUENTE_RESPUESTA, COLOR_BLANCO)
        if usado:
            pygame.draw.line(pantalla, COLOR_ROJO, boton["rectangulo"].topleft, boton["rectangulo"].bottomright, 4)
            pygame.draw.line(pantalla, COLOR_ROJO, boton["rectangulo"].topright, boton["rectangulo"].bottomleft, 4)

    for i in range(len(lista_respuestas)):
        if (i + 1) in comodines.respuestas_ocultas:
            lista_respuestas[i]["superficie"].fill(COLOR_VIOLETA)
        else:
            limpiar_superficie(lista_respuestas[i], "imagenes/textura_respuesta.jpg", ANCHO_BOTON, ALTO_BOTON)
            mostrar_texto(
                lista_respuestas[i]["superficie"],
                pregunta_actual[f"respuesta_{i+1}"],
                (15, 15),
                FUENTE_RESPUESTA,
                COLOR_BLANCO
            )
        pantalla.blit(lista_respuestas[i]["superficie"], lista_respuestas[i]["rectangulo"])

    mostrar_texto(pantalla, f"VIDAS: {datos_juego['vidas']}", (10, 10), FUENTE_TEXTO, COLOR_NEGRO)
    mostrar_texto(pantalla, f"PUNTUACION: {datos_juego['puntuacion']}", (10, 40), FUENTE_TEXTO, COLOR_NEGRO)
    mostrar_texto(pantalla, f"TIEMPO: {datos_juego['tiempo_restante']} seg", (275, 10), FUENTE_TEXTO, COLOR_NEGRO)

    return retorno
