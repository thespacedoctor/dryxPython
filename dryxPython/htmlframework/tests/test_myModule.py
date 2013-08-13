import os
from nose import with_setup

## SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
def setUpModule():
    "set up test fixtures"
    moduleDirectory = os.path.dirname(__file__)

    # SETUP PATHS TO COMMONG DIRECTORIES FOR TEST DATA
    global pathToInputDataDir, pathToOutputDir, pathToOutputDataDir
    pathToInputDataDir = moduleDirectory+"/input/data/"
    pathToOutputDir = moduleDirectory+"/output/"
    pathToOutputDataDir = pathToOutputDir+"data/"

    # SETUP THE TEST LOG FILE
    global testlog
    testlog = open(pathToOutputDir + "tests.log", 'w')

    return None

def tearDownModule():
    "tear down test fixtures"
    # CLOSE THE TEST LOG FILE
    testlog.close()
    return None


## SETUP AND TEARDOWN FIXTURE FUNCTIONS
def setUpFunc():
    "set up the test fixtures"

    return None

def tearDownFunc():
    "tear down the test fixtures"

    return None
