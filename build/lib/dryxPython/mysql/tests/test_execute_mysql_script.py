import os
import nose
from .. import execute_mysql_script

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE


def setUpModule():
    import logging
    import logging.config
    import yaml

    from dryxPython.commonutils.getpackagepath import getpackagepath

    # SETUP PATHS TO COMMONG DIRECTORIES FOR TEST DATA
    testDir = getpackagepath() + "tests/"
    global pathToOutputDir, pathToInputDir
    pathToInputDir = testDir + "/input/"
    pathToOutputDir = testDir + "/output/"

    # SETUP THE TEST LOG FILE
    global testlog
    testlog = open(pathToOutputDir + "tests.log", 'w')

    # SETUP LOGGING
    loggerConfig = """
    version: 1
    formatters:
        file_style:
            format: '* %(asctime)s - %(name)s - %(levelname)s (%(pathname)s > %(funcName)s > %(lineno)d) - %(message)s  '
            datefmt: '%Y/%m/%d %H:%M:%S'
        console_style:
            format: '* %(asctime)s - %(levelname)s: %(pathname)s:%(funcName)s:%(lineno)d > %(message)s'
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
    global log
    log = logging.getLogger(__name__)

    # x-setup-dbconn-for-test-module

    return None


def tearDownModule():
    "tear down test fixtures"
    # CLOSE THE TEST LOG FILE
    testlog.close()
    return None


class test_command_line():

    def test_command_line_method_01(self):
        kwargs = {}
        kwargs["--settingsFile"] = pathToInputDir + "project_settings.yaml"
        kwargs["--pathToMysqlScript"] = pathToInputDir + \
            "clean_objectnames_in_transientbucket.sql"
        kwargs["force"] = True
        execute_mysql_script.main(kwargs)

    def test_command_line_method_02(self):
        kwargs = {}
        kwargs["--host"] = "localhost"
        kwargs["--user"] = "root"
        kwargs["--passwd"] = "root"
        kwargs["--dbName"] = "pessto_marshall_sandbox"
        kwargs["--pathToMysqlScript"] = pathToInputDir + \
            "clean_objectnames_in_transientbucket.sql"
        execute_mysql_script.main(kwargs)

    # x-class-method-to-test-a-command-line-usage
# x-class-to-test-named-worker-function
