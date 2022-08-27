import urllib.request

import pyrebase

firebaseConfig = {"apiKey": "AIzaSyBETK45cbP1g2ZYC03ras5UYys5fXAqV_4",
  "authDomain": "fir-course-edb8c.firebaseapp.com",
  # "databaseURL": "https://fir-course-edb8c.firebaseio.com",
  "databaseURL": "https://fir-course-edb8c-default-rtdb.firebaseio.com/",
  "projectId": "fir-course-edb8c",
  "storageBucket": "fir-course-edb8c.appspot.com",
  "messagingSenderId": "760960563313",
  "appId": "1:760960563313:web:eb3b145202888f8a3c83d0",
  "measurementId": "G-336MJ5MK72"}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()
# auth=firebase.auth()
storage=firebase.storage()

# Authentication
# Login
# email = input('Enter your email ')
# password = input("Enter your Password ")
# try:
#     auth.sign_in_with_email_and_password(email, password)
#     print("Successfully signed in!")
# except:
#     print("Inalid user or password. Try again")

# Signup
# email = input("Enter your email")
# password = input("Enter your password")
# confirmpass = input("Confirm password")
# if password == confirmpass:
#     try:
#         auth.create_user_with_email_and_password(email, password)
#         print("Success!")
#     except:
#         print("Email already exists")

# Storage
filename = input("Enter the name of the file you want to upload")
cloudfilename = input("Enter the name of the file on the cloud")
storage.child(cloudfilename).put(filename)
#
print(storage.child(cloudfilename).get_url(None))

# download
cloudfilename = input("Enter the name of the file you want to download")
storage.child(cloudfilename).download("","dummy.txt")

# reading file
# cloudfilename = input("Enter the name of the file you want to download")
# url = storage.child(cloudfilena me).get_url(None)
# f = urllib.request.urlopen(url).read()
# print(f)

# Database
# create
# data = {'age':32, 'address':"LA", 'employed':True, 'name':"Jane"}
# db.child("people").child("asdfghjk").set(data)
data = {'name':'설재혁', 'engname':'Seol', 'number':'201929196'}
db.child("person").push(data)
data = {'name':'손옥무', 'engname':'Son', 'number':'202159884 '}
db.child("person").push(data)
data = {'name':'김건우', 'engname':'Kim', 'number':'202163104'}
db.child("person").push(data)

# update
# db.child("people").child("asdfghjk").update({'name':'Jane'})

# people=db.child("people").get()
# for person in people.each():
#   if person.val()['name']=='Mark':
#     db.child("people").child(person.key()).update({'name':'Jane'})

# Delete
# db.child("people").child("person").remove()

# people=db.child("people").get()
# for person in people.each():
#   if person.val()['name']=='John Smith':
#     db.child("people").child(person.key()).child("age").remove()

# Read
# people = db.child("people").order_by_child("age").start_at(20).get()
# people = db.child("people").order_by_child("employed").equal_to(True).get().val()
# if len(people) != 0:
#   print("true")
# else:
#   print("false")