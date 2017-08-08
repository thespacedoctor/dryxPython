import os
import nose
from .. import createpythonpackage
from fundamentals import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# x-class-to-test-main-command-line-function-of-module
# x-class-to-test-named-worker-function


class test_command_line(unittest.TestCase):

    def test_command_line_method_01(self):
        """*--packageName=<packageName> --location=<"/path/to/package/parent/folder">*"""
        import shutil
        try:
            shutil.rmtree(pathToOutputDir + "/mytestpackage")
        except:
            pass
        kwargs = {}
        kwargs["--packageName"] = "mytestpackage"
        kwargs["--location"] = pathToOutputDir
        createpythonpackage.main(kwargs)

    def test_command_line_method_02(self):
        self.test_command_line_method_01()
        kwargs = {}
        kwargs["--subPackageName"] = "mytestsubpackage"
        kwargs["--pathToHostDirectory"] = pathToOutputDir + \
            "/mytestpackage/" + "/mytestpackage"
        createpythonpackage.main(kwargs)

    def test_command_line_method_03(self):
        self.test_command_line_method_01()
        self.test_command_line_method_02()
        import shutil
        try:
            shutil.rmtree(
                pathToOutputDir + "/mytestpackage/mytestpackage/mytestsubpackage/tests")
        except:
            pass
        kwargs = {}
        kwargs["--moduleName"] = "mytestmodule"
        kwargs["--pathToHostDirectory"] = pathToOutputDir + \
            "/mytestpackage/" + "/mytestpackage/mytestsubpackage"
        createpythonpackage.main(kwargs)

    # x-class-method-to-test-a-command-line-usage
