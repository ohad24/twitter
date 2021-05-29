from pprint import pprint
from dotenv import load_dotenv
from google.cloud import firestore
import os

db = firestore.Client()

docs = db.collection(u'twitter-home-timeline').where(u'user.screen_name', u'==', u'netanyahu').stream()

for doc in docs:
    d = doc.to_dict()
    print(f'{doc.id} => {doc.to_dict().get("text")}')