import telepot, time
from nltk.chat.iesha import iesha_chatbot
from tweep import Tweet

tweet_client = Tweet()
is_chatting = False

def handle(msg):
    global is_chatting
    global tweet_client
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command
    if command == '/hello' and not is_chatting:
        bot.sendMessage(chat_id, 'Hello, how are you?')
    elif command == '/timeline' and not is_chatting:
        bot.sendMessage(chat_id, '\n'.join([message.text for message in tweet_client.handle.home_timeline()]))
    elif command.split('=')[0] == '/tweet' and not is_chatting:
        try:
            tweet_client.hitme(command.split('=')[1] + ' #mika')
            bot.sendMessage(chat_id, 'Your message tweeted successfully')
        except:
            bot.sendMessage(chat_id, 'There is some problem tweeting! Try after some time')
    elif command == '/chat':
        is_chatting = True
        bot.sendMessage(chat_id, 'Hi I am Iesha. Who are You?')
    elif command == '/stopchat':
        is_chatting = False
        bot.sendMessage(chat_id, 'Bye Bye. take care!')
    elif not command.startswith('/') and is_chatting:
        bot.sendMessage(chat_id, iesha_chatbot.respond(command))
    else:
        pass


# Create a bot object with API key
bot = telepot.Bot('152871568:AAFRaZ6ibZQ52wXXXXXXXXXXXXXX')

# Attach a function to notifyOnMessage call back
bot.notifyOnMessage(handle)

# Listen to the messages
while 1:
 time.sleep(10)
