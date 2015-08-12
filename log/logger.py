import logging
#print 'inside logger.py'

def logger():
      """
      Defines the logger
      """

      #print 'initializing logger....'
      import os
      from os import path

      # get the current directory
      logPath = path.dirname(path.abspath(__file__))

      fileName = 'log_file'

      # configure log formatter
      file_logFormatter = logging.Formatter("%(asctime)s [%(filename)s] [%(funcName)s] [%(levelname)s] [%(lineno)d] %(message)s")

      console_logFormatter = logging.Formatter("[%(filename)s] [%(funcName)s] [%(levelname)s] [%(lineno)d] %(message)s")

      # configure file handler
      fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
      fileHandler.setFormatter(file_logFormatter)
      fileHandler.setLevel(logging.DEBUG)

      # configure stream handler
      consoleHandler = logging.StreamHandler()
      consoleHandler.setFormatter(console_logFormatter)
      consoleHandler.setLevel(logging.DEBUG)

      # get the logger instance
      logger = logging.getLogger("LakvuLogger")

      # set the logging level
      logger.setLevel(logging.DEBUG)

      #print 'adding handlers- '
      # making sure we don't add duplicates
      #if not len(logger.handlers):
      logger.addHandler(fileHandler)
      logger.addHandler(consoleHandler)

