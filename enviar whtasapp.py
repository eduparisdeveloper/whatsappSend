# Importamos el Módulo

import pywhatkit as py
import time

#Usamos Un try-except

try:
    #enviamos el mensaje
    py.sendwhatmsg("+34 number","Esto es un mensaje automatizado",0,2)
    print("Mensaje Enviado")

except:
    time.sleep(10);
    print("Ocurrio un error")
    