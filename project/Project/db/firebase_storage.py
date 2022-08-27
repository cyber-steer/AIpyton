import pyrebase
import json

class firebase_storage():
    with open("db/auth.json") as f:
        config = json.load(f)
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    # unknown
    def img_insert(self, date):
        print("img_insert")
        print(date)
        year = date[:4]
        month = date[5:7]
        day = date[8:10]
        print("year :",year)
        print("month :",month)
        print("day :",day)
        print("file Name :",date[11:19])
        self.storage.child("club").child(year).child(month).child(day).child(date[11:19]).put("unknown.jpg")
