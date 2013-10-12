'''
	Config options 
'''

import os

#-----------------------------------
# NOTE: It's not good practice to save keys in code files
# put the following lines in your ~/.bashrc instead
# export CONSUMER_KEY=<your_twitter_app_key> 
# export CONSUMER_SECRET=<your_twitter_app_secret>
#-----------------------------------

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']

#make sure to set your CALBACK_URL in the application settings on Twitter as well
CALLBACK_URL = 'http://127.0.0.1:5000/verify'

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = '5000'