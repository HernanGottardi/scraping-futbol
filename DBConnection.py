import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

# Cargar las credenciales desde la variable de entorno
# credentials_json = {
#     "type": "service_account",
#     "project_id": "dbfutbol-979f4",
#     "private_key_id": os.environ.get("PRIVATE_KEY_ID"),
#     "private_key": os.environ.get("PRIVATE_KEY").replace('\\n', '\n'),  # Reemplaza \n por saltos de línea reales
#     "client_email": os.environ.get("CLIENT_EMAIL"),
#     "client_id": os.environ.get("CLIENT_ID"),
#     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#     "token_uri": "https://oauth2.googleapis.com/token",
#     "auth_provider_x509_cert_url": os.environ.get("AUTH_PROVIDER_X509_CERT_URL"),
#     "client_x509_cert_url": os.environ.get("AUTH_PROVIDER_X509_CERT_URL")
# }

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


