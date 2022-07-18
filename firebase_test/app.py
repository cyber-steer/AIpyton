import pyrebase
import json

with open("auth.json") as f:
    config = json.load(f)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

signin = {"id":"abcd", "password":"1234", "username":"nick"}
db.child("users").child("abcd").set(signin)