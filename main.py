"""
The main file that serves all the API
"""
from bottle import route
from bottle import run
from bottle import debug
from bottle import request
from bottle import response
from bottle import error
from bottle import Bottle
from pprint import pprint
from pprint import pformat

import dao.ExpenseMgmtDao as dao
import json
import log

import logging

# get the logger instance
mainLogger = logging.getLogger('LakvuLogger.main')
app = Bottle()

@app.route('/lakevu', method='GET')
def showMainPage():
      """
      Returns the main page
      """
      return "Welcome to lakevu!"



@app.route('/lakevu/addUser', method='POST')
def addUser():
      """
      Adds a new user
      """
      new_user = request.json
      mainLogger.info('handling request for getUsers')
      mainLogger.info('received-\n%s', pformat(new_user))
      collection = "users"

      inserted_id = dao.addNewUser(new_user, collection)
      message = ""

      if inserted_id:
            mainLogger.info("Successfully addded the user with id- %s", inserted_id)
            message = "Successfully added! :)"
      else:
            mainLogger.info("Something went wrong :(")
            message = "Something went wrong :("

      return message



@app.route('/lakevu/getUsers', method='GET')
def getUsers():
      """
      Adds a new user
      """
      mainLogger.info('handling request for getUsers')
      collection = request.GET.get('collection').strip()
      mainLogger.info('received: collection - %s', collection)

      result = dao.getAllUsers(collection)

      mainLogger.info('fetching data from backend...')
      mainLogger.info('type(result)- %s', type(result))
      mainLogger.info('returning-\n%s', result)

      response.content_type = 'application/json'
      from bson.json_util import dumps
      return dumps(result)


if __name__ == "__main__":
      debug(True)
      run(app, reloader=True)
