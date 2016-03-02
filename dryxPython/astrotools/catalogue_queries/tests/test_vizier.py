import os
import nose
from .. import vizier
from fundamentals import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_vizier():

    def test_vizier_function(self):
        kwargs = {}
        kwargs = {}
        kwargs["log"] = log
        kwargs["ra"] = "21.2232434"
        kwargs["dec"] = "34.23423423"
        kwargs["catalogue"] = "2mass"
        kwargs["radius"] = "10."
        vizier.vizier(**kwargs)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
