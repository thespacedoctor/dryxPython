import os
import nose
from .. import convert_mysql_database_to_myisam
from dryxPython.utKit import utKit

## SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()


class test_command_line():

    def test_command_line_method_01(self):
        kwargs = {}
        kwargs["--settingsFile"] = pathToInputDir + "project_settings.yaml"
        kwargs["--tableSchema"] = False
        convert_mysql_database_to_myisam.main(kwargs)

    # x-class-method-to-test-a-command-line-usage


# class test_convert_mysql_database_to_myisam():

#     def test_convert_mysql_database_to_myisam_function(self):
#         kwargs = {}
#         kwargs = {}
#         kwargs["log"] = log
#         kwargs["dbConn"] = dbConn
#         convert_mysql_database_to_myisam.convert_mysql_database_to_myisam(
#             **kwargs)


        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
