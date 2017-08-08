import os
import nose
from .. import sqlquery_to_csv_file
from fundamentals import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# x-class-to-test-main-command-line-function-of-module


class test_sqlquery_to_csv_file(unittest.TestCase):

    def test_sqlquery_to_csv_file_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["dbConn"] = dbConn
        kwargs["sqlQuery"] = """
            select transientBucketId, magnitude, filter, survey, surveyObjectUrl, observationDate, observationMJD from transientBucket where transientBucketId = 324413 and observationDate is not null and observationDate != 0000-00-00 and magnitude is not null and magnitude < 50 order by observationDate asc;
        """
        kwargs["csvType"] = "human"
        kwargs["csvTitle"] = "data exported from database"
        kwargs["csvFilename"] = "data exported from database"
        kwargs["returnFormat"] = "plainText"
        output = sqlquery_to_csv_file(**kwargs)

        print "\n\nOUTPUT:\n\n%(output)s" % locals()p

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
