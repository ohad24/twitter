import markovify
from get_tweets import get_tweets
import json

# # Get raw text as string.
with open("tweets.txt") as f:
    text = f.read()

# print('\n'.join(text))
# quit()

# sentences = get_tweets()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(10):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
# for i in range(3):
#     print(text_model.make_short_sentence(280))