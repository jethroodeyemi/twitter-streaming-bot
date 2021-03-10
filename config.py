import logging
import tweepy

logger = logging.getLogger()

def create_api():
    consumer_key = "AidDo5F5GIAV29AA6JllMMown"
    consumer_secret = "ssTbjY4WZSQgIPo0W5Iwwghng40MQqvfHMn3DPaxAxheqGgpKf"
    access_token = "1243164206481973249-z6SrtkjzjDHixIviYJdfV48rTlKBBB"
    access_token_secret = "5rp3DWr8TMRtHIepAfmrXKJ72QjMNW2WtDQ215ntdVOAO"

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
