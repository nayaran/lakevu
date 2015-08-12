
import logging

def testExpenseMgmtDao():

      # import the module to be tested
      # add the current parent directory to the python path
      from os import sys, path
      sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

      # now the modules are ready to be imported
      import log
      from dao import ExpenseMgmtDao

      # initialize the logger
      logger = logging.getLogger('LakvuLogger.test')

      # test the module
      logger.info('testing testExpenseMgmtDao!!!!')
      print ExpenseMgmtDao.getAllCollections()


if __name__ == '__main__':
      testExpenseMgmtDao()
