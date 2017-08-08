import os
import nose
import shutil
from .. import download_google_sheet
from fundamentals import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_download_google_sheet(unittest.TestCase):

    def test_download_google_sheet_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["email"] = "d.r.young@qub.ac.uk"
        kwargs["password"] = "i8VLH)+d7rm}22o9P;W%&yRa7pmu7P"
        kwargs["gdoc_id"] = "1A9NOjQTS4nSt_KSb0YUTlQ0utTARjcGT5UWbsADcY1M#gid=0"
        # xt-kwarg_key_and_value

        downloadFilepath = download_google_sheet(**kwargs)
        print downloadFilepath

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
