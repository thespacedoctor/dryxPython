import os
import nose
import shutil
from .. import update_request_watcher
from fundamentals import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()


class test_command_line():

    def test_command_line_method_01(self):
        kwargs = {}
        kwargs["pathToGitRepos"] = "/Users/Dave/git_repos"
        update_request_watcher.main(kwargs)

    # x-class-method-to-test-a-command-line-usage
# xnose-class-to-test-named-worker-function
