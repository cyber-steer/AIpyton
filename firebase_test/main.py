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
# storage=firebase.storage()

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
# filename = input("Enter the name of the file you want to upload")
# cloudfilename = input("Enter the name of the file on the cloud")
# storage.child(cloudfilename).put(filename)
#
# print(storage.child(cloudfilename).get_url(None))

# download
# cloudfilename = input("Enter the name of the file you want to download")
# storage.child(cloudfilename).download("","downloaded.txt")

# reading file
# cloudfilename = input("Enter the name of the file you want to download")
# url = storage.child(cloudfilena me).get_url(None)
# f = urllib.request.urlopen(url).read()
# print(f)

# Database
data = {'age':32, 'address':"LA", 'employed':False, 'name':"John Smith"}
db.child("people").child("person").push(data)