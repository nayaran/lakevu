"""
The main file that serves all the API
"""
from bottle import route
from bottle import run
from bottle import debug
from bottle import request
from bottle import error
from bottle import Bottle
from pprint import pprint
from pprint import pformat

import dao

app = Bottle()

@app.route('lakevu/', method='GET')
def showMainPage():
      """
      Returns the main page
      """
      return "Welcome to lakevu!"


if __name__ == "__main__":
      debug(True)
      run(app, reloader=True)
