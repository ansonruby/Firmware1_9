# -*- coding: utf-8 -*-
# Librerias creadas para multi procesos o hilos -------------
#import random
import lib.Control_Archivos
import lib.Seguridad
#import time

from datetime import datetime
from datetime import timedelta

# definiciones para el aplicativo principal -----------------

Leer_Archivo            = lib.Control_Archivos.Leer_Archivo
Borrar                  = lib.Control_Archivos.Borrar_Archivo
Escrivir_Archivo        = lib.Control_Archivos.Escrivir_Archivo

MD5		        = lib.Seguridad.MD5


def Generador_Pines(N_PINES):

    Usuarios = Leer_Archivo(0)
    Key = Leer_Archivo(25)

    now = datetime.now()
    Fecha = now.strftime('%Y%m%d')

    #Fecha ='20200225'
    #print(Fecha)

    Borrar(26)
    for linea in Usuarios.split('\n'):
        if len (linea) >5 :
            Lista_Pines =''
            linea = linea.split('.')
            ID= linea[0].rstrip('\r')
            Rut_MD5 = linea[1].rstrip('\r')

            for x in  range(N_PINES):
                if x == 0   : Resualtado = MD5(Key + Rut_MD5+ Fecha)
                else        : Resualtado = MD5(Resualtado)
                #print 'MD5:' + Resualtado
                Numeros =''
                contador =0
                for letra in Resualtado:
                    if letra.isalpha() == False:
                        Numeros += letra
                contador =0
                N_Salto =''
                #print Numeros
                inv_numeros = Numeros[::-1] # invertir lista de nuemros
                #print inv_numeros
                for Numero in inv_numeros:
                    if contador%2 == 0 :
                        N_Salto += Numero
                    contador = contador + 1

                if len (N_Salto[0:4]) > 3:
                    Lista_Pines = Lista_Pines + '.'+ N_Salto[0:4]
                else:
                    N_Salto += '9999'
                    Lista_Pines = Lista_Pines + '.'+ N_Salto[0:4]
                    #print 'numero de faltantes'

            cadena = ID + Lista_Pines  # +'\n'
            #print cadena
            Escrivir_Archivo(cadena,26)

    print 'pines listos'


#Generador_Pines(4)
