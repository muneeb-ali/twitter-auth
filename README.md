# twitter-flask

A simple Flask app for performing Twitter OAuth with Python Flask

### How to Get Started

1. Install all the necessary packages (best done inside of a virtual environment)
> pip install -r requirements.txt

2. Make sure 'mongod' is installed and running - http://docs.mongodb.org/manual/installation/ (needed only for storing CONSUMER_KEY and CONSUMER_SECRET, if you're saving it in some other way then there is no need for this). 

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
