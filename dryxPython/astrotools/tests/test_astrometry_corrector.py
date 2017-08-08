import os
import nose
from .. import astrometry_corrector
from ... import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit.utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_astrometry_corrector(unittest.TestCase):

    def test_astrometry_corrector_function(self):
        kwargs = {}
        kwargs["log"] = log

        # List of (RA, Dec) for the "reference" (correct) positions for 4
        # sources
        sky_ref = [(335.744175,  -28.968303),
                   (335.772717,  -28.916425),
                   (335.821662,  -28.922406),
                   (335.799923,  -28.986095),
                   ]
        # List of (RA, Dec) measured in the HST image for the same 4 sources
        sky_img = [(335.74290,    -28.96692),
                   (335.77277,    -28.91569),
                   (335.82129,    -28.92240),
                   (335.79844,    -28.98553)
                   ]

        kwargs["sky_ref"] = sky_ref
        kwargs["sky_img"] = sky_img
        kwargs["hdu"] = 0
        kwargs["opt_alg"] = 'scipy'
        kwargs["infile"] = pathToInputDir + "test.fits"
        kwargs["outfile"] = pathToInputDir + "test_fix_scipy.fits"
        astrometry_corrector.astrometry_corrector(**kwargs)

    # def test_astrometry_corrector_function_02(self):
    #     kwargs = {}
    #     kwargs["log"] = log

    #     # List of (RA, Dec) for the "reference" (correct) positions for 4
    #     # sources
    #     sky_ref = [(335.744175,  -28.968303),
    #                (335.772717,  -28.916425),
    #                (335.821662,  -28.922406),
    #                (335.799923,  -28.986095),
    #                ]
    #     # List of (RA, Dec) measured in the HST image for the same 4 sources
    #     sky_img = [(355.74290,    -28.96692),
    #                (335.77277,    -28.91569),
    #                (335.82129,    -28.92240),
    #                (335.79844,    -28.98553)
    #                ]

    #     kwargs["sky_ref"] = sky_ref
    #     kwargs["sky_img"] = sky_img
    #     kwargs["hdu"] = 0
    #     kwargs["opt_alg"] = 'sherpa'
    #     kwargs["infile"] = pathToInputDir + "test.fits"
    #     kwargs["outfile"] = pathToInputDir + "test_fix_sherpa.fits"
    #     astrometry_corrector.astrometry_corrector(**kwargs)

    # x-class-to-test-named-worker-function
