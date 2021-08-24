import tweepy
from twitter_codes import *

auth = tweepy.OAuthHandler(my_api_key, my_api_secret)
auth.set_access_token(my_access_token, my_access_token_sec)

api = tweepy.API(auth)
retry_counter = 0

#Yeah. I won't learn regex for this. Sorry lol.
keyword_arr = ["ideologie", "ideologický", "ideologická", "ideologické"]

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

def search_for_tweets():
    pass

while True: 
    if retry_counter < 4: #If it fails, just try it multiple times in order to be sure lol. 
        try: 
            api.verify_credentials()
            print("auth ok")
            allGood = True #this code is shit lol
        except:
            print("Auth error")
            allGood = False

        if allGood == True:
            
            while True: 
                pass


            break
        elif allGood == False: 
            retry_counter = retry_counter + 1 
            continue
    else: 
        print("Yeah, the code is f-ed. Sorry, but you need to rewrite it.")
        break
        