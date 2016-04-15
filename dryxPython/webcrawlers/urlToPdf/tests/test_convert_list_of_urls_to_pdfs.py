import os
import nose
import shutil
from .. import convert_list_of_urls_to_pdfs
from fundamentals import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_convert_list_of_urls_to_pdfs():

    def test_convert_list_of_urls_to_pdfs_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs[
            "pathToRequestDirectory"] = "/Users/Dave/Dropbox/Apps/ifttt/script_triggers/url_to_pdf"
        kwargs["pathToPDFDirectory"] = "/Users/Dave/Dropbox/dryxDocs/inbox"
        # xt-kwarg_key_and_value

        convert_list_of_urls_to_pdfs(**kwargs)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
