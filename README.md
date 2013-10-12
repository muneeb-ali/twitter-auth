# twitter-flask

A simple Flask app for performing Twitter OAuth with Python Flask

### How to Get Started

1. Install all the necessary packages (best done inside of a virtual environment)
> pip install -r requirements.txt

2. Get your Twitter app keys (https://dev.twitter.com/apps) and add CONSUMER_KEY and CONSUMER_SECRET to your ~/.bashrc file
```
export CONSUMER_KEY=<your_twitter_app_key> 
export CONSUMER_SECRET=<your_twitter_app_secret>
```
and reload
> . ~/.bashrc

3. Run the app
> python runserver.py

If all goes well, you should see the example Twitter connect option at http://localhost:5000. Screenshot: 

![Alt text](static/images/twitter_flask_screenshot.png "Screenshot of the example submission form")

### Making Changes

* Global configuration options like DB_NAME, APP_NAME are in config.py. 
* Make sure that your CALLBACK_URL is the same as you set in your Twitter app (needed as of 10/2013)

### Author(s) 

Muneeb Ali | http://muneeb.org  
Code modified from: Tweepy docs and http://github.com/whichlight/flask-tweepy-oauth
