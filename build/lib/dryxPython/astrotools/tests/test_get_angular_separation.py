import os
import nose
import shutil
from .. import get_angular_separation
from fundamentals import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_get_angular_separation():

    def test_get_angular_separation_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["ra1"] = 199.28521
        kwargs["dec1"] = -20.41161
        kwargs["ra2"] = 199.28583
        kwargs["dec2"] = -20.40942
        # xt-kwarg_key_and_value

        angularSeparation, north, east = get_angular_separation(**kwargs)
        print angularSeparation, north, east

    def test_get_angular_separation_function_02(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["ra1"] = "13:17:08.45"
        kwargs["dec1"] = "-20:24:41.8"
        kwargs["ra2"] = 199.28583
        kwargs["dec2"] = -20.40942
        # xt-kwarg_key_and_value

        angularSeparation, north, east = get_angular_separation(**kwargs)
        print angularSeparation, north, east

    def test_get_angular_separation_function_03(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["ra1"] = "12:21:57.57"
        kwargs["dec1"] = "+04:28:18.5"
        kwargs["ra2"] = "12:21:54.9"
        kwargs["dec2"] = "+04:28:25.7"
        # xt-kwarg_key_and_value

        angularSeparation, north, east = get_angular_separation(**kwargs)
        print angularSeparation, north, east

    def test_get_angular_separation_function_03(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["ra1"] = "16:29:47.3"
        kwargs["dec1"] = "+08:38:39"
        kwargs["ra2"] = "16:29:46.09"
        kwargs["dec2"] = "+8:38:30.6"
        # xt-kwarg_key_and_value

        angularSeparation, north, east = get_angular_separation(**kwargs)
        print angularSeparation, north, east

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
