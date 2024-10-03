import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
from dotenv import load_dotenv
load_dotenv()

# Obtiene las variables de entorno
private_key_id = os.getenv('PRIVATE_KEY_ID') or os.getenv('FIREBASE_PRIVATE_KEY_ID')
client_email = os.getenv('CLIENT_EMAIL') or os.getenv('FIREBASE_CLIENT_EMAIL')
client_id = os.getenv('CLIENT_ID') or os.getenv('FIREBASE_CLIENT_ID')
auth_provider_x509_cert_url = os.getenv('AUTH_PROVIDER_X509_CERT_URL') or os.getenv('FIREBASE_AUTH_PROVIDER_X509_CERT_URL')

# credentials_json = {
#     "type": "service_account",
#     "project_id": "dbfutbol-979f4",
#     "private_key_id": private_key_id,
#     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC7M2EDrT2pDp3f\nd8hPkw0BRdkdAQ4ShuBSMJ15DPuOuLGcoiqldGBSXzg9OLwTYL/94Fv+iUDil1qF\nEs9gdLZFRuzZbuGaX9FrKo9PzgxUFeYhFnEN1vJ1TO/g4aCN11dGaDNJxDoZUjx0\nZKDTDaFzg0PKuwrRLXSbdNd4YUPNbNTk0zDq4u4WrQc8Hb7degpQDRDpnsATjoTw\n8tEWcWfDpavcc5vI0vwCscpp8qNcjknb4MMaDdAIdMMtAbVKH//tURhj1gYj8XJb\nNjtFfSu+5O3dvdiXSyaK5uCViNCHdxC1IjmFvyzDAmBcgKmipQcVOMCeYs0solzt\n1sMPesHJAgMBAAECggEADW7Yp5GjItI2cG5xPIqODJkVRRBKEPjGOIeeCS1uELX+\nosF9Q22oKskD6Vq8njxbUo2qtEdnlUrsly98G40MdkiqXsjm3fPBvImrinu75T3E\nC3xHhQl3UQUCEpZGNd9ttxLrmT/ANohw554/7x0jiH0zHGVTF6MGItCd1JjQK3mj\n7oAF1MXuEdhEy2T1P357bv3bbTaXzX5sYh+uKarMlOKgjhwfclTXHGGwGKB+XlQQ\nK/BhstT1OhCngx5IwEQ1QvXbG9wSPi4RUJacD3rKib83eJ4/5stYbg4w4qMU0j3G\n6C/JL+uEHI5114j8rIWCn6EWPmfO2gb3FeqEn8V2vQKBgQDzRLKB2TqvZte2MvbT\nzD6d3gCkKlREQGSSsMbc9szweYFeLao/H/tSeDWzyrjTNJi+mAn3Ov+M/tede5vZ\nHBqUolm+2xtcgvDgka1ERkKRk2hNZZ+w6UlEVaJgFgbwrCT5//UQl/vpJ5fZHNNo\nSob2LXgMCg3oYadmz6NCmFOAZQKBgQDE/30jrrf/xVStF5dSQPlJm5THRVbQCHHS\nifvX9g4j8A1VqIs/RDcNIjIjUNG0PXAe7FR0dlpK4Afyaaz1/k9ehLP7K7cM9hwn\nw6H/VaCWaWTocWIFtYiIdjQUO9hLUtEDJ0qd4y1tODq5qC0rRRT7HA31ErrPwyNK\n4bQJhSb7lQKBgGUUU1OuzjqZceIL1RF2GUKBPyT3TaI6W0+0Ujz383msEvvt34Jx\nKH1A45d8EUX44cq349QtWIfeT/ropH4WtliyCLZL1lefNLUq8qKeywQwCrO2GR9q\nH35cUqa4IFQaQxb5qnslm49qWybkWldIOEHL7Mib2OGIygTnG8ANCQ0dAoGAK445\ngtwsfnaIxESFBoCrHWUyveRMz24ujFhJwHP8qGF48Ul0kCZq7ZJz9271Dp7O3Wdv\nPNi2Gfvyhdxri3AQ6Fr62DvQGyOHEhulA6lQ+jCPSP1YqN58M3+/AAJDTlQfNk1H\nqCUEdDOMeGQAqKJ7gxGu3FKpzynb8cB5Z+lytwkCgYAA+GoBbX05RTmgsZ8oUFvB\nCfKdM+yRcy9qMVb5OdRnMfLq4LFVjuRNbFMTldRmexB3+PWL8DkG9u94NPiBxc24\nLMPNlvm4IcJl0rPocqL2fior2pnSwUu6fekHagjgz/jnjvsBQyTtTTzcR6gAQ0E6\nvHYg48zcGMCShpcpTHmZzw==\n-----END PRIVATE KEY-----\n",
#     "client_email": client_email,
#     "client_id": os.getenv('CLIENT_ID'),
#     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#     "token_uri": "https://oauth2.googleapis.com/token",
#     "auth_provider_x509_cert_url": auth_provider_x509_cert_url,
#     "client_x509_cert_url": auth_provider_x509_cert_url,
# }

# Crear las credenciales desde el diccionario
cred = credentials.Certificate("./creden.json")

# Inicializar la aplicación Firebase
firebase = firebase_admin.initialize_app(cred)
db = firestore.client()

# def iniciar

def getAllDocuments():
    docs = db.collection("Entorno").stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}\n\n")

def addDocument(newNameDoc, objValor):
    doc_ref = db.collection("Entorno").document(newNameDoc)
    doc_ref.set(objValor)

def deleteAllDocuments():
    docs = db.collection("Entorno").list_documents()
    for doc in docs:
        doc.delete()
    
    db.collection("Entorno").document("init").set({"mensaje": "Colección recreada"})


