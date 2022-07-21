import pyrebase
import datetime

class testFuntion():
    delay = 10
    last_person = None
    firebaseConfig = {"apiKey": "AIzaSyBETK45cbP1g2ZYC03ras5UYys5fXAqV_4",
                      "authDomain": "fir-course-edb8c.firebaseapp.com",
                      # "databaseURL": "https://fir-course-edb8c.firebaseio.com",
                      "databaseURL": "https://fir-course-edb8c-default-rtdb.firebaseio.com/",
                      "projectId": "fir-course-edb8c",
                      "storageBucket": "fir-course-edb8c.appspot.com",
                      "messagingSenderId": "760960563313",
                      "appId": "1:760960563313:web:eb3b145202888f8a3c83d0",
                      "measurementId": "G-336MJ5MK72"}

    firebase = pyrebase.initialize_app(firebaseConfig)
    db=firebase.database()

    def __init__(self, delay = 5):
        self.delay = delay

    def get(self, key):
        return self.db.child("club").child(key).get().val()
    def set(self, name):
        date = str(datetime.datetime.now())
        data = {name:date}
        year = date[:4]
        month = date[5:7]
        day = date[8:10]
        if self.cooldowncheck(name):
            self.last_person = data
        # self.cooldownadd(data)
        self.db.child("club").child(year).child(month).child(day).push(data)
        self.cooldowncheck(name)
        print(self.last_person)
        return (name, date)
    def cooldownadd(self, data):
        pass
        # for key, val in data.items():
        #     self.cooldownlist[key] = val
    def cooldowncheck(self, name): # 마지막과 동일하면 False DB저장하려면 True
        if self.last_person == None:
            return True
        else:
            for key, val in self.last_person.items():
                key =key
                val =val
            now = datetime.datetime.now()
            date = val
            year = int(date[:4])
            month = int(date[5:7])
            day = int(date[8:10])
            hour = int(date[11:13])
            minute = int(date[14:16])
            second = int(date[17:19])
            date = datetime.datetime(year, month, day, hour, minute, second)
            difference = (now - date).seconds
            if difference > self.delay:
                return True
            else:
                return False
        print("error")
        # else if name == :
        #     date = self.cooldownlist[name]
        #     year = int(date[:4])
        #     month = int(date[5:7])
        #     day = int(date[8:10])
        #     hour = int(date[11:13])
        #     minute = int(date[14:16])
        #     second = int(date[17:19])
        #     date = datetime.datetime(year, month, day, hour, minute, second)
        #     difference = (now - date).seconds
        #     if difference > 30:
        #         return
        #     else:
        #         return False
    def cooldownprint(self):
        # print(self.cooldownlist)
        pass