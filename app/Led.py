

import lib.Control_Archivos  as Ca

import digitalio
from board import *
import time

import neopixel




Leer			= Ca.Leer_Estado
Borrar			= Ca.Borrar_Archivo


#led = digitalio.DigitalInOut(D26)
#led.direction = digitalio.Direction.OUTPUT

PIXEL_PIN = D21#D21             #pin de control
num_pixels = 10#8#10             #Numero de pixels
num_medio = int(num_pixels/2)   #Mitad de pixel
Led_int=120                     #Intensidad luminica
ORDER = neopixel.RGB            #Pixel color channel order

DELAY = 0.25


pixel = neopixel.NeoPixel(PIXEL_PIN, num_pixels, pixel_order=ORDER)

CL_Blink_0 =0
CL_Blink_1 =0

CL_D_Blink=1 #Duracion del blink  1


def Color(Nombre,ID):

        global num_medio
        global Led_int

        COLOR = (0, 0, 0)
        mitad=0

        if 'Verde' == Nombre:
                COLOR = ( Led_int, 0, 0)
        elif 'Azul' == Nombre:
                COLOR = ( 0, 0, Led_int)
        elif 'Negro' == Nombre:
                COLOR = ( 0, 0, 0)
        elif 'Rojo' == Nombre:
                COLOR = (0, Led_int, 0)
        elif 'Amarillo' == Nombre:
                COLOR = ( Led_int, Led_int, 0)
        elif 'Blanco' == Nombre:
                COLOR = ( Led_int, Led_int, Led_int)
        else :
                COLOR = ( 0, 0, 0)


        if ID == 1:
                mitad=num_medio

        for j in range(num_medio):

                pixel[j+mitad] = COLOR


def Blink_0(i,CL_m):
	global CL_Blink_0
	CL_Blink_0+= 1
	if CL_Blink_0 <=CL_m:
		Color(i,0)
	else:
		Color('Negro',0)

	if CL_Blink_0 >= 2*CL_m:
		CL_Blink_0 = 0

def Blink_1(i,CL_m):
	global CL_Blink_1
	CL_Blink_1+= 1
	if CL_Blink_1 <=CL_m:
		Color(i,1)
	else:
		Color('Negro',1)

	if CL_Blink_1 >= 2*CL_m:
		CL_Blink_1 = 0

# estados del aplicativo ---------------------------------
CL_Estados_Antes=0

def Led_Estados(CL_Estados):

        global CL_Estados_Antes
        if CL_Estados != CL_Estados_Antes :

                CL_Estados_Antes = CL_Estados

                if CL_Estados == 0:	#Estado Inicial
                        Color('Azul',1)
                        Color('Azul',0)
                elif	CL_Estados == 3:	#Entrar
                        Color('Verde',1)
                        Color('Negro',0)
                elif	CL_Estados == 4:	#Salir
                        Color('Negro',1)
                        Color('Verde',0)
                elif	CL_Estados == 5:	#Sin Acceso
                        Color('Rojo',1)
                        Color('Rojo',0)
                elif	CL_Estados == 7:	#Usuario digita Rut sin internet
                        Color('Amarillo',1)
                        Color('Amarillo',0)
                elif	CL_Estados == 8:	#Usuario digita Rut con internet
                        Color('Blanco',1)
                        Color('Blanco',0)
                else :						#No definido
                        Color('Negro',1)
                        Color('Negro',0)
        else :
                if CL_Estados == 1:             #Lectura QR con internet
                        Blink_0('Amarillo',CL_D_Blink)
                        Blink_1('Amarillo',CL_D_Blink)
                elif	CL_Estados == 2:	#Lectura QR sin internet
                        Blink_0('Blanco',CL_D_Blink)
                        Blink_1('Blanco',CL_D_Blink)
                elif	CL_Estados == 6:	#Rut equibocado
                        Blink_0('Rojo',CL_D_Blink)
                        Blink_1('Rojo',CL_D_Blink)

#---------------------------------------------------------


Estado=0
Dato_Antes = 'b'
a = 'b'
print ('quue pasa')
Color('Azul',1)
Color('Amarillo',0)
time.sleep(15)

while (True):
        #Estado = 1 #pruebas
        time.sleep(0.05)
        Led_Estados(Estado)
        a=Leer(3)
        #print (a)
        if a != Dato_Antes :
                Dato_Antes = a
                #print (a)
                if(a =='0'):
                        Estado=0
                        a='b'
                        Borrar(3)
                elif(a =='1'):
                        Estado=1
                        a='b'
                        Borrar(3)
                elif(a =='2'):
                        Estado=3
                        a='b'
                        Borrar(3)
                elif(a =='3'):
                        Estado=3
                        a='b'
                        Borrar(3)
                elif(a =='4'):
                        Estado=4
                        a='b'
                        Borrar(3)
                elif(a =='5'):
                        Estado=5
                        a='b'
                        Borrar(3)
                elif(a =='6'):
                        Estado=6
                        a='b'
                        Borrar(3)
                elif(a =='7'):
                        Estado=7
                        a='b'
                        Borrar(3)
                elif(a =='8'):
                        Estado=8
                        a='b'
                        Borrar(3)
                elif(a =='9'):
                        Estado=9
                        a='b'
                        Borrar(3)
                else:
                        #Estado=9
                        a='b'
                        Borrar(3)
