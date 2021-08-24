#
# File: Main.py
# Description: Entry point into a simple Flask app to serve a URL Shortener API.
# Author: Bryan Peabody
#
from flask import Flask
from flask import request
from Utils import utils
from Utils import dbUtils
import validators

app = Flask(__name__)

# Define host and port to run on
HOST = '127.0.0.1'
PORT = 4000


#
# Routes
#

# Default route
@app.route('/')
def index():
    return "Default route"


# The route for shortening a given URL
@app.route('/shorten')
def shortenURL():
    # Get the URL from the request
    fullURL = request.args.get('url')

    # Is the URL valid?
    if not validators.url(fullURL):
        return "Invalid URL!"

    # Does fullURL already have a short URL?
    if dbUtils.does_full_url_exist(fullURL) == False:
        # Generate a random string that will be used for the shortened URL
        randomString = utils.create_random_string()

        # Create the full shortened URL
        shortURL = utils.create_shortened_url_string(HOST, PORT, randomString)

        # Persist the new pair
        dbUtils.add_url_pair(shortURL, fullURL)

        # Return the shortened address
        return shortURL
    else:
        return "The URL already exists!"


# The route to translate a shortened URL to the full, original URL
@app.route('/lengthen')
def lengthen():
    # Get the URL from the request
    shortURL = request.args.get('shortURL')

    # Look up the full url
    fullURL = dbUtils.get_full_url(shortURL)

    return fullURL


#
# Run the app
#
if __name__ == '__main__':
    app.run(HOST, PORT)
