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

    global fitsFilePath
    fitsFilePath =  pathToInputDataDir + "LSQ12dwl_20120808_i705_56462_1_fr.fits"
    testlog.write(fitsFilePath)

    return None

def tearDownFunc():
    "tear down the test fixtures"

    return None


@with_setup(setUpFunc, tearDownFunc)
def test_convert_fits_header_to_dictionary():
    "a function to test convert_fits_header_to_dictionary"
    # testlog.write(fitsFilePath)
    assert 1 + 1 == 2



