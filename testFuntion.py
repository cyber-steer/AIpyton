import pyrebase

class testFuntion():
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

    def testMethod(self):
        return self.db.child("name").get().val()
