from testFuntion import*

db = testFuntion()
nameKey = db.set("aaaa")
print(db.get(nameKey["name"]))