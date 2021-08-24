#
# File: dbUtils.py
# Description: SQLite3 utils to read, write and init the database
# Author: Bryan Peabody
#

import sqlite3
from sqlite3 import Error


#
# Creates and returns the db connection
#
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("urls.db")
    except Error as e:
        print(e)

    return conn


#
# Init the SQLite database. Only needs to be ran once.
#
def init_db():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE urls (shortURL TEXT, fullURL TEXT)")


#
# Checks to see if the full url already has been shortened
#
def does_full_url_exist(fullURL):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT shortURL FROM urls WHERE fullURL=?", (fullURL,))
    row = cursor.fetchone()

    if row is not None:
        return True

    return False


#
# Add a URL pair. The pairs will be the short URL and the full URL
#
def add_url_pair(shortURL, fullURL):
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO urls(shortURL, fullURL) VALUES(?, ?)", (shortURL, fullURL))
        conn.commit()

        return True
    except:
        return False


#
# Looks up the short url and returns the full url, if it exists. If not, an empty string is returned.
#
def get_full_url(shortURL):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT fullURL FROM urls WHERE shortURL=?", (shortURL,))
    row = cursor.fetchone()

    # Get the return value - the full url
    fullURL = ''

    # If we got something back from the db, return it
    if row is not None:
        fullURL = row[0]

    return fullURL
