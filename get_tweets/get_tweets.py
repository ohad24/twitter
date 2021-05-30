from pprint import pprint
from dotenv import load_dotenv
from google.cloud import firestore
import os

db = firestore.Client()

users = [u'YinonMagal', u'netanyahu']

for user in users:
    print(user)
    docs = db.collection(u'twitter-home-timeline').document(u'users').collection(user).stream()
    for doc in docs:
        d = doc.to_dict()
        print(f'{doc.id} => {doc.to_dict().get("text")}')
