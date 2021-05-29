import tweepy
from pprint import pprint
import json
from dotenv import load_dotenv
import os
from google.cloud import secretmanager
from google.cloud import firestore
import hashlib
from typing import Dict


def access_secret_version(project_id, secret_id, version_id="latest"):
    client = secretmanager.SecretManagerServiceClient()
    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(name=name)


def secret_hash(secret_value):
    return hashlib.sha224(bytes(secret_value, "utf-8")).hexdigest()


def get_gcp_secrest(secret_id):
    project_id = 'neat-tempo-205717'
    return secret_hash(access_secret_version(project_id, secret_id))


def remove_nested_lists(d: dict):

    def is_nested_list(some_list):
        if list(filter(lambda x: isinstance(x, list), some_list)):
            return True
        else:
            return False

    for key in d.keys():
        if isinstance(d[key], list) and is_nested_list(d[key]):
            d[key] = []
        elif isinstance(d[key], Dict):
            remove_nested_lists(d[key])
        elif isinstance(d[key], list):
            for ix, elmt in enumerate(d[key]):
                if isinstance(elmt, Dict):
                    remove_nested_lists(d[key][ix])
    return d


def get_and_load_tweets(event=None, context=None):

    # PROJECT_ID = 'neat-tempo-205717'
    # get_gcp_secrest('access_token')

    load_dotenv()

    access_token = os.getenv('access_token')
    access_token_secret = os.getenv('access_token_secret')
    consumer_key = os.getenv('consumer_key')
    consumer_secret = os.getenv('consumer_secret')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = api.home_timeline(count=100)

    db = firestore.Client()
    batch = db.batch() # * https://firebase.google.com/docs/firestore/manage-data/transactions#batched-writes
    for status in public_tweets:
        j = remove_nested_lists(status._json)
        screen_name = j.get('user').get('screen_name')
        ref = db.collection(u'twitter-home-timeline').document('users').collection(screen_name).document(j.get('id_str'))
        batch.set(ref, j)
    batch.commit()
    return {}

    

if __name__ == '__main__':
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(os.getcwd(), 'load_tweets_to_gcp/datastore_user_creds.json')
    get_and_load_tweets(event=None, context=None)
