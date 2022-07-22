import pyrebase
import json

class firebase_storage():
    with open("auth.json") as f:
        config = json.load(f)
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    # unknown
    def img_insert(self, date):
        year = date[:4]
        month = date[5:7]
        day = date[8:10]
        self.storage.child("club").child(year).child(month).child(day).put(date[11:19])
