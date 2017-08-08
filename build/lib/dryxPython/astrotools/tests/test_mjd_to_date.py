import os
import nose
import shutil
from .. import mjd_to_date
from fundamentals import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_mjd_to_date():

    def test_mjd_to_date_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["mjd"] = 57843.343
        # xt-kwarg_key_and_value

        thisDate = mjd_to_date(**kwargs)
        print thisDate.get()

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
