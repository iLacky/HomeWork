import random
import requests

GOOGLE = "https://google.com"
FACEBOOK = "https://facebook.com"
TWITTER = "https://twitter.com"
AMAZON = "https://amazon.com"
APPLE = "https://apple.com"

seq = GOOGLE, FACEBOOK, TWITTER, AMAZON, APPLE
web = random.choice(seq)
print(web)
res = requests.get(web)
print(f'status code: {res.status_code}')
string = str(web)
print(f'length HTML code: {len(string)}')