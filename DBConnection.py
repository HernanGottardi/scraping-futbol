import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Crear las credenciales desde el diccionario
cred = credentials.Certificate("./dbfutbol-979f4-firebase-adminsdk-59xgr-6c6799f9ca.json")

# Inicializar la aplicación Firebase
firebase = firebase_admin.initialize_app(cred)
db = firestore.client()

def getAllDocuments():
    docs = db.collection("Entorno").stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}\n\n")

def getDocument():

    doc_ref = db.collection("Entorno").document("1")
    doc = doc_ref.get()

    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("No such document!")

def addDocumentEjemplo():
    doc_ref = db.collection("Entorno").document("2")
    doc_ref.set({"nombre": "Jesabel"})

def addDocument(newNameDoc, objValor):
    doc_ref = db.collection("Entorno").document(newNameDoc)
    doc_ref.set(objValor)

def deleteAllDocuments():
    docs = db.collection("Entorno").list_documents()
    for doc in docs:
        doc.delete()
    
    db.collection("Entorno").document("init").set({"mensaje": "Colección recreada"})


