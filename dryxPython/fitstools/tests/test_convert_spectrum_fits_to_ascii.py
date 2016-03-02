import os
import nose
import shutil
import yaml
# from dryxPython import cl_utils
from dryxPython.fitstools import convert_spectrum_fits_to_ascii
from fundamentals import utKit

from fundamentals import tools, times

su = tools(
    arguments={},
    docString=__doc__,
    logLevel="DEBUG",
    options_first=False,
    projectName="dryxPython"
)
arguments, settings, log, dbConn = su.setup()

# load settings
stream = file(
    "/Users/Dave/.config/dryxPython/dryxPython.yaml", 'r')
settings = yaml.load(stream)
stream.close()

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()


class test_convert_spectrum_fits_to_ascii():

    def test_convert_spectrum_fits_to_ascii_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["fitsFilePath"] = pathToInputDir + \
            "/CSS130903-012242+181_20130908_Gr13_Free_slit1.5_56999_1.fits"
        # xt-kwarg_key_and_value
        testObject = convert_spectrum_fits_to_ascii(**kwargs)
        testObject.get()

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
