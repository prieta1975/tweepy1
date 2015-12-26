from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import pandas as pd

#consumer key, consumer secret, access token, access secret.
ckey="QIqgjITOfksfMW4lRLDacQ"
csecret="R8x0xN9iSKXGNxUtGKA2hgnlIhh5INZIOdgEfxzk"
atoken="1401204486-BeLUAuruh294KeJX8NXvdqjCeZOQcLl6HWmMlgA"
asecret="pwjiLF42TbORaXtkCS5Oc24qywOU0eFN0esVcibA"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Madrid"])
