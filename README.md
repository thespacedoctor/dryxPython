# dryx Python Modules - Full Collection #

This repo exists so that users can clone the full collection of dryx Python Modules in one go.

To clone the _master_ repo use the following command:

	git clone --recursive git@github.com:thespacedoctor/dryxPythonModulesFC.git <folderName>

Or to clone the _dev_ repo use the following command:

	git clone --recursive -b dev git@github.com:thespacedoctor/dryxPythonModulesFC.git <folderName>

To use this repo as a submodule of another repo then you must first
initiate the git workspace in the directory you want to include _dryxPythonModulesFC_, then add the code as a submodule:

    git init
    git submodule init
    git submodule add -b dev git@github.com:thespacedoctor/dryxPythonModulesFC.git python

Finally you must now update the submodules recursively:

    git submodule update --init --recursive