# Load Tweets to GCP

## Assets
### GCP secret manager
[GCP secrets docs and examples](https://codelabs.developers.google.com/codelabs/secret-manager-python#6)

### GCP firebase batched writes
https://firebase.google.com/docs/firestore/manage-data/transactions#batched-writes


## Setup
### Twitter keys
Create new `.env` file in `load_tweets_to_gcp` directory. You can copy from `load_tweets_to_gcp/env.example` file and fill it with your twitter keys.

### GCP datastore user key
create member in GCP and download the cred file into `load_tweets_to_gcp` and rename it to `datastore_user_creds.json`

## Deploy
`cd load_tweets_to_gcp` and run `./deploy.sh`
