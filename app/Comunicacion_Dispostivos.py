
# 'scp pi@192.168.1.127:/home/pi/Hola.txt /home/pi/Hola.txt'
#a = scp.get('/home/pi/Comunicacion/Hola.txt','/home/pi/Hola.txt')
#PUT_Dispostivos('/home/pi/Comunicacion/Hola.txt','/home/pi/Hola.txt')
#print PUT_Dispostivo('192.168.1.127','/home/pi/Comunicacion/Hola.txt','/home/pi/Hola.txt')
#print GET_Dispostivo('192.168.1.127','/home/pi/Hola2.txt','/home/pi/Hola2.txt')


# sudo apt-get update
# sudo apt-get install python-scp # instalacion de  scp y paramiko

# posiblenete para escaner la red en busca de dispsotivos
# sudo apt-get install sshpass
# sudo apt-get install nmap



import lib.Control_Archivos
import time
import paramiko
from scp import SCPClient

# definiciones  -----------------

Leer_Archivo            = lib.Control_Archivos.Leer_Archivo
Leer_Estado             = lib.Control_Archivos.Leer_Estado
Borrar                  = lib.Control_Archivos.Borrar_Archivo
Escrivir_Estados        = lib.Control_Archivos.Escrivir_Estados
ID                      = lib.Control_Archivos.ID
Estado_Usuario 	        = lib.Control_Archivos.Estado_Usuario
Escrivir_Enviar         = lib.Control_Archivos.Escrivir_Enviar
Escrivir                = lib.Control_Archivos.Escrivir
Escrivir_nuevo          = lib.Control_Archivos.Escrivir_nuevo
Leer                    = lib.Control_Archivos.Leer
Escrivir_Archivo        = lib.Control_Archivos.Escrivir_Archivo



Usuario = 'pi'
Password = "fusepong2019"
Reposo = 5.05
Estado = 0 # estado inicial en ivernacion

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client


def PUT_Dispostivo (IP_Destino, Archivo_Local,  Archivo_Destino):

    global Usuario
    global Password

    Respuesta ='NO'
    print 'hola'
    ssh = createSSHClient(IP_Destino, 22,Usuario,Password)
    scp = SCPClient(ssh.get_transport())

    try :
        Respuesta = scp.put(Archivo_Local,Archivo_Destino)
        scp.close()
        return Respuesta

    except:
        scp.close()
        return Respuesta


def GET_Dispostivo (IP_Destino, Archivo_Local,  Archivo_Destino):

    global Usuario
    global Password

    Respuesta ='NO'
    ssh = createSSHClient(IP_Destino, 22,Usuario,Password)
    scp = SCPClient(ssh.get_transport())
    try :
        Respuesta = scp.get(Archivo_Local,Archivo_Destino)
        scp.close()
        return Respuesta

    except:
        scp.close()
        return Respuesta

def PUT_Dispostivos (Archivo_Local, Archivo_Destino):

    IP_Dispositivos = Leer_Archivo(21)
    s2 =IP_Dispositivos.split('\n')
    print len(s2)
    for IP_dis in s2:
        print IP_dis
        if len(IP_dis) >= 3:
            Respuesta = PUT_Dispostivo(IP_dis,Archivo_Local,Archivo_Destino)
            print Respuesta


def PUT_Autorizaciones():

    PUT_Dispostivos(lib.Control_Archivos2.N_A_Tx_Dispo,lib.Control_Archivos2.N_A_Rx_Dispo)
    #verificar que se transmitio...


   	#---------------------------------------------------------
	#----						    ------
	#----				 Programa principal ------
	#----						    ------
	#---------------------------------------------------------


#PUT_Autorizaciones()
print 'listo para comunicacion'

while 1 :


    time.sleep(Reposo)

    #------------------------------
    #   Avilitar procesos de actualizacion dispsotivos locales
    #------------------------------

    IP_Dispositivos = Leer_Archivo(21)
    if len(IP_Dispositivos) >= 3:
        Reposo = 0.05
        #print 'Avilitado'

        Estado = 1
    else:
        Reposo = 5.05
        Borrar(22) # borrar datos que no se nesesita por precausion
        Borrar(23) # Tx
        Borrar(24) # Rx
        print 'Ivernando'

        Estado = 0


    if Estado == 1:
        #------------------------------
        #       proceso TX de Actualizacion dispostivos red local
        #------------------------------

        TX_Pendiente = Leer_Archivo(22) #hay autorizaciones pendientes
        if len(TX_Pendiente) >= 5:
            Borrar(22)
            #TX_Pendiente = TX_Pendiente.replace("\n","")
            TX_Pendiente = TX_Pendiente.rstrip("\n")
            print TX_Pendiente
            Escrivir_Archivo(TX_Pendiente, 23) # Gardar en TX para trasmitir
            PUT_Autorizaciones()
            Borrar(23)
            print 'Listo TX de nuevo'

        #------------------------------
        #       proceso RX de Actualizacion dispostivos red local
        #------------------------------

        RX_Pendiente = Leer_Archivo(24) #hay autorizaciones pendientes
        if len(RX_Pendiente) >= 5:
            Borrar(24)
            RX_Pendiente = RX_Pendiente.rstrip("\n")
            print RX_Pendiente
            Escrivir_Archivo(RX_Pendiente, 1) # Guardar en Tabla_lector
            print 'Listo RX de nuevo'
