## Overview
This is a simple Python 3 web service using Flask and SQLite3. It has 2 end points:

1- The shorten endpoint - /shorten
It takes a query parameter called url and returns a shortened url.

Example url: http://127.0.0.1:4000/shorten?url=http://www.bryanpeabody.com

2- The lengthen endpoint - /lengthen
It takes a query parameter called shortURL and returns the original url, if it exists. If not, an empty string is returned.

Example url: http://localhost:4000/lengthen?shortURL=http://127.0.0.1:4000/dnvAXnJaBA
 
Notes: 

-I left both endpoints as GET for ease of testing. You can do it in a browser or Postman (which is what I used).

-The SQLite3 database is included in the git repo. It can be used as is.

## How to run
I developed this using Python 3, PyCharm and Flask. There are a couple of dependecies in the requirements file. Please are steps to run it:

> pip install Flask
> pip install validators

> py .\main.py

## Unit tests
The unit tests are in the file test.py. They contains 3 unit tests that test the basic functionality of the service.

Example: python -m unittest test

## Notes
I used approximately 2.5 hours for this. It broke down as:

-1.5 hours getting the basic Flask API setup and working (basic functionality)

-1 hour setting up some very basic unit tests, testing and fixing a bug or two

-Half an hour of over architecting it and thinking about if my solution to random short urls was good or not :)

Some possible improvements:

-The random string generator is 10 characters long and it made up of 26 lower case and 26 upper case letters for a total of 52. That makes for a very large number of combinations. However, it is possible to get a dup, even with that many combinations. I also, briefly, considered using uuid's since those are supposed to always be unique but decided against it.

-Ideally, I'd like to have each shortened URL have a "last accessed timestamp". This would allow shortened urls that haven't been used in x days/months/years to be cleaned up and recycled.

-Make the endpoints POST instead of GET so that there could be a UI that posts to them.
