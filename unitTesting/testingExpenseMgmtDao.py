
import logging
from pprint import pformat
from pprint import pprint

# import the module to be tested
# add the current parent directory to the python path
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

# now the modules are ready to be imported
import log
from dao import ExpenseMgmtDao as dao

# initialize the logger
logger = logging.getLogger('LakvuLogger.test')

def testGetAllCollections():
      """
      Basic testing for getAllCollections
      """
      # test the module
      logger.info('testing testGetAllCollections!')
      pprint(dao.getAllCollections())

def testAddNewUser():
      """
      Basic testing for addNewUser
      """
      # prepare data
      new_group = [
                  {
                        "name" : "ghi",
                        "color": "pink"
                  },
                  {
                        "name" : "jkl",
                        "color": "brown"
                  }
      ]
      new_user = {
            "name": "sama",
            "age" : 28,
            "groups": new_group
      }
      collection = "users"

      # test the module
      dao.addNewUser(new_user, collection)

def testGetAllUsers():
      """
      Basic testing for getAllUsers
      """
      collection = "users"
      users = dao.getAllUsers(collection)

      logger.info('testing testGetAllCollections!')
      pprint(users)

if __name__ == '__main__':
      logger.info('_________testing ExpenseMgmgDao!_________')
      testGetAllCollections()
      testGetAllUsers()
      testAddNewUser()
      testGetAllUsers()

