import tweepy

#NPG class deals with all housekeeping for creating instances.
class Tweet:
    #My Twitter consumer key
    consumer_key='3CbMubgpZvqbSEaXXXXXXXXXX'
    #My consumer secret
    consumer_secret='Clua2xLNfvbjj3Zoi4BQUXXXXXXXXXXEa5jOHeeC5MtGDt9HSwX'
    #My access token
    access_token='153952894-cPurjdaQW7bAXXXXXXXXXXXXXFNWmpev4N9nHWfAbs'
    #My access token secret
    access_token_secret='r6NJ6qjPrYDenqwuHaopXXXXXXXXXXXsrarhZ3IM4SQ'

    def __init__(self):
            self.auth = tweepy.OAuthHandler(self.consumer_key,self.consumer_secret)
            self.auth.set_access_token(self.access_token, self.access_token_secret)
            self.handle = tweepy.API(self.auth)

    def get_handle(self):
            return self.handle

    def hitme(self,str):
            self.handle.update_status(str)
            print 'posted succesfully'
