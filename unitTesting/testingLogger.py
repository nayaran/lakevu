import logging

if __name__ == '__main__':

      # add the current parent directory to the python path

      from os import sys, path
      sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
      import log

      logger = logging.getLogger('LakvuLogger.test')
      logger.info('testing lakevu logger!!!!')
