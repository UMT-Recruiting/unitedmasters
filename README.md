## Overview
This is a simple Python 3 web service using Flask. It has 2 end points:

1- The shorten endpoint - /shorten
It takes a query parameter called url and returns a shortened url.

Example url: http://127.0.0.1:4000/shorten?url=http://www.bryanpeabody.com

2- The lengthen endpoint - /lengthen
It takes a query parameter called shortURL and returns the original url, if it exists. If not, an empty string is returned.

Example url: http://localhost:4000/lengthen?shortURL=http://127.0.0.1:4000/dnvAXnJaBA
 
## How to run
I developed this using Python 3, PyCharm and Flask. There are a couple of dependecies in the requirements file. Please are steps to run it:

pip install Flask
pip install validators

 py .\main.py

OUTPUT:

(venv) PS:> py .\main.py

 Serving Flask app 'main' (lazy loading)

Environment: production

WARNING: This is a development server. Do not use it in a production deployment.

Use a production WSGI server instead.

Debug mode: off

Running on http://127.0.0.1:4000/ (Press CTRL+C to quit)

Note: I wrote this in PyCharm. It can be ran in the IDE as well.

## Unit tests
The unit tests are in the file test.py. They contains 3 unit tests that test the main functionality of the service.

Example: python -m unittest test
