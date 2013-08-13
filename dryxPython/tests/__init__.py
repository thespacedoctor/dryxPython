import os

## SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE PACKAGE
## SETUP & INCLUDE MOCK DATABASES AND DATA HERE
def setUpPackage():
    "set up test fixtures"
    moduleDirectory = os.path.dirname(__file__)

    # SETUP PATHS TO COMMONG DIRECTORIES FOR TEST DATA
    global pathToInputDataDir, pathToOutputDir, pathToOutputDataDir
    pathToInputDataDir = moduleDirectory+"/input/data/"
    pathToOutputDir = moduleDirectory+"/output/"
    pathToOutputDataDir = pathToOutputDir+"data/"

    # FILE TO WRITE TEST LOGS TO
    global testlog
    testlog = open(pathToOutputDir + "tests.log", 'w')

    return None

def tearDownPackage():
    "tear down test fixtures"

    # CLOSE THE TEST LOG FILE
    testlog.close()

    return None
