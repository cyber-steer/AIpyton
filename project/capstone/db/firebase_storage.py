import os

import pyrebase
import json
from datetime import datetime

class firebase_storage():
    def __init__(self, path='db/auth.json'):
        with open(path) as f:
            config = json.load(f)
        firebase = pyrebase.initialize_app(config)
        self.storage = firebase.storage()
    # unknown
    def img_insert(self, date):
        year = date[:4]
        month = date[5:7]
        day = date[8:10]
        self.storage.child("club").child(year).child(month).child(day).child(date[11:19]).put('Unknown.jpg')
    def insert(self, q, send, receive):
        while True:
            if receive.is_set():
                file = q.get()
                self.img_insert(str(datetime.now()))
                send.set()
                receive.clear()
    def update(self,q, e):
        while True:
            log = q.get()
            for key, value in log.items():
                if key == 'insert':
                    self.download(value)
                elif key == 'delete':
                    self.deletefile(value)

            if q.empty():
                e.set()
    def download(self, number, path='registered/'):
        cloud_path = 'registered/' + str(number)
        local_path = path + str(number) +'.jpg'
        self.storage.child(cloud_path).download("", local_path)
    def deletefile(self, number, path='registered/'):
        path = path + str(number) +'.jpg'
        try:
            os.remove(path)
        except:
            print(f'FileNotFoundError : {path}')
if __name__ =='__main__':
    storage = firebase_storage(path='../db/auth.json')
    storage.download(number=3, path='../registered/')