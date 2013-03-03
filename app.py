# -*- coding: utf-8 -*-
"""
Flaskr
~~~~~~

A microblog example application written as Flask tutorial with
Flask and sqlite3.

:copyright: (c) 2010 by Armin Ronacher.
:license: BSD, see LICENSE for more details.
"""
from flask import Flask, render_template, url_for, request
SECRET_KEY = 'development key'

# create our little application :)
app = Flask(__name__)
app.debug = True

@app.route('/video')
def show_video(methods=["GET"]):
    videoid = request.args['food']
    return render_template("video.html", videoid=videoid)
 #   return output

@app.route('/')
def main_site():
    return render_template("index.html")
 #   return output


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)