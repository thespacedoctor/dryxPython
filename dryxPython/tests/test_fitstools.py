import os
import nose
from .. import fitstools

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE


def setUpModule():
    import logging
    import logging.config
    import yaml

    "set up test fixtures"
    moduleDirectory = os.path.dirname(__file__) + "/../tests"

    # SETUP PATHS TO COMMONG DIRECTORIES FOR TEST DATA
    global pathToInputDataDir, pathToOutputDir, pathToOutputDataDir, pathToInputDir
    pathToInputDir = moduleDirectory + "/input/"
    pathToInputDataDir = pathToInputDir + "data/"
    pathToOutputDir = moduleDirectory + "/output/"
    pathToOutputDataDir = pathToOutputDir + "data/"

    # SETUP THE TEST LOG FILE
    global testlog
    testlog = open(pathToOutputDir + "tests.log", 'w')

    global pathToFitsFile
    pathToFitsFile = pathToInputDataDir + "LSQ12dwl_20120808_B639_56462_1.fits"

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

    return None


def tearDownModule():
    "tear down test fixtures"
    # CLOSE THE TEST LOG FILE
    testlog.close()
    return None


class emptyLogger:
    info = None
    error = None
    debug = None
    critical = None
    warning = None


class test_convert_fits_header_to_dictionary():

    def test_pathToFitsFile_argu_is_str(self):
        nose.tools.assert_raises(
            TypeError, fitstools.convert_fits_header_to_dictionary, log, ["not a string", 10])

    def test_error_raises_if_fits_file_does_not_exists(self):
        nose.tools.assert_raises(
            IOError, fitstools.convert_fits_header_to_dictionary, log, "/path/to/nothing")

    def test_dictionary_is_returned(self):
        result = fitstools.convert_fits_header_to_dictionary(
            log, pathToFitsFile)
        nose.tools.assert_is_instance(result, dict)

    def test_dictionary_values_are_lists_with_2_items(self):
        result = fitstools.convert_fits_header_to_dictionary(
            log, pathToFitsFile)
        lengthResult = True
        for k, v in result.iteritems():
            if len(v) != 2:
                lengthResult = False
        nose.tools.assert_true(lengthResult)
