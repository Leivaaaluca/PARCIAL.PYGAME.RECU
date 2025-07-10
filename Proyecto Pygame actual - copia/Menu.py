import pygame
from Constantes import *
from Funciones import *

pygame.init()
lista_botones = crear_botones_menu()
fondo_pantalla = pygame.transform.scale(pygame.image.load("imagenes/menufoto.jpg"),PANTALLA)
fondo_titulo = pygame.transform.scale(pygame.image.load("imagenes/fondotitulo4.jpg"), (400,100)) 


def mostrar_menu(pantlla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    retorno = "menu"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                for i in range(len(lista_botones)):
                    if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                        if i == BOTON_JUGAR:
                            retorno = "juego"
                        elif i == BOTON_CONFIG:
                            retorno = "ajustes"
                        elif i == BOTON_PUNTUACIONES:
                            retorno = "rankings"
                        else:
                            retorno = "salir"
    
    pantlla.blit(fondo_pantalla,(0,0))
      
    titulo_x = (PANTALLA[0] - fondo_titulo.get_width()) // 2
    titulo_y = 10 
    pantlla.blit(fondo_titulo, (titulo_x, titulo_y))
    
    titulo = FUENTE_TITULO.render("QUIZ DE FUTBOL", True, COLOR_BLANCO)
    titulo_rect = titulo.get_rect(center=(PANTALLA[0] // 2, 55)) 
    pantlla.blit(titulo, titulo_rect)
 
    for i in range(len(lista_botones)):
        pantlla.blit(lista_botones[i]["superficie"],lista_botones[i]["rectangulo"])
        
    mostrar_texto(lista_botones[BOTON_JUGAR]["superficie"],"JUGAR",(30,20),FUENTE_BOTONES,COLOR_BLANCO)
    mostrar_texto(lista_botones[BOTON_CONFIG]["superficie"],"AJUSTES",(15,20),FUENTE_AJUSTES,COLOR_BLANCO)
    mostrar_texto(lista_botones[BOTON_PUNTUACIONES]["superficie"],"TOP 10",(20,20),FUENTE_BOTONES,COLOR_BLANCO)
    mostrar_texto(lista_botones[BOTON_SALIR]["superficie"],"SALIR",(30,15),FUENTE_BOTONES,COLOR_BLANCO)


    return retorno
    
    


