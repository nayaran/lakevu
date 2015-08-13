
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
testLogger = logging.getLogger('LakvuLogger.test')

def testGetAllCollections():
      """
      Basic testing for getAllCollections
      """
      # test the module
      testLogger.info('testing testGetAllCollections!')
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
      testLogger.info('testing testGetAllUsers!')
      collection = "users"
      users = dao.getAllUsers(collection)
      testLogger.info('type(users)- %s', type(users))
      testLogger.info('received-\n%s', pformat(users))

if __name__ == '__main__':
      testLogger.info('_________testing ExpenseMgmgDao!_________')
      #testGetAllCollections()
      #testGetAllUsers()
      #testAddNewUser()
      testGetAllUsers()

