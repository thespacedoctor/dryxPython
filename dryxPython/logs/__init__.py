#!/usr/local/bin/python
# encoding: utf-8
"""
logs.py

Initially created by David Young on October 10, 2012
If you have any questions requiring this script please email me: davidrobertyoung@gmail.com

dryx syntax:
p<Var> = variable formated in the way I want it output to file or screen
xxx = come back here and do some more work

"""
import os
import sys
import logging
from logging import handlers

############################################
# MAIN LOOP - USED FOR DEBUGGING           #
############################################


def main():
    pass
if __name__ == '__main__':
    main()


def console_logger(
    level="INFO"
):
    # LAST MODIFIED : October 22, 2013
    # CREATED : October 22, 2013
    # AUTHOR : DRYX
    """Setup and return a console logger only.

    **Key Arguments:**
        - ``level`` -- the level of logging required

    **Return:**
        - ``logger`` -- the console logger

    .. todo::

        - [ ] when complete, clean console_logger function
        - [ ] when complete add logging
        - [ ] when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import logging
    import logging.config
    ## THIRD PARTY ##
    import yaml
    ## LOCAL APPLICATION ##

    # SETUP LOGGING
    loggerConfig = """
  version: 1
  formatters:
      console_style:
          format: '* %(asctime)s - %(levelname)s: %(pathname)s:%(funcName)s:%(lineno)d > %(message)s'
          datefmt: '%H:%M:%S'
  handlers:
      console:
          class: logging.StreamHandler
          level: """ + level + """
          formatter: console_style
          stream: ext://sys.stdout
  root:
      level: """ + level + """
      handlers: [console]"""

    logging.config.dictConfig(yaml.load(loggerConfig))
    logger = logging.getLogger(__name__)

    return logger


def setup_dryx_logging(yaml_file):
    """

    *setup dryx style python logging*

    """
    import logging
    # REINSTATE logging.config WHENEVER PYTHON 2.7 INSTALLED - dictconfig IS
    # USED TO MAKE LOGGING BACKWARD COMPATIBLE WITH PYTHON 2.6
    import logging.config
    # import dictconfig
    import yaml

    # IMPORT CUSTOM HANDLER THAT ALLOWS GROUP WRITING
    handlers.GroupWriteRotatingFileHandler = GroupWriteRotatingFileHandler

    # IMPORT YAML LOGGING DICTIONARY
    # REINSTATE AFTER PYTHON 2.7 INSTALLED
    stream = file(yaml_file, 'r')
    yamlContent = yaml.load(stream)
    stream.close()

    # use the logging settings section of the dictionary file if there is one
    # - otherwise assume the file contains only logging settings
    if "logging settings" in yamlContent:
        yamlContent = yamlContent["logging settings"]
        yamlContent["version"] = 1

    logging.config.dictConfig(yamlContent)
    # dictconfig.dictConfig(yaml.load(open(yaml_file, 'r')))
    # SET THE ROOT LOGGER
    logger = logging.getLogger(__name__)

    logging.captureWarnings(True)

    return logger


class GroupWriteRotatingFileHandler(handlers.RotatingFileHandler):

    """
    *rotating file handler for logging*
    """

    def doRollover(self):
        """
        *Override base class method to make the new log file group writable.*
        """
        # Rotate the file first.
        handlers.RotatingFileHandler.doRollover(self)

        # Add group write to the current permissions.
        currMode = os.stat(self.baseFilename).st_mode
        os.chmod(self.baseFilename, currMode | stat.S_IWGRP |
                 stat.S_IRGRP | stat.S_IWOTH | stat.S_IROTH)


class GroupWriteRotatingFileHandler(handlers.RotatingFileHandler):

    """
    *rotating file handler for logging*
    """

    def _open(self):
        prevumask = os.umask(0)
        # os.fdopen(os.open('/path/to/file', os.O_WRONLY, 0600))
        rtv = logging.handlers.RotatingFileHandler._open(self)
        os.umask(prevumask)
        return rtv
