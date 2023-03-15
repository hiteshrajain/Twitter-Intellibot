import tweepy
import time
print('this is my twitterbot')

CONSUMER_KEY = 'MjaJK4USSJ6gDQe3XJWgtP6Fu'
CONSUMER_SECRET = 'WYIthZnFz6HmRA2h7fRWSFV23BPNZ4Hl2Rb98AMMz8BhLCZiZy'
ACCESS_KEY = '1044249459562098688-cO3z3LxUf9UOeC13nEAnWvGxxUtldK'
ACCESS_SECRET = 'uZmk4OS8amoWl6Da3oXzsnuYB0vgaQPN66PqGBfVXlRwI'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return
def reply_to_tweets():
    print('Retrieving and Replying to tweets...')

last_seen_id = retrieve_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline()
for mention in reversed (mentions):
    print(str(mention.id) + ' _ ' + mention.text)
    last_seen_id = mention.id
    store_last_seen_id(last_seen_id, FILE_NAME)
    if '#helloworld' in mention.text.lower():
        print('Found #helloworld!')
        print('Responding back....')
        api.update_status('@' + mention.user.screen_name +'#HelloWorld back to you!', mention.id)


while True:
    reply_to_tweets()
    time.sleep(15)
