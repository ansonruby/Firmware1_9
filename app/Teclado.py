#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------
# Importacion de los módulos
# ---------------------------

import pygame
from pygame.locals import *
import commands
import sys
import time

import lib.Control_Archivos  as Ca
import lib.Control_Ethernet

#-----------------------------------
#           Definiciones
#-----------------------------------
Leer		        = Ca.Leer_Led
Borrar		        = Ca.Borrar_Archivo
Escrivir_Estados    = Ca.Escrivir_Estados
Escrivir            = Ca.Escrivir_Archivo
Leer_Estado         = Ca.Leer_Estado

Serial              = lib.Control_Ethernet.ID_Tarjeta
Estatus_Coneccion   = lib.Control_Ethernet.Estatus_Coneccion
Estados_Internet    = lib.Control_Ethernet.Estados_Internet

#-----------------------------------
#    Variables de configuracion
#-----------------------------------
Estado_Forzar_Firmware = 0
Estado_Informacion = 0
Contador_vista_Inf=0

operator= ""
Texto_Display= ""
Contador_Menu=0

Memoria = ""
Tamano = 11

#-----------
# estados eternet y wifi
Contador_vista=0
Relleno=1
Divicion=0
Tipo_comec=0
Conectividad =''
Antes_Conectividad=''

#-------------
#   estadodes de internet por test


# -----------
# Constantes
# -----------
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 480

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------

def imprimir_texto(screen, texto, x, y, color, fuente):

    pygame.draw.rect(screen,(32,112,164), (x,y-10, 245, 250))


    fuente = pygame.font.SysFont("Arial", 20)


    # separa el texto en elementos de una lista
    # ejemplo: convierte "hola \n mundo" en ["hola ", " mundo"
    texto_en_lineas = texto.split('\n')

    # un bucle que itera por cada una de las lineas del texto
    for linea in texto_en_lineas:
        nueva = fuente.render(linea, 1, color)

        # imprime en pantalla (se debe ejecutar pygame.display.flip() luego
        screen.blit(nueva, (x, y))

        # reduce la altura de la coordenada vertical, para luego volver
        # a imprimir la siguiente linea de texto mas abajo
        y += nueva.get_height()

    fuente = pygame.font.SysFont("Arial", 40)

def Inf_Dispositivo():


        Inf =''
        C =str(Leer_Estado(29)).split('\n')  # version firmware
        #print C[0]
        Inf +='              '+C[0]+'\n'
        Inf += 'Version:'+str(Leer_Estado(17))  # vercion firmware

        Inf +='              Nombre\n'
        Inf += commands.getoutput('hostname')
        Inf +='\n'

        Inf +='              Serial\n'
        Inf +=Serial[0:12]+'xxx'+Serial[12+12:12+12+6]
        Inf +='\n'

        Inf +='              Conexion\n'
        IPs = commands.getoutput('hostname -I')
        texto_en_lineas = IPs.split(' ')

        for linea in texto_en_lineas:
            if len(linea)>=3:
                Inf +='IP: '
                Inf +=linea
                Inf +='\n'
        #print res2
        #print Serial

        #print Inf
        return Inf

"""
def Estatus_Coneccion (c):
        res2 = commands.getoutput('cat /sys/class/net/'+c+'/carrier')
        if res2 == '0':     return 0 #  print 'Desconectado'
        else:               return 1 # print 'Conectado'


def Estados_Internet():
        Sres = ""
        Cantidad =0
        res = commands.getoutput('ls /sys/class/net/')
        redes =res.split("\n")

        for x1 in range(len(redes)):
                c= redes[x1]
                #print c
                if c.find('eth') != -1: #print 'ethernet'
                        if Estatus_Coneccion (c) == 0:  #print 'ED'
                            Sres = Sres + 'ED'
                            Cantidad+=1
                        else:                           #print 'EC'
                            Sres = Sres + 'EC'
                            Cantidad+=1
                if c.find('wlan') != -1: #print 'Wifi'

                        if Estatus_Coneccion (c) == 0:  #print 'WD'
                                Sres = Sres + 'WD'
                                Cantidad+=1
                        else:                           #print 'WC'
                                Sres = Sres + 'WC'
                                Cantidad+=1
        #print str(Cantidad) + Sres
        return  str(Cantidad) + Sres

"""




def motion(x,y):

    Ix=40
    Iy=75
    Disx=75+10
    Disy=75+10

    if (x >= Ix+(Disx*0)) and (x<=Ix+75+(Disx*0)) and (y >= Iy+(Disy*0)-10) and (y <= Iy+70+(Disy*0)) : clickbut(1) #print "Tecla 1"
    if (x >= Ix+(Disx*1)) and (x<=Ix+75+(Disx*1)) and (y >= Iy+(Disy*0)-10) and (y <= Iy+70+(Disy*0)) : clickbut(2) #print "Tecla 2"
    if (x >= Ix+(Disx*2)) and (x<=Ix+75+(Disx*2)) and (y >= Iy+(Disy*0)-10) and (y <= Iy+70+(Disy*0)) : clickbut(3) #print "Tecla 3"
    if (x >= Ix+(Disx*0)) and (x<=Ix+75+(Disx*0)) and (y >= Iy+(Disy*1)) and (y <= Iy+70+(Disy*1)) :    clickbut(4) #print "Tecla 4"
    if (x >= Ix+(Disx*1)) and (x<=Ix+75+(Disx*1)) and (y >= Iy+(Disy*1)) and (y <= Iy+70+(Disy*1)) :    clickbut(5) #print "Tecla 5"
    if (x >= Ix+(Disx*2)) and (x<=Ix+75+(Disx*2)) and (y >= Iy+(Disy*1)) and (y <= Iy+70+(Disy*1)) :    clickbut(6) #print "Tecla 6"
    if (x >= Ix+(Disx*0)) and (x<=Ix+75+(Disx*0)) and (y >= Iy+(Disy*2)) and (y <= Iy+70+(Disy*2)) :    clickbut(7) #print "Tecla 7"
    if (x >= Ix+(Disx*1)) and (x<=Ix+75+(Disx*1)) and (y >= Iy+(Disy*2)) and (y <= Iy+70+(Disy*2)) :    clickbut(8) #print "Tecla 8"
    if (x >= Ix+(Disx*2)) and (x<=Ix+75+(Disx*2)) and (y >= Iy+(Disy*2)) and (y <= Iy+70+(Disy*2)) :    clickbut(9) #print "Tecla 9"
    if (x >= Ix+(Disx*0)) and (x<=Ix+75+(Disx*0)) and (y >= Iy+(Disy*3)) and (y <= Iy+70+(Disy*3)) :    clrbut() #print "Tecla c"
    if (x >= Ix+(Disx*1)) and (x<=Ix+75+(Disx*1)) and (y >= Iy+(Disy*3)) and (y <= Iy+70+(Disy*3)) :    clickbut(0) #print "Tecla 0"
    if (x >= Ix+(Disx*2)) and (x<=Ix+75+(Disx*2)) and (y >= Iy+(Disy*3)) and (y <= Iy+70+(Disy*3)) :    clickbut(11) #print "Tecla k"
    if (x >= Ix+(Disx*0)) and (x<=Ix+75+(Disx*2)) and (y >= Iy+(Disy*4)) and (y <= Iy+70+(Disy*4)) :    equlbut() #print "Tecla OK"


def clickbut(number): # teclas de 0-9 y k
    global operator
    global Contador_Menu
    global Texto_Display
    global Memoria
    global Tamano
    global Estado_Informacion
    global Estado_Forzar_Firmware

    #print Contador_Menu
    #print number


    if Contador_Menu == 3:# Numero de borrados
            if number == 11: #Digito teclado
                    Estado_Forzar_Firmware = 1
                    #print Estado_Informacion
                    print 'Forzar Actualizacion Firmware'

    if Contador_Menu == 3:# Numero de borrados
            if number == 1: #Digito teclado
                    Estado_Informacion = 1
                    #print Estado_Informacion
                    print 'ver informacion dispositivo'

    Contador_Menu=0

    if number == 11:
        number = 'K'

    N_Teclas = len(operator)

    if N_Teclas > 0:
        operator=operator+str(number)
        #Texto_Display = operator
        Escrivir_Estados('1',6)# activar sonido por 500*2
        Memoria = operator
    elif number != 0:
        operator=operator+str(number)
        #Texto_Display  = operator
        Escrivir_Estados('1',6)# activar sonido por 500*2
        Memoria = operator

    N_Teclas = len(operator)

    if N_Teclas >= Tamano:
        #print 'visualisar diferente'
        Memoria=Memoria[N_Teclas-Tamano:N_Teclas+1]


    Texto_Display = Memoria




def equlbut():  #para el boton k
     global operator
     global Contador_Menu
     global Texto_Display
     global Memoria



     Contador_Menu=0

     if len(operator) > 0:

          add = operator
          Borrar(5)
          Escrivir(add,5)

          operator=""
          Memoria=""
          Texto_Display  = operator
          Escrivir_Estados('1',4)

     Escrivir_Estados('1',6)# activar sonido por 500*2


def clrbut(): #para el boton c borrar

    global operator
    global Contador_Menu
    global Texto_Display
    global Memoria

    trama = len(operator)
    if trama > 0:
        operator=operator[:trama-1]
        Memoria = operator
        #Texto_Display = operator
    else:
        operator=""
        Memoria = operator
        #Texto_Display = operator
        Contador_Menu+=1

    Escrivir_Estados('1',6)# activar sonido por 500*2

    N_Teclas = len(operator)

    if N_Teclas >= Tamano:
        #print 'visualisar diferente'
        Memoria=Memoria[N_Teclas-Tamano:N_Teclas+1]

    Texto_Display = Memoria

    print Contador_Menu

    if Contador_Menu == 5:# numero de veces para activar la configuracion wifi
        Contador_Menu = 0

        pygame.quit()
        commands.getoutput('python /home/pi/Firmware/app/Menu_Config.py')
        sys.exit()
        #pygame.QUIT:



# ------------------------------
#       Funcion principal
# ------------------------------


def main():

    global Texto_Display
    global Contador_vista
    global Antes_Conectividad
    global Divicion
    global Estado_Informacion
    global Contador_vista_Inf
    global Estado_Forzar_Firmware

    Esta_QR_Repetido = 0
    retraso=0
    #-------------------------------------------------------------
    #              Inicioando Elementos Graficos
    #-------------------------------------------------------------
    print 'Iniciando Elementos Graficos'
    pygame.init()

    # Tamano de la ventana
    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,0)
    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.set_caption("pruebas pygame")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo       = pygame.image.load("/home/pi/Firmware/img/keypad-fondo.png").convert()
    fondo2       = pygame.image.load("/home/pi/Firmware/img/Keypad-Borrar_Amarillo.png").convert()
    Denegado    = pygame.image.load("/home/pi/Firmware/img/denegado.png").convert_alpha()
    Denegado    = pygame.transform.scale(Denegado,(330,310))
    Permitido   = pygame.image.load("/home/pi/Firmware/img/permitido.png").convert_alpha()
    if Serial.find("CCCB") != -1: #ID_Tratado = IDQ
        #Per_Derecha   = pygame.image.load("/home/pi/Firmware/img/derecha.png").convert_alpha()
        Per_Derecha     = pygame.transform.scale(Permitido,(290,290))
        #Per_Izquierda   = pygame.transform.rotate(Permitido,180)
        Per_Izquierda     = pygame.transform.scale(Permitido,(290,290))
    else:
        Per_Derecha   = pygame.image.load("/home/pi/Firmware/img/derecha.png").convert_alpha()
        Per_Derecha     = pygame.transform.scale(Per_Derecha,(290,290))
        Per_Izquierda   = pygame.transform.rotate(Per_Derecha,180)
        #Per_Izquierda     = pygame.transform.scale(Per_Izquierda,(240,290))

    Alerta      = pygame.image.load("/home/pi/Firmware/img/alerta2.png").convert_alpha()
    #Alerta     = pygame.transform.scale(Alerta,(480,210))
    Alerta2     = pygame.image.load("/home/pi/Firmware/img/CirVerde.png").convert_alpha()
    Alerta2     = pygame.transform.scale(Alerta2,(290,290))
    Teclado     = pygame.image.load("/home/pi/Firmware/img/teclado.png").convert_alpha()
    fuente = pygame.font.SysFont("Arial", 40)

    screen.blit(fondo, (0, 0))  # pintando fondo
    pygame.display.flip()       # se muestran lo cambios en pantalla





    #-------------------------------------------------------------
    #              Ciclo programa principal
    #-------------------------------------------------------------
    while True:
        #------------------------------------------
        #           tiempo de espera
        #------------------------------------------
        time.sleep(0.05)

        #------------------------------------------
        #           Pintado del fondo
        #------------------------------------------
        if Leer_Estado(28) == '0':
            #print Leer_Estado(28)
            screen.blit(fondo, (0, 0))
        else:
            screen.blit(fondo2, (0, 0))


        #-----------------------------------
        #       Alerta sin prioridad
        #-----------------------------------
        if Leer_Estado(11) == '2' and Leer_Estado(8) != '1':
            print Leer_Estado(8)
            #screen.blit(Alerta2, (15, 94))
            #screen.blit(Alerta, (32, 210))
            screen.blit(Alerta, (0,0))
            #pygame.draw.rect(screen,(255,255,255),[20,5,285,465])
            #screen.blit(Alerta, (-25, 120))
            Esta_QR_Repetido += 1
            if Esta_QR_Repetido >= 18:
                Esta_QR_Repetido = 0
                Borrar(11)# borrar estado 2


        #-----------------------------------
        #       Estados de prioridad
        #-----------------------------------
        Lec_estado = Leer_Estado(10)

        #leer el estado de los procesos
        if Lec_estado != '0':                       # Proceso inicil
            if Lec_estado == '6':
                Esta_QR_Repetido = 0
                Borrar(11)# borrar estado 2
                screen.blit(Denegado, (-20, 70))    # Denegado
            elif Lec_estado == '3':
                Esta_QR_Repetido = 0
                Borrar(11)# borrar estado 2
                pygame.draw.rect(screen,(255,255,255),[20,5,285,465])
                screen.blit(Per_Derecha, (20, 100))   # Permitido
            elif Lec_estado == '4':
                Esta_QR_Repetido = 0
                Borrar(11)# borrar estado 2
                pygame.draw.rect(screen,(255,255,255),[20,5,285,465])
                screen.blit(Per_Izquierda, (20, 100))   # Permitido


        #--------------------------------------------------
        #               Display
        #--------------------------------------------------
        mensaje = fuente.render(Texto_Display, 1, (255, 255, 255))
        screen.blit(mensaje, (40, 10))

        #--------------------------------------------------
        #               colores de estado de conectividad
        #--------------------------------------------------

        Contador_vista = Contador_vista +1
        if Contador_vista <= 2:

                for x1 in range(Divicion):
                        conec= Conectividad[1+x1*2]+ Conectividad[2+x1*2]

                        if conec == 'ED' :              #Azul oscura ethernet desconectado
                                Relleno=0
                                Tipo_comec=0
                        if conec == 'EC' :              #Azul claro ethernet conectado
                                Relleno=1
                                Tipo_comec=0
                        if conec == 'WD' :              #Magenta wifi desconectado
                                Relleno=0
                                Tipo_comec=1
                        if conec == 'WC' :              #Azul claro wifi conectado
                                Relleno=1
                                Tipo_comec=1

                        pygame.draw.circle(screen,(32,112,164),(5+(10)*x1, 475),5,Relleno)
                        if Tipo_comec == 1 :    pygame.draw.line(screen,(0,0,0),(0+(10)*x1 , 475) ,(8+(10)*x1 , 475))



        if Contador_vista >= 30:

                Conectividad = Estados_Internet()
                Divicion = int (Conectividad[0])
                Contador_vista = 0




        if Estado_Informacion == 1:
                Contador_vista_Inf = Contador_vista_Inf+1
                #print 'informaccion cual'
                imprimir_texto(screen,Inf_Dispositivo(), 40, 70, (0,0,0), fuente)
                if Contador_vista_Inf >= 30:
                    Contador_vista_Inf = 0
                    Estado_Informacion = 0



        if Estado_Forzar_Firmware == 1:
                Contador_vista_Inf = Contador_vista_Inf+1
                #print 'informaccion cual'
                Escrivir_Estados('1',40)

                imprimir_texto(screen,"      Forzando\n Actualizacion\n     Firmware\n", 40, 70, (0,0,0), fuente)
                if Contador_vista_Inf >= 30:
                    Contador_vista_Inf = 0
                    Estado_Forzar_Firmware = 0


        #--------------------------------------------------
        # se muestran lo cambios en pantalla
        #--------------------------------------------------
        pygame.display.flip()

        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                motion(x,y)


if __name__ == "__main__":
    main()
