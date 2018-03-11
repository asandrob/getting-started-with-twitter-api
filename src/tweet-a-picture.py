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

message = "Python is awesome!"

photo = open('./assets/i-love-python.jpg', 'rb')

response = twitter.upload_media(media=photo)

twitter.update_status(status=message, media_ids=[response['media_id']])