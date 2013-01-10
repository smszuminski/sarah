# -*- coding: utf-8 -*-
"""
Flaskr
~~~~~~

A microblog example application written as Flask tutorial with
Flask and sqlite3.

:copyright: (c) 2010 by Armin Ronacher.
:license: BSD, see LICENSE for more details.
"""
from flask import Flask
SECRET_KEY = 'development key'

# create our little application :)
app = Flask(__name__)
app.debug = True
@app.route('/')
def main_site():
    output = "WEBSITE OMGH!"
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)