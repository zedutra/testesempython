import pyrebase

config = {
  "apiKey": "AIzaSyDxRy6v71CBnPaFda4tc9YcZ7IKmUnCpUg",
  "authDomain": "rfidufvjm.firebaseapp.com",
  "databaseURL": "https://rfidufvjm.firebaseio.com",
  "storageBucket": "rfidufvjm.appspot.com"
}

firebase = pyrebase.initialize_app(config)

nome = 'Guilherme'

db = firebase.database()
data = db.child("5b559379").child("nome").get()

if data == nome:
    print(data, "é lindo")
else:
    print("Você não é o Guilherme")

print(data.val())

