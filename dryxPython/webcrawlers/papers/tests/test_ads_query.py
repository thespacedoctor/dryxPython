import os
import nose
from .. import ads_query
from dryxPython.utKit import utKit

## SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_ads_query():

    def test_ads_query_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["queryString"] = "pessto"
        ads_query.ads_query(**kwargs)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
