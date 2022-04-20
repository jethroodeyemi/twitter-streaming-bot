import logging
import tweepy

logger = logging.getLogger()

def create_api():
    consumer_key = "8XHm6fVwUMco0oYE19fGMmVWL"
    consumer_secret = "zW5hYwC7tCM2sKFxCqZ98ula8cFKxiODuzFg6qwohOsPhjBpP2"
    access_token = "1243164206481973249-k2p5hsyLMb7NLK6UfHPSkDGm9FWNiu"
    access_token_secret = "SVDdEbqESmwWoLgCB9rec8BLpYMTZMymdhqhUAvpAucx4"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
