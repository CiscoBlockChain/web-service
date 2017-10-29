from flask import Flask
import requests
import json
import time

class JsonF():
    payload = open("urls.json").read()
    urls = json.loads(payload)

jsonF = JsonF()    
app = Flask(__name__)
   
@app.route("/urls")
def default():
    while True:
#        payload = open("urls.json").read()
#        urls = json.loads(payload)
        for link in jsonF.urls["urls"]:
            requests.post(url=link, data=jsonF.payload)
        return jsonF.payload
    time.sleep(5)
    
if __name__ == '__main__': 
    app.run(port=5050, debug = True)