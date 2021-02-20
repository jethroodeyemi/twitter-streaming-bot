import tweepy
#import schedule
import time
from PIL import Image, ImageDraw, ImageFont

def timer(days):
    img=Image.open('twitter.png')
    I1=ImageDraw.Draw(img)
    myFont=ImageFont.truetype('BERNHC.TTF',185)
    I1.text((258.25,386.99),str(days), font=myFont,fill=(0,137,72))
    img.save('twitter2.png')
    print(days)

    twitter_auth_keys = { 
        "consumer_key"        : "CNpeVrrmf57DOrWzETKpzwRA6",
        "consumer_secret"     : "yfypGXmBQ72QxPuMXFq7AcJ8hA9N8br1Pu7D9YRtlLVEABhyNr",
        "access_token"        : "1243164206481973249-1yoxu697UWVezOsU5q6CN1DImPpim6",
        "access_token_secret" : "qWgAV18xfNRfwqC6nkjLQSP5yOZx8KeZgoMT3HtOGrAZ2"
    }
 
    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)
 
    media = api.media_upload("twitter2.png")
    tweet = f"Days left till Buhari leaves Aso Rock: {days}"
    api.update_status(status=tweet, media_ids=[media.media_id])
    return

def main():
    days=829
    #schedule.every().day.at('09:04').do(timer)
    for i in range(1,829):
        timer(days-i)
        # schedule.every(1).minutes.do(timer,days-i)
        # schedule.run_pending()

        time.sleep(86400)

if __name__ == "__main__":
    main()
