import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import json

cred_Data = {
    "type": os.getenv("TYPE"),
    "project_id": os.getenv("PROJECT_ID"),
    "private_key_id": os.getenv("PRIVATE_KEY_ID"),
    "private_key": os.getenv("PRIVATE_KEY"),
    "client_email": os.getenv("CLIENT_EMAIL"),
    "client_id": os.getenv("CLIENT_ID"),
    "auth_uri": os.getenv("AUTH_URI"),
    "token_uri": os.getenv("TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_x509_CERT_URL"),
    "client_x509_cert_url": os.getenv("CLIENT_x509_CERT_URL")
}
print(cred_Data)
cred = credentials.Certificate({
    "type": os.getenv("TYPE"),
    "project_id": os.getenv("PROJECT_ID"),
    "private_key_id": os.getenv("PRIVATE_KEY_ID"),
    "private_key": os.getenv("PRIVATE_KEY").replace('\\n','\n'),
    "client_email": os.getenv("CLIENT_EMAIL"),
    "client_id": os.getenv("CLIENT_ID"),
    "auth_uri": os.getenv("AUTH_URI"),
    "token_uri": os.getenv("TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_x509_CERT_URL"),
    "client_x509_cert_url": os.getenv("CLIENT_x509_CERT_URL")
})
firebase_admin.initialize_app(cred)
db = firestore.client()

def collectData():
    doc_ref = db.collection('Data').document('messages')
    doc = doc_ref.get()
    if doc.exists:
        print(doc)
        return doc
    else:
        print('no doc')
        return ""