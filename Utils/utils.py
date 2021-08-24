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
    letters = string.ascii_letters

    # define the condition for random.choice() method
    result = ''.join((random.choice(letters)) for x in range(10))
    return result

def create_shortened_url_string(HOST, PORT, randomString):
    return 'http://' + HOST + ':' + str(PORT) + '/' + randomString