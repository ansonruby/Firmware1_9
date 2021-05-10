
import lib.Control_Archivos  as Ca
import time

import RPi.GPIO as GPIO #Libreria Python GPIO

Leer			= Ca.Leer_Estado
Borrar			= Ca.Borrar_Archivo


GPIO.setmode (GPIO.BOARD)
# configuracion de pines

        #chicharra
CC_Pin =  7 #38

GPIO.setup(CC_Pin, GPIO.OUT)

def sonido(i):

	for CT_m in range(i):
		GPIO.output(CC_Pin, GPIO.HIGH)
	GPIO.output(CC_Pin, GPIO.LOW)


#sonido(100000)



Dato_Antes = '0'
a = '0'
Archivo=6
Tiempo_sonido =500
contador=0

while (True):

        time.sleep(0.05)

        a=Leer(Archivo)
        #print (a)
        if a != Dato_Antes :
                Dato_Antes = a
                print (a)
                if(a =='0'):

                        a='b'
                        Borrar(Archivo)
                        sonido(Tiempo_sonido*1)
                elif(a =='1'):

                        a='b'
                        Borrar(Archivo)
                        sonido(Tiempo_sonido*2)
                elif(a =='2'):

                        a='b'
                        Borrar(Archivo)
                        sonido(Tiempo_sonido*3)
                else:
                        #Estado=9
                        a='b'
                        Borrar(Archivo)
        elif a!='b':
                contador+=1
                if contador>=10:
                        Dato_Antes='b'
                        contador=0
