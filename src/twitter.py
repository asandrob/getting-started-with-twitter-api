import random
from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

messages = [
    "Olá Twython!!",
    "Olha eu aqui",
    "Qual é a boa?",
    "Como vão as coisas?",
    "Você já esteve aqui antes?",
    "Vá cortar o seu cabelo!"
]

message = random.choice(messages)
twitter.update_status(status=message)
print("Tweeted: %s" % message)