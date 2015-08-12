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
      db = client['user']
      #db = client['expenseManagement']
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


