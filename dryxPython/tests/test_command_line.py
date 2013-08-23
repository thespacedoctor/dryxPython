import os
import nose
import dryxPython.command_line as cl
from unittest import TestCase

## SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
def setUpModule():
    import logging
    import logging.config
    import yaml

    print "SETUP"

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

    return None

def tearDownModule():
    "tear down test fixtures"

    print "TEARDOWN"
    # CLOSE THE TEST LOG FILE
    testlog.close()
    return None

class emptyLogger:
    info=None
    error=None
    debug=None
    critical=None
    warning=None

class test_get_help_for_python_module():
    def test_fail_for_no_argv(self):
        result = cl.py_get_help_for_python_module()
        assert result == -1

class test_fits_print_fits_header():

    def test_docopt(self):
        clArgs = {}
        clArgs["<path-to-fits-file>"] = pathToInputDataDir + "LSQ12dwl_20120808_B639_56462_1.fits"
        clArgs["--pydict"] = False
        clArgs["--help"] = False
        result = cl.dft_print_fits_header(clArgs)
        nose.tools.assert_is_instance(result, list)

    def test_result_to_python_dictionary(self):
        clArgs = {}
        clArgs["<path-to-fits-file>"] = pathToInputDataDir + "LSQ12dwl_20120808_B639_56462_1.fits"
        clArgs["--pydict"] = True
        clArgs["--help"] = False
        result = cl.dft_print_fits_header(clArgs)
        nose.tools.assert_is_instance(result, dict)
