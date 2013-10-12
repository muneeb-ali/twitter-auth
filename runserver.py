#!/usr/bin/env python
# Author: Muneeb Ali | http://muneeb.org

import os
from twitter_flask import app
from config import SERVER_ADDRESS, SERVER_PORT 

def runserver():
	port = int(os.environ.get('PORT', SERVER_PORT))
	app.run(host=SERVER_ADDRESS, port=port, debug=True)

if __name__ == '__main__':
	runserver()
