import logging

def testLogger():
      """
      A basic method for testing the logger
      """
      # import the module to be tested
      # add the current parent directory to the python path
      from os import sys, path
      sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

      # now the module is ready to be imported
      import log

      # get child logger which would inherit the configuration
      # from the parent (LakvuLogger) logger
      logger = logging.getLogger('LakvuLogger.test')

      # test the module
      logger.info('testing lakevu logger!!!!')


if __name__ == '__main__':
      testLogger()
