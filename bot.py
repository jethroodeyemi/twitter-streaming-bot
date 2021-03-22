
import tweepy
import logging
from config import create_api
import json
import time
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.search,keywords,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")

            if not tweet.user.following:
                tweet.user.follow()

            api.update_status(
                status=f"Thanks for mentioning Wizkid in your tweet, this is an automatic reply. Follow the Wizkid FC Bot account for everything concerning Wizkid. IFB automatically. \n({datetime.today()})",
                in_reply_to_status_id=tweet.id,
                auto_populate_reply_metadata=True
            )
            time.sleep(600)
            # api.update_with_media('/image.jpg', status='message')
    return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["wizkid"], since_id)
        logger.info("Waiting...")
        time.sleep(10)

if __name__ == "__main__":
    main()
