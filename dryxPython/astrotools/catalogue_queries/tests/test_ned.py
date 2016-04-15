import os
import nose
import shutil
from .. import ned
from fundamentals import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_ned():

    def test_ned_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["ra"] = 199.28521
        kwargs["dec"] = -20.41161
        kwargs["arcsec"] = 5.0
        # xt-kwarg_key_and_value
        ned(**kwargs)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
