#!/bin/bash

# export GOOGLE_FUNCTION_SOURCE=app.py
# --trigger-topic get_and_load_tweets_topic \
gcloud functions deploy get_and_load_tweets \
    --trigger-topic get_and_load_tweets_topic \
    --memory 128 \
    --set-env-vars GOOGLE_APPLICATION_CREDENTIALS=/workspace/datastore_user_creds.json \
    --runtime python39