import commands
import sys
import time

from crontab import CronTab

#import lib.Control_Archivos2  as Ca
import lib.Control_Archivos  as Ca
import lib.Control_Automatico  as Cu

#-----------------------------------
#           Definiciones
#-----------------------------------

Leer                    = Ca.Leer_Led
Borrar                  = Ca.Borrar_Archivo
Escrivir_Estados        = Ca.Escrivir_Estados
Escrivir                = Ca.Escrivir_Archivo
Leer_Estado             = Ca.Leer_Estado
Leer_Archivo            = Ca.Leer_Archivo
Generar                 = Ca.Generar_ID_Tarjeta

Crear_Trabajo           = Cu.Crear_Trabajo
Eliminar_Trabajo        = Cu.Eliminar_Trabajo
Activar_Trabajo         = Cu.Activar_Trabajo
Desactivar_Trabajo      = Cu.Desactivar_Trabajo

Desactivar_Trabajos     = Cu.Desactivar_Trabajos
Activar_Trabajos        = Cu.Activar_Trabajos
Adicionar_Trabajos      = Cu.Adicionar_Trabajos
Eliminar_Trabajos       = Cu.Eliminar_Trabajos


def Log_Actualizador(Dato):
    print Dato
    Escrivir(Dato,19)



print 'Soy el guardian'

while 1:
    time.sleep(2.05)

    print Leer_Estado(20) # Estado Actualizador

    #if Leer_Estado(20) == '0':
    #    print 'no hay actualizaciones pendientes'
    if Leer_Estado(20) == '1': # inicio de actualizacion primeros pasos
        print 'actualizacion pendiente'

        Log_Actualizador('0. Preparando actualizacion.')
        Log_Actualizador('0.1 Detener Firmware Actual.')
        res16 = Leer_Archivo(16)
        Desactivar_Trabajos(res16)
        Log_Actualizador('0.2 Activar vista Actualizacion.')
        Activar_Trabajo('Actualizador')
        Log_Actualizador('0.3 Activar proceso Actualizacion.')
        Activar_Trabajo('Proceso_Actualizar')

        Log_Actualizador('0.4 Reiniciando el Dispostivo.')
        Borrar(20)              # Borrar QR
        Escrivir_Estados('2',20)   # Guardar QR
        commands.getoutput('sudo reboot')
    if Leer_Estado(20) == '2':
        print 'Actualizando El dispostivo'
    if Leer_Estado(20) == '3':
        print 'Fin de Actualizar el dispostivo'
    if Leer_Estado(20) == '4':
        print 'Error en la actualizacion'

        res16 = Leer_Archivo(16)
        Activar_Trabajos(res16)
        Desactivar_Trabajo('Actualizador')
        #Log_Actualizador('0.3 Activar proceso Actualizacion.')
        Desactivar_Trabajo('Proceso_Actualizar')
        Borrar(20)              # Borrar QR
        Escrivir_Estados('5',20)   # Guardar QR
        commands.getoutput('sudo reboot')

    if Leer_Estado(20) == '0':
        print 'no hay actualizaciones pendientes'
        print 'revizar otras cosas.'

        Formware = Leer_Archivo(29)
        Firm = Formware.split('\n')
        #print Firm[0].find("Firmware1_8")
        if Firm[0].find("Firmware1_8") != -1:
            print 'firmware de instalacion tiempo sin ejcutar el sh'
            Tiem_de_activo = commands.getoutput('uptime -p')
            if Tiem_de_activo.find(",") != -1:
                Te = Tiem_de_activo.split(',')
                print Te[0]
                print Te[1]
                if Te[0].find("hours") != -1:

                    apache2 = commands.getoutput('which apache2')
                    php = commands.getoutput('which php')
                    mysql = commands.getoutput('which mysql')
                    print apache2

                    if len(apache2)>3 and len(php)>3 and len(mysql)>3:
                        print 'Ya esta instalado todo'
                        Borrar(47)              #
                        Escrivir_Estados('OK',47)   # Estado final de la instalacion
                    elif len(apache2) == 0 or len(php) == 0 or len(mysql) == 0:
                        print 'NO hay nada Instalado reiniciar'
                        commands.getoutput('sudo reboot')

            else:
                print Tiem_de_activo
                Te = Tiem_de_activo.split(' ')
                print 'separando que pasa'
                print Te[0]
                print Te[1]
                print Te[2]
                if int(Te[1]) >=15:
                    print 'revisar y reiniciar proque no se instalo'
                    apache2 = commands.getoutput('which apache2')
                    php = commands.getoutput('which php')
                    mysql = commands.getoutput('which mysql')
                    print apache2

                    if len(apache2)>3 and len(php)>3 and len(mysql)>3:
                        print 'Ya esta instalado todo'
                        Borrar(47)              #
                        Escrivir_Estados('OK',47)   # Estado final de la instalacion
                    elif len(apache2) == 0 or len(php) == 0 or len(mysql) == 0:
                        print 'NO hay nada Instalado reiniciar'
                        commands.getoutput('sudo reboot')



        res = commands.getoutput('if test -f /home/pi/Firmware/Web/Install/P.sh; then echo "OK"; else echo "NO"; fi')
        if res == 'OK':
            print 'revizar si ya esta configurado';

            apache2 = commands.getoutput('which apache2')
            php = commands.getoutput('which php')
            mysql = commands.getoutput('which mysql')

            if len(apache2)>3 and len(php)>3 and len(mysql)>3:
                print 'Ya esta instalado todo'
                Borrar(47)              #
                Escrivir_Estados('OK',47)   # Estado final de la instalacion
            elif len(apache2) == 0 and len(php) == 0 and len(mysql) == 0:
                print 'NO hay nada Instalado'

                res = commands.getoutput('stat -c "%a" /home/pi/Firmware/Web/Install/P.sh')
                print res
                if res != "755":
                    print 'colocar permisos';
                    res = commands.getoutput('chmod -R 755 /home/pi/Firmware/Web/Install/P.sh')

                res = commands.getoutput('stat -c "%a" /home/pi/Firmware/Web/Install/P.sh')
                if res == "755":
                    print 'ejecutar sh';
                    Borrar(47)              #
                    Escrivir_Estados('INS',47)   # Estado final de la instalacion
                    res = commands.getoutput('/home/pi/Firmware/Web/Install/P.sh')
                    print res
                    Borrar(47)              #
                    Escrivir_Estados('OK',47)   # Estado final de la instalacion
                    commands.getoutput('sudo chgrp www-data /var/www/html')
                    commands.getoutput('sudo usermod -a -G www-data pi')
                    commands.getoutput('sudo chmod -R 775 /var/www/html')
                    commands.getoutput('sudo chmod -R g+s /var/www/html')
                    commands.getoutput('sudo chown -R pi /var/www/html')
                    commands.getoutput('sudo reboot')



            else:
                print 'Error de la web.'
        else:
            print 'no hacer nada';



    #res = commands.getoutput('chmod -R 755 /home/pi/Firmware/sh/'+c)
"""
0. berificar si esta intalado apache2 mysql y php  si no ejecutamos el intaldor

1. dar permisos al sh de intalacion Firmware

"""


"""
# ------------------------------
#           Constantes
# ------------------------------
MAC_DIRC        = 'cat /sys/class/net/eth0/address'
MAC_DIRC        = 'cat /sys/class/net/wlan0/address'
MAC             = commands.getoutput(MAC_DIRC)
MAC             = MAC.replace(":","")
ID_Tarjeta      = Generar(MAC)
#ID_Tarjeta      = ID_Tarjeta +'5'
# para Clonar repositorios
Direccion_Clonada           = ' /home/pi/Actualizador/'
Nombre_Carpeta_clonada      = 'Nueva_Actualizacion'
Direccion_Firmware          = ' /home/pi/'
Nombre_Carpeta_Firmware     = 'Prueba_Firmware'

#print ID_Tarjeta       #ID tarjeta mejorar que quede una sola peticion
# ejemplo de comandos
#res2 = commands.getoutput('ifconfig')
#print res2

# ------------------------------
#       Funciones
# ------------------------------

def Verificar_Actualizacion (Arc):

    lineas =Arc.split("\n")     #separador

    for linea in range(len(lineas)):
        c = lineas[linea]
        print c
        if linea == 0 :
            if ID_Tarjeta !=  c :
                print 'NO es para mi'
                return '0'
        if linea == 1 :
            C =str(Leer_Archivo(17))
            if C.find(c) != -1 :
                print 'ya esta actualizado'
                return '0'
        if linea == 2 :
            print 'Devo actualizar'
            return c


def Log_Actualizador(Dato):
    print Dato
    Escrivir(Dato,19)

# ------------------------------
#       Funcion principal
# ------------------------------

#-----  simulacion de respuesta de Actualizacion

# -2. peticion de actualizacion:
# datos de envio del dispostivo al servidor para actualizacion:
# ID_Dispostivo, Vercion_actual_firware.
# guardar el resultado en el archivo 15
# respuesta de la peticion

# 0 -> volver a activar procesos
# 1 -> Actualizar
prueba_1= 1

Arc = Leer_Archivo(15)

#-1.  verificar respuesta:
print '-1. Verificar Actualizacion'
Resp = Verificar_Actualizacion(Arc)

Resp = '1'

if Resp != '0':

    # my_cron = CronTab(user = 'pi')
    Borrar(19) # borrado de memoria del proceso de actulaizacion OJO "solo pro pruebas"
    # Desactivar_Trabajo("Chicharra")
    # revicion de bd si hay infomacion sin procesar para guardar y limpiar

    if prueba_1 == 1:
        Log_Actualizador('0. Preparando actualizacion.')
        Log_Actualizador('0.1 Detener Firmware Actual.')
        res16 = Leer_Archivo(16)
        Desactivar_Trabajos(res16)
        Log_Actualizador('0.2 Activar vista Actualizacion.')
        Activar_Trabajo('Actualizador')
        Log_Actualizador('0.3 Activar proceso Actualizacion.')
        Activar_Trabajo('Proceso_Actualizar')

        Log_Actualizador('0.4 Reiniciando el Dispostivo.')
        #commands.getoutput('sudo reboot')
    else:
        res16 = Leer_Archivo(16)
        Activar_Trabajos(res16)
        Desactivar_Trabajo('Actualizador')
        Desactivar_Trabajo('Proceso_Actualizar')
        #commands.getoutput('sudo reboot')


"""
