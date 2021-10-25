import random
import tweepy
from twitter_codes import *

#Yeah. I won't learn regex for this. Sorry lol.
keyword_arr = ["ideologie", "ideologický", "ideologická", "ideologické", "ideology", "ideological"]

#All of the Zizek gifs I found
zizeks_arr = [
    "https://media.giphy.com/media/r7bjWH3xADPZObjK0y/giphy.gif?cid=790b7611bb6319acdbfe384d3ed53a013a16c6a6dbbe2826&rid=giphy.gif&ct=g", 
    "https://media.giphy.com/media/12WLJVZoDpUrSg/giphy.gif?cid=790b7611bf2e2e68baf3c55247d0c882e79796e3859921a9&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/MtuaGCPQ95osM/giphy.gif?cid=790b76114952d3b81db19fad58e39355abc45e36e7d79c0d&rid=giphy.gif&ct=g",
    "https://tenor.com/WDs7.gif",
    "https://tenor.com/WFoV.gif",
    "https://tenor.com/WFoT.gif",
    "https://tenor.com/xLax.gif",
    "https://tenor.com/v0FK.gif",
    "https://tenor.com/bh6Ku.gif"
]

auth = tweepy.OAuthHandler(my_api_key, my_api_secret)
auth.set_access_token(my_access_token, my_access_token_sec)

api = tweepy.API(auth)



def search_for_tweets():
    pass

def auth_to_tw(): 

    retry_counter = 0

    while True: 
        if retry_counter < 4: #If it fails, just try it multiple times in order to be sure lol. 
            try: 
                api.verify_credentials()
                print("auth ok")
                break
            except:
                print("Auth error")
                retry_counter = ++retry_counter
        elif retry_counter > 4:
            print("Auth failed. There is problem with your code.")
            break

def test_tweeting():
    my_tweet = random.choice(zizeks_arr)
    api.update_status(my_tweet)


def run_it():
    auth_to_tw()
    test_tweeting()

run_it() 