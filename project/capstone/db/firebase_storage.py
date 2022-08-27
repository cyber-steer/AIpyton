import pyrebase
import json
from datetime import datetime

class firebase_storage():
    def __init__(self):
        with open("db/auth.json") as f:
            config = json.load(f)
        firebase = pyrebase.initialize_app(config)
        self.storage = firebase.storage()
    # unknown
    def img_insert(self, date):
        print("img_insert")
        year = date[:4]
        month = date[5:7]
        day = date[8:10]
        self.storage.child("club").child(year).child(month).child(day).child(date[11:19]).put('Unknown.jpg')
    def insert(self, q, send, receive):
        while True:
            print(f'1storage receive : {receive.is_set()}')
            if receive.is_set():
                print(f'2storage receive : {receive.is_set()}')
                file = q.get()
                self.img_insert(str(datetime.now()))
                print('storage upload')
                send.set()
                receive.clear()
