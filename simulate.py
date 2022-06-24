#!/usr/bin/env python

import hashlib
from hashlib import sha256
import time
import struct
import binascii
import datetime
from binascii import unhexlify, hexlify
from dateutil import parser
from datetime import datetime
from datetime import timedelta 

nontrouve = True
now = datetime.now()
inonc = 4107802134 - 2500 #Starting 2500 before the good nonce

resultat = []

version    = '1'
prevblock  = '000000000000000000078908d256fa7a9f97b2e1ea532fb1ce45ee4bf050d221'
merkleroot = 'c504fc3a406f11c7c5b598da7f50916f4e298041e6f9b91535a80db113af109a'
time       = '1614006862'  # 2021-02-22 15:14:22 GMT +1
bits       = '170cf4e3'
nonce      = '4107801734'
print("Mining Simulator")
input()

print("""
1. Get Transactions
-------------------
transactions: 1343
""")
input()

print("""
2. Block
--------""")
print("Version : " + version+'\n'+"Prevblock : " + prevblock+'\n'+"Merkleroot : "+merkleroot+'\n'+"Time : 2021-02-22 15:14:22 GMT +1"+'\n'+"Bits : "+bits+'\n'+"Nonce : "+nonce)

input()

print("""
3. Target
--------""")
print("00000000FFFF0000000000000000000000000000000000000000000000000000")
input()


while(nontrouve):
    inonc +=1
    if(inonc%50==0):
        print(str(round(timedelta(seconds=1)/(datetime.now() - now))) + ' H/s')
    now = datetime.now()
    header_hex = (binascii.hexlify(struct.Struct('<L').pack(int('0x2fffe000',16))).decode()  + 
     binascii.hexlify(binascii.unhexlify('000000000000000000078908d256fa7a9f97b2e1ea532fb1ce45ee4bf050d221')[::-1]).decode()+
     binascii.hexlify(binascii.unhexlify('c504fc3a406f11c7c5b598da7f50916f4e298041e6f9b91535a80db113af109a')[::-1]).decode() +
     binascii.hexlify(struct.Struct('<L').pack(int(hex(int(parser.parse('2021-02-22 15:14:22 GMT +1').timestamp())-3600),16))).decode() +
     binascii.hexlify(struct.Struct('<L').pack(int("0x170cf4e3",16))).decode() + 
     binascii.hexlify(struct.Struct('<L').pack(int(hex(inonc),16))).decode()) 
    header_bin = unhexlify(header_hex)
    dt1 = datetime.now().strftime("%H:%M:%S.%f")
    hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
    hexlify(hash).decode("utf-8")
    hexlify(hash[::-1]).decode("utf-8")
    hash=hexlify(hash[::-1]).decode("utf-8") 
    resultat.append([round(int(hash,16)/10**65)])
    MAX_TARGET = int("00000000FFFF0000000000000000000000000000000000000000000000000000", 16)           
    Difficulty = 21724134900047.27                     
    target = int(MAX_TARGET / Difficulty)
    target32 = '{:0>64x}'.format(target)    
    if(int(hash,16) < int(target32,16)):
        print('\n'+'###########BLOC MINED###################')
        print('HEADER= ' + header_hex)
        print('HASH= ' + hash)
        print('NONCE= ' + str(inonc))
        print('NONCE (hex)= ' + hex(inonc))
        print('###########BLOC MINED###################')
        break
