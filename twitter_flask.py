#!/usr/bin/env python

'''
	A simple Flask app for performing Twitter OAuth
	Author: Muneeb Ali | http://muneeb.org
	Code modified from: Tweepy docs and http://github.com/whichlight/flask-tweepy-oauth 
'''


from flask import Flask, render_template, request
import flask 

from config import DB_NAME, APP_NAME, CALLBACK_URL
import tweepy
from pymongo import MongoClient

c = MongoClient()

app = Flask(__name__)

from config import CONSUMER_KEY, CONSUMER_SECRET

session = dict()
db = dict()

#-----------------------------------
@app.route('/')
def index():
	return render_template('index.html')

#-----------------------------------
@app.route('/auth')
def perform_auth():

	'''	
		Redirects to Twitter for performing auth 
		Needs CONSUMER_KEY, CONSUMER_SECRET, and CALLBACK_URL
	'''

	auth = tweepy.OAuthHandler(CONSUMER_KEY, 
							CONSUMER_SECRET,
							CALLBACK_URL)

	try: 

		redirect_url= auth.get_authorization_url()
		
		session['request_token']= (auth.request_token.key,
								auth.request_token.secret)

	except tweepy.TweepError as e:
		return render_template('error.html',error=e)
	
	#this is twitter's url for authentication
	return flask.redirect(redirect_url)	

#-----------------------
@app.route('/verify')
def get_verification():
	
	#get the verifier key from the request url
	verifier= request.args['oauth_verifier']
	
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

	token = session['request_token']
	del session['request_token']
	
	auth.set_request_token(token[0], token[1])

	try:
		    auth.get_access_token(verifier)
	except tweepy.TweepError:
		    print 'Error! Failed to get access token.'
	
	#now you have access!
	api = tweepy.API(auth)

	#store in a db
	db['api']=api
	db['access_token_key']=auth.access_token.key
	db['access_token_secret']=auth.access_token.secret
	
	return flask.redirect(flask.url_for('start'))

#-----------------------
@app.route("/start")
def start():
	#auth done, app logic can begin
	api = db['api']

	#example, print your latest status posts
	return flask.render_template('tweets.html', tweets=api.user_timeline())

#-----------------------
if __name__ == '__main__':

	app.run(debug=True)
