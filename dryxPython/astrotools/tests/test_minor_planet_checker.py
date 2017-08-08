import os
import nose
import shutil
from .. import minor_planet_checker
from fundamentals import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_minor_planet_checker(unittest.TestCase):

    def test_minor_planet_checker_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["ra"] = 228.916583333
        kwargs["dec"] = -18.3386305556
        kwargs["radius"] = 5
        kwargs["mjd"] = 57101.2648
        mpc = minor_planet_checker(**kwargs)
        print mpc.get()
        # x-print-testpage-for-pessto-marshall-web-object

    def test_minor_planet_checker_function02(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["ra"] = 228.916583333
        kwargs["dec"] = -18.3386305556
        kwargs["radius"] = 5
        kwargs["mjd"] = 57102.2648
        mpc = minor_planet_checker(**kwargs)
        print mpc.get()
