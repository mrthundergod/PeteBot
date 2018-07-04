import tweepy as tp
import time
from credentials import *

def authenticTweePy():
# login to twitter account api
  auth = tp.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)
  api = tp.API(auth)
  return api

def followFollowers(api):
    for follower in tp.Cursor(api.followers).items():
      print("Attempting to follow my followers")
      follower.follow()


def theTweeter(api):
  for tweet in tp.Cursor(api.search, q='#AI').items(1):
    try:
        print('\nRetweet Bot found tweet by @' +tweet.user.screen_name + '. ' + 'Attempting to retweet.')

        tweet.retweet()
        print('Retweet published successfully.')

      # Some basic error handling. Will print out why retweet failed, into your terminal.
    except tp.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break

    #followFollowers(api)

    time.sleep(60)

if __name__=='__main__':
  api = authenticTweePy()
  theTweeter(api)

#    https://python-twitter.readthedocs.io/en/latest/twitter.html#module-twitter.api