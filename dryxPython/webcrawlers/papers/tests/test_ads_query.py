import os
import nose
from .. import ads_query
from fundamentals import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_ads_query():

    # def test_ads_query_function(self):
    #     kwargs = {}
    #     kwargs["log"] = log
    #     kwargs["queryString"] = "pessto"
    #     ads_query.ads_query(**kwargs)

        # x-print-testpage-for-pessto-marshall-web-object

    def test_ads_query_function02(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs[
            "url"] = "http://adsabs.harvard.edu/cgi-bin/nph-abs_connect?library&libname=PESSTO&libid=47fa2f1493&data_type=SHORT_XML"
        ads_query.ads_query(**kwargs)
