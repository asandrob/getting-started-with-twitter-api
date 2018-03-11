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

message = "Hello world - here's picture!"

with open('twython-01.jpg', 'rb') as photo:
    twitter.update_status_with_media(status=message, media=photo)