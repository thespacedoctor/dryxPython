import os
import nose
from .. import declination_sexegesimal_to_decimal

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE


def setUpModule():
    import logging
    import logging.config
    import yaml

    from dryxPython.commonutils.getpackagepath import getpackagepath

    # SETUP PATHS TO COMMONG DIRECTORIES FOR TEST DATA
    moduleDirectory = os.path.dirname(__file__)
    global pathToOutputDir, pathToInputDir
    pathToInputDir = moduleDirectory + "/input/"
    pathToOutputDir = moduleDirectory + "/output/"

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
    # x-import-test-database

    return None


def tearDownModule():
    "tear down test fixtures"
    # CLOSE THE TEST LOG FILE
    testlog.close()
    return None


class test_command_line(unittest.TestCase):

    def test_command_line_method_01(self):
        kwargs = {}
        kwargs["--dec"] = "12  13 13.4554"
        declination_sexegesimal_to_decimal.main(kwargs)

    def test_command_line_method_02(self):
        kwargs = {}
        kwargs["--dec"] = "-12-13-13.4554"
        declination_sexegesimal_to_decimal.main(kwargs)

    def test_command_line_method_03(self):
        kwargs = {}
        kwargs["--dec"] = "12: 13,13.4554"
        declination_sexegesimal_to_decimal.main(kwargs)

    def test_command_line_method_04(self):
        kwargs = {}
        kwargs["--dec"] = "-12_13    13.4"
        declination_sexegesimal_to_decimal.main(kwargs)

    def test_command_line_method_05(self):
        kwargs = {}
        kwargs["--dec"] = "12:13:13"
        declination_sexegesimal_to_decimal.main(kwargs)

    def test_command_line_method_06(self):
        kwargs = {}
        kwargs["--dec"] = "-0:00:23.334343"
        declination_sexegesimal_to_decimal.main(kwargs)

    def test_command_line_method_07(self):
        kwargs = {}
        kwargs["--dec"] = "0:00:23.334343"
        declination_sexegesimal_to_decimal.main(kwargs)

    def test_command_line_method_08(self):
        kwargs = {}
        kwargs["dec"] = "-92:12:34.3344"
        nose.tools.assert_raises(
            IOError, declination_sexegesimal_to_decimal.declination_sexegesimal_to_decimal, **kwargs)
        pass

    def test_command_line_method_09(self):
        kwargs = {}
        kwargs["dec"] = "02:67:34.3344"
        nose.tools.assert_raises(
            IOError, declination_sexegesimal_to_decimal.declination_sexegesimal_to_decimal, **kwargs)
        pass

    # x-class-method-to-test-a-command-line-usage
# x-class-to-test-named-worker-function
