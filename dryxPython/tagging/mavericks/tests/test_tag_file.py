import os
import nose
import shutil
from .. import tag_file

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE


def setUpModule():
    import logging
    import logging.config
    import yaml

    from dryxPython.commonutils.getpackagepath import getpackagepath

    # SETUP PATHS TO COMMONG DIRECTORIES FOR TEST DATA
    moduleDirectory = os.path.dirname(__file__)
    global pathToOutputDir, pathToInputDir, testFileIn, testFileOut
    pathToInputDir = moduleDirectory + "/input/"
    pathToOutputDir = moduleDirectory + "/output/"
    testFileIn = "%(pathToInputDir)stest.txt" % globals()
    testFileOut = "%(pathToOutputDir)stest.txt" % globals()

    try:
        os.remove(testFileOut)
    except:
        pass

    shutil.copyfile(testFileIn, testFileOut)

    # SETUP THE TEST LOG FILE
    global testlog
    testlog = open(pathToOutputDir + "tests.log", 'w')

    # SETUP LOGGING
    loggerConfig = """
    version: 1
    formatters:
        file_style:
            format: '* %(asctime)s - %(name)s - %(levelname)s (%(filename)s > %(funcName)s > %(lineno)d) - %(message)s  '
            datefmt: '%Y/%m/%d %H:%M:%S'
        console_style:
            format: '* %(asctime)s - %(levelname)s: %(filename)s:%(funcName)s:%(lineno)d > %(message)s'
            datefmt: '%H:%M:%S'
        html_style:
            format: '<div id="row" class="%(levelname)s"><span class="date">%(asctime)s</span>   <span class="label">file:</span><span class="filename">%(filename)s</span>   <span class="label">method:</span><span class="funcName">%(funcName)s</span>   <span class="label">line#:</span><span class="lineno">%(lineno)d</span> <span class="pathname">%(pathname)s</span>  <div class="right"><span class="message">%(message)s</span><span class="levelname">%(levelname)s</span></div></div>'
            datefmt: '%Y-%m-%d <span class= "time">%H:%M <span class= "seconds">%Ss</span></span>'
    handlers:
        console:
            class: logging.StreamHandler
            level: DEBUG
            formatter: console_style
            stream: ext://sys.stdout
    root:
        level: DEBUG
        handlers: [console]"""

    logging.config.dictConfig(yaml.load(loggerConfig))
    global logger
    logger = logging.getLogger(__name__)

    # x-setup-dbconn-for-test-module
    # x-import-test-database

    return None


def tearDownModule():
    "tear down test fixtures"
    # CLOSE THE TEST LOG FILE
    testlog.close()
    return None


class test_tag_file():

    def test_tag_file_function(self):
        kwargs = {}
        kwargs["log"] = logger
        kwargs["pathToFile"] = testFileOut
        kwargs["mode"] = "set"
        kwargs["tagList"] = ["one", "two", "three"]

        tag_file.tag_file(**kwargs)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
