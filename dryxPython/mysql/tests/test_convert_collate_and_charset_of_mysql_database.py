import os
import nose
from .. import convert_collate_and_charset_of_mysql_database
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
        convert_collate_and_charset_of_mysql_database.main(kwargs)

    # x-class-method-to-test-a-command-line-usage


# class test_convert_collate_and_charset_of_mysql_database():

#     def test_convert_collate_and_charset_of_mysql_database_function(self):
#         kwargs = {}
#         kwargs = {}
#         kwargs["log"] = log
#         kwargs["dbConn"] = dbConn
#         convert_collate_and_charset_of_mysql_database.convert_collate_and_charset_of_mysql_database(
#             **kwargs)


        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
