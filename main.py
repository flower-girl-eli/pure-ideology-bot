import tweepy
from twitter_codes import *

auth = tweepy.OAuthHandler(my_api_key, my_api_secret)
auth.set_access_token(my_access_token, my_access_token_sec)

api = tweepy.API(auth)
retry_counter = 0
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
        