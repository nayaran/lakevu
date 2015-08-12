from pymongo import MongoClient
from datetime import datetime, date
from pprint import pformat
from pprint import pprint


# initializing the logger
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

# now the module is ready to be imported
import log
import logging

# get the logger instance
mainLogger = logging.getLogger('LakvuLogger.ExpenseMgmtDAO')


def getConnection():
      """
      Get the connection from the DB
      """
      #mainLogger.info(":: inside getConnection :: ")
      client = MongoClient()
      #db = client['user']
      #db = client['expenseManagement']
      db = client['testingDB']
      #mainLogger.info(":: returning Connection :: ")
      return db

def getAllCollections():
      """
      Get all the collections from the DB
      """
      #mainLogger.info(":: inside getAllCollections :: ")
      db = getConnection()
      result = db.collection_names()
      #mainLogger.info(":: exiting getAllCollections :: ")
      mainLogger.info("returning - %d collections", len(result))
      return result

def addNewUser(userDoc, collection):
      """
      Adds a new user to the DB
      """
      db = getConnection()
      mainLogger.info("inserting in collection- %s", collection)
      mainLogger.info("inserting document- \n%s", pformat(userDoc))
      result = db[collection].insert_one(userDoc)
      return result.inserted_id

def getAllUsers(collection):
      """
      Returns all the users in a given group
      """
      db = getConnection()
      result = db[collection].find()
      mainLogger.info("fetching useres from collection- %s", collection)
      mainLogger.info("total count of users fetched- %d", result.count())

      users = []

      for user in result:
            users.append(user)

      return users


















