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

    ## CREATE A TABLE TO TEST WITH
    global testTableName
    testTableName = "setupmodule_table_for_unit_testing"
    cursor = dbConn.cursor(ms.cursors.DictCursor)
    try:
        createTestTable = """CREATE TABLE %s(
            id int NOT NULL AUTO_INCREMENT,
            ra DOUBLE,
            decl DOUBLE,
            PRIMARY KEY(id)
        )""" % (testTableName,)

        print createTestTable
        cursor.execute(createTestTable)
    except:
        pass

    raList = [
        23.2434234234234,
        145.123123123123,
        46.1231231231231,
        86.1312312321312,
        203.432342342343,
        309.124123131231,
        09.334132412412,
        245.242342343244,
        103.434535354234,
        0.23424242423423
    ]

    decList = [
        -89.3242342342324,
        -82.3324342342342,
        -64.1231312312312,
        -45.1231231231232,
        -30.2342342342342,
        -0.03232323232323,
        12.23232445225352,
        25.23423423424244,
        56.23234234234334,
        79.12314252435345
    ]

    for r, d in zip(raList, decList):
        insertMe = """\
            INSERT INTO %s( \
                ra, \
                decl \
            )VALUES( \
                %s, \
                %s \
            ) \
        """ % (testTableName, r,d)

        print insertMe

        cursor.execute(insertMe)

    cursor.close()

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

    def test_raise_error_if_createHelperTables_is_not_boolean(self):
        kwargs = {}
        kwargs["dbConn"] = dbConn
        kwargs["log"] = log
        kwargs["dictionary"] = {"someGoodKey":"nice","another good key":"andother value"}
        kwargs["dbTableName"] = "python_unit_testing_dict_to_mysql"
        kwargs["uniqueKeyList"] = ["someGoodKey",]
        kwargs["createHelperTables"] = ">>>>>>>>>>> not a boolean <<<<<<<<<<<"
        nose.tools.assert_raises(TypeError, mysql.convert_dictionary_to_mysql_table, **kwargs)

    def test_to_create_a_table_to_see_if_code_completes(self):
        kwargs = {}
        kwargs["dbConn"] = dbConn
        kwargs["log"] = log
        kwargs["dictionary"] = {"someGoodKey":["nice","nice"],"and other":["nice","nice"]}
        kwargs["dbTableName"] = "python_unit_testing_dict_to_mysql"
        kwargs["uniqueKeyList"] = ["someGoodKey","and other"]
        mysql.convert_dictionary_to_mysql_table(**kwargs)


class test_add_HTMIds_to_mysql_tables():
    def test_table_exits(self):
        kwargs = {}
        kwargs["primaryIdColumnName"] = "id"
        kwargs["raColName"] = "ra"
        kwargs["declColName"] = "decl"
        kwargs["tableName"] = ">>>>>>>>>>>not_a_valid_name<<<<<<<<<<<"
        kwargs["dbConn"] = dbConn
        kwargs["log"] = log
        nose.tools.assert_raises(IOError, mysql.add_HTMIds_to_mysql_tables, **kwargs)

    def test_ra_column_exits(self):
        kwargs = {}
        kwargs["primaryIdColumnName"] = "id"
        kwargs["raColName"] = ">>>>>>>>>>> not an RA name <<<<<<<<<<<"
        kwargs["declColName"] = "decl"
        kwargs["tableName"] = testTableName
        kwargs["dbConn"] = dbConn
        kwargs["log"] = log
        nose.tools.assert_raises(IOError, mysql.add_HTMIds_to_mysql_tables, **kwargs)

    def test_dec_column_exits(self):
        kwargs = {}
        kwargs["primaryIdColumnName"] = "id"
        kwargs["raColName"] = "ra"
        kwargs["declColName"] = ">>>>>>>>>>> not a DEC name <<<<<<<<<<<"
        kwargs["tableName"] = testTableName
        kwargs["dbConn"] = dbConn
        kwargs["log"] = log
        nose.tools.assert_raises(IOError, mysql.add_HTMIds_to_mysql_tables, **kwargs)

    def test_htmIds_are_generated_after_function_has_run(self):
        kwargs = {}
        kwargs["primaryIdColumnName"] = "id"
        kwargs["raColName"] = "ra"
        kwargs["declColName"] = "decl"
        kwargs["tableName"] = testTableName
        kwargs["dbConn"] = dbConn
        kwargs["log"] = log





