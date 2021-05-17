#!/usr/bin/env python3
import sys, os

import numpy as np
from PIL import Image, ImageOps

# peripage imports
import ppa6
import time
import logging

import socket




def read_img(rdata):
    if not rdata:
        #raise ValueError('No data received')
        return False
    
    if peripage.isConnected():
        connected = True
        #logging.debug('Printer connected!')

        contrast = rdata[0]
        w = int.from_bytes(rdata[1:3], 'big')
        h = int.from_bytes(rdata[3:5], 'big')
        for n in range(int(len(rdata)/((w*h)+5))):
            peripage.setConcentration(contrast)
            #om = Image.frombytes('L',(w,h), rdata[5:])
            pos = n*((w*h)+5)
            om = Image.frombytes('L',(w,h), rdata[pos:])
            #om.save('test_'+str(n)+'.png')
            peripage.printImage(om)
            peripage.printBreak(break_l)
            time.sleep(pausa)
        #logging.debug('page processed') #debug
        return True
    else:
        #logging.debug('printer not connected') #debug
        return False
               
    


if __name__ == '__main__':
	
    #logging.basicConfig(filename='/tmp/peripage_bak.log', level=logging.DEBUG)
    #logging.basicConfig(filename='backend.log', level=logging.DEBUG)

    connected = False
    
    if len(sys.argv) == 1:
        print ('direct peri "Unknown" "Peripage thermal printer"')

    else:
        uri = os.getenv('DEVICE_URI')
        cupsprintername = os.getenv('PRINTER')
        sys.stderr.write('DEBUG: Peripage uri = ' + uri + '\n')
        sys.stderr.write('DEBUG: Peripage name = ' + cupsprintername + '\n')
        sys.stderr.flush()

        peripageType = ppa6.PrinterType.A6p
        timeout = 5.0
        pausa = 2.0
        mac = '02:03:04:59:34:FA'
        #mac = uri[7:]
        sys.stderr.write('DEBUG: Peripage MAC ADDRESS = ' + mac + '\n')
        sys.stderr.flush()
        contrast = 1
        break_l = 100

        peripage = ppa6.Printer(mac, peripageType, timeout)
        
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

        s.connect((mac, 1))
        s.settimeout(timeout)

        peripage.sock = s

        #peripage.connect()
        peripage.reset()
    
        sys.stderr.write('DEBUG: Peripage connected\n')
        sys.stderr.flush()
        
        #read_img(sys.stdin.buffer.read())
        
        
        while True:
            dati = sys.stdin.buffer.read()
            sys.stderr.write ('DEBUG: Peripage dati letti: '+str(len(dati)) + '\n')
            data = read_img(dati)
            if not data:
                break
