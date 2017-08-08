import os
import nose
import shutil
from .. import download_flicker_image
from fundamentals import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_download_flicker_image(unittest.TestCase):

    def test_download_flicker_image_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["url"] = 'http://www.flickr.com/photos/43846774@N02/12181701385'
        # xt-kwarg_key_and_value
        downloader = download_flicker_image(**kwargs)
        url = downloader.get_url()
        print url

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
