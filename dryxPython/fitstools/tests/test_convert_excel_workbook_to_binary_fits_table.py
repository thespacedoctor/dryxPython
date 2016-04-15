import os
import nose
import shutil
from .. import convert_excel_workbook_to_binary_fits_table
from fundamentals import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_convert_excel_workbook_to_binary_fits_table():

    def test_convert_excel_workbook_to_binary_fits_table_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs[
            "pathToWorkbook"] = "/Users/Dave/git_repos/pessto_phaseIII_transient_catalogue/phase_III_transient_catalogue_pre_20140401.xls"
        # xt-kwarg_key_and_value

        fits = convert_excel_workbook_to_binary_fits_table(**kwargs)
        fits.get()

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
