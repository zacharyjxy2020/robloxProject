import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('credentials.json')
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