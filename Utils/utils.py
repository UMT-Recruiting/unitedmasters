#
# File: utils.py
# Description: Util functions for URL shortening.
# Author: Bryan Peabody
#

import random
import string


#
# Create a random string of characters that will serve as the shortened URL.
#
def create_random_string():
    # Upper and lower case letters, 52 total
    letters = string.ascii_letters
    
    # TODO: Check if this randomly generated string already exists in the database

    # Generate a random string of 10 characters. Should give us a very large number of possible combinations.
    # However, there is the chance of getting a dup here.
    result = ''.join((random.choice(letters)) for x in range(10))
    return result


#
# Create the shortened url string
#
def create_shortened_url_string(HOST, PORT, randomString):
    return 'http://' + HOST + ':' + str(PORT) + '/' + randomString
