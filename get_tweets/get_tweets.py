from pprint import pprint
from dotenv import load_dotenv
from google.cloud import firestore
import os
import json
import re


def sensitize(tweet:str) -> str:
    tweet = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', tweet)
    tweet = re.sub(r'\@(\w)*', '', tweet)
    tweet = re.sub(r'(\(|\))', '', tweet)
    tweet = re.sub(r'RT : ', '', tweet)
    tweet = re.sub(r'\#(\w)*', '', tweet)
    tweet = re.sub(r'\s{1,}', ' ', tweet)
    tweet = re.sub(r'\n', ' ', tweet)
    return tweet


def get_tweets() -> list:
    db = firestore.Client()
    users = [u'YinonMagal', u'netanyahu', 'Riklin10', 'shlomo_karhi', 'bezalelsm', 'Shutup100000', 'TopazLuk', 'itamarbengvir', '@ronitlev12']
    # users = [u'YinonMagal', u'Riklin10']
    sentences = []
    for user in users:
        # print(user)
        docs = db.collection(u'twitter-home-timeline').document(u'users').collection(user).stream()
        for doc in docs:
            d = doc.to_dict()
            sentence = sensitize(d.get("text"))
            # sentence = re.sub(r'https?:\/\/.*[\r\n]*', '', sentence)
            # sentence = re.sub(r'@?:\/\/.*[\r\n]*', '', sentence)
            # print(f'{doc.id} => {sentence}')
            sentences.append(sentence)
        # quit()
    return sentences


if __name__ == '__main__':
    sentences = get_tweets()
    print(len(sentences))
    with open('tweets.txt', 'w') as f:
        # f.write(json.dumps(sentences, indent=4, default=str, ensure_ascii=False))
        map(lambda i:f.write(i), sentences)
