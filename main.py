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


def theRetweeter(api, search):
  for tweet in tp.Cursor(api.search, q=search).items(1):
    try:
        print('\nRetweet Bot found tweet by @' +tweet.user.screen_name + '. ' + 'Attempting to retweet.')

        tweet.retweet()
        print('Retweet published successfully.')

    except tp.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break

    #followFollowers(api)

    time.sleep(30)

def iterator(api):
    searchTerms=['#AI', '#ML', '#technology','#deeplearning','#machinelearning','#BigData','#IoT', '#artificialintelligence', '#robotics', '#internetofthings']
    for s in range(len(searchTerms)):
        theRetweeter(api, searchTerms[s])


if __name__=='__main__':
    api = authenticTweePy()
    for i in range(287):
      iterator(api)
    api.update_status(status="Reboot Pending")
