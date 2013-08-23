import os
import nose
from .. import mysql

## SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
def setUpModule():
    import logging
    import logging.config
    import yaml

    "set up test fixtures"
    moduleDirectory = os.path.dirname(__file__) + "/../tests"

    # SETUP PATHS TO COMMONG DIRECTORIES FOR TEST DATA
    global pathToInputDataDir, pathToOutputDir, pathToOutputDataDir, pathToInputDir
    pathToInputDir = moduleDirectory+"/input/"
    pathToInputDataDir = pathToInputDir + "data/"
    pathToOutputDir = moduleDirectory+"/output/"
    pathToOutputDataDir = pathToOutputDir+"data/"

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
    global log
    log = logging.getLogger(__name__)

    # SETUP DB CONNECTION
    import MySQLdb as ms
    dbConfig = """
    version: 1
    db: pessto_marshall_sandbox
    host: localhost
    user: root
    password: root
    """
    connDict = yaml.load(dbConfig)
    global dbConn
    dbConn = ms.connect(
        host=connDict['host'],
        user=connDict['user'],
        passwd=connDict['password'],
        db=connDict['db'],
    )

    return None

def tearDownModule():
    "tear down test fixtures"
    # CLOSE THE TEST LOG FILE
    testlog.close()
    return None

class emptyLogger:
    info=None
    error=None
    debug=None
    critical=None
    warning=None

class test_convert_dictionary_to_mysql_table():
    def test_raise_error_if_dbConn_is_not_a_working_db_connection(self):
        kwargs = {}
        kwargs["dbConn"] = "garbage"
        kwargs["log"] = log
        kwargs["dictionary"] = {"someGoodKey":"nice"}
        kwargs["dbTableName"] = "python_unit_testing_dict_to_mysql"
        kwargs["uniqueKeyList"] = ["someGoodKey",]
        nose.tools.assert_raises(TypeError, mysql.convert_dictionary_to_mysql_table, **kwargs)

    def test_raise_error_if_dictionary_argu_not_a_dictionary(self):
        kwargs = {}
        kwargs["dbConn"] = dbConn
        kwargs["log"] = log
        kwargs["dictionary"] = "not a dictionary"
        kwargs["dbTableName"] = "python_unit_testing_dict_to_mysql"
        kwargs["uniqueKeyList"] = ["not a dictionary",]
        nose.tools.assert_raises(TypeError, mysql.convert_dictionary_to_mysql_table, **kwargs)

    def test_raise_error_if_dictionary_has_not_simple_values(self):
        kwargs = {}
        kwargs["dbConn"] = dbConn
        kwargs["log"] = log
        kwargs["dictionary"] = {"someGoodKey":"nice","someOtherBadKey":["ev!l","list",42]}
        kwargs["dbTableName"] = "python_unit_testing_dict_to_mysql"
        kwargs["uniqueKeyList"] = ["someGoodKey","someOtherBadKey",]
        nose.tools.assert_raises(ValueError, mysql.convert_dictionary_to_mysql_table, **kwargs)

    # @action : add in test to test the database connection where i first setup dbConn (code in test database connection snippet)

    def test_raise_error_if_uniqueKeyList_is_not_list(self):
        kwargs = {}
        kwargs["dbConn"] = dbConn
        kwargs["log"] = log
        kwargs["dictionary"] = {"someGoodKey":"nice"}
        kwargs["dbTableName"] = "python_unit_testing_dict_to_mysql"
        kwargs["uniqueKeyList"] = ">>>>>>>>>>> not a list <<<<<<<<<<<"
        nose.tools.assert_raises(TypeError, mysql.convert_dictionary_to_mysql_table, **kwargs)
        pass

    def test_raise_error_if_uniqueKeyList_values_not_in_dictionary(self):
        kwargs = {}
        kwargs["dbConn"] = dbConn
        kwargs["log"] = log
        kwargs["dictionary"] = {"someGoodKey":"nice","another good key":"andother value"}
        kwargs["dbTableName"] = "python_unit_testing_dict_to_mysql"
        kwargs["uniqueKeyList"] = ["someGoodKey",">>>>>>>>>>> not a good key <<<<<<<<<<<"]
        nose.tools.assert_raises(ValueError, mysql.convert_dictionary_to_mysql_table, **kwargs)

    def test_to_create_a_table_to_see_if_code_completes(self):
        kwargs = {}
        kwargs["dbConn"] = dbConn
        kwargs["log"] = log
        kwargs["dictionary"] = {"someGoodKey":"nice","and other":"nice, nice"}
        kwargs["dbTableName"] = "python_unit_testing_dict_to_mysqlysq"
        kwargs["uniqueKeyList"] = ["someGoodKey","and other"]
        mysql.convert_dictionary_to_mysql_table(**kwargs)







