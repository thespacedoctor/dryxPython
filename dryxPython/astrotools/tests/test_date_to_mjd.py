import os
import nose
import shutil
from .. import date_to_mjd
from fundamentals import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_date_to_mjd():

    def test_date_to_mjd_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["date"] = "20140506"
        # xt-kwarg_key_and_value

        mjd = date_to_mjd(**kwargs)
        print mjd.get()

    def test_date_to_mjd_function02(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["date"] = "20140506  ads 34 adsasd --=+ 2323"
        # xt-kwarg_key_and_value

        mjd = date_to_mjd(**kwargs)
        print mjd.get()

    def test_date_to_mjd_function03(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["date"] = "20140506"
        # xt-kwarg_key_and_value

        mjd = date_to_mjd(**kwargs)
        print mjd.get()

    def test_date_to_mjd_function04(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["date"] = "20140506"
        # xt-kwarg_key_and_value

        mjd = date_to_mjd(**kwargs)
        print mjd.get()

    def test_date_to_mjd_function05(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["date"] = "20140506"
        # xt-kwarg_key_and_value

        mjd = date_to_mjd(**kwargs)
        print mjd.get()

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
