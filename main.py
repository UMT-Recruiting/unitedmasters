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


# The route for shortening a given URL. Setting method to GET for ease of testing either in a browser or Postman.
# POST would be the best idea for prod.
@app.route('/shorten', methods=['GET'])
def shorten():
    # Get the URL from the request
    full_url = request.args.get('url')

    # Is the URL valid?
    if full_url is None or not validators.url(full_url):
        return "Invalid URL!", 400

    # Does fullURL already have a short URL?
    if not dbUtils.does_full_url_exist(full_url):
        # Generate a random string that will be used for the shortened URL
        random_string = utils.create_random_string()

        # Create the full shortened URL
        short_url = utils.create_shortened_url_string(HOST, PORT, random_string)

        # Persist the new pair
        result = dbUtils.add_url_pair(short_url, full_url)

        # Return the short url
        if not result:
            return "Failed to add url!", 400

        return short_url, 201
    else:
        return "The URL already exists!", 400


# The route to translate a shortened URL to the full, original URL. Setting method to GET  for ease of testing
# either in a browser or Postman. POST would be the best idea for prod.
@app.route('/lengthen', methods=['GET'])
def lengthen():
    # Get the URL from the request
    short_url = request.args.get('shortURL')

    if short_url is None or not validators.url(short_url):
        return "Invalid URL!", 400

    # Look up the full url
    full_url = dbUtils.get_full_url(short_url)

    # If not found, return 404
    if full_url is None:
        return "Not found", 404

    # Found it, return the value
    return full_url, 200


#
# Run the app
#
if __name__ == '__main__':
    app.run(HOST, PORT)
