#!/usr/bin/python
# -*- coding: utf-8 -*-


import lib.Control_Web  as CW
"""
import socket
import fcntl
import struct
import commands
import time
"""
import time

import os

#----------------------------------------------
#                   definiciones
#----------------------------------------------

Resolver_Comando_Web    = CW.Resolver_Comando_Web

print 'ok listo'
while 1:
        time.sleep(2.05)
        """
        if os.path.exists('/home/pi/Firmware/db/Data/Tabla_Servidor45.txt'):
            print "Existe";
        else:
            print "No Existe";
        """
        #print os.path.exists('/home/pi/Firmware/db/Data/Tabla_Servidor.txt')
        Resolver_Comando_Web()
