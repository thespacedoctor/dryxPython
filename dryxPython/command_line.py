from dryxPython import commonutils
from dryxPython import fitstools

def _set_up_command_line_tool():
    import logging
    import logging.config
    import yaml

    loggerConfig = """
    version: 1
    formatters:
        file_style:
            format: '* %(asctime)s - %(name)s - %(levelname)s (%(filename)s > %(funcName)s > %(lineno)d) - %(message)s  '
            datefmt: '%Y/%m/%d %H:%M:%S'
        console_style:
            format: '* %(asctime)s - %(levelname)s: %(filename)s:%(funcName)s:%(lineno)d > %(message)s'
            datefmt: '%H:%M:%S'
        html_style:
            format: '<div id="row" class="%(levelname)s"><span class="date">%(asctime)s</span>   <span class="label">file:</span><span class="filename">%(filename)s</span>   <span class="label">method:</span><span class="funcName">%(funcName)s</span>   <span class="label">line#:</span><span class="lineno">%(lineno)d</span> <span class="pathname">%(pathname)s</span>  <div class="right"><span class="message">%(message)s</span><span class="levelname">%(levelname)s</span></div></div>'
            datefmt: '%Y-%m-%d <span class= "time">%H:%M <span class= "seconds">%Ss</span></span>'
    handlers:
        console:
            class: logging.StreamHandler
            level: DEBUG
            formatter: console_style
            stream: ext://sys.stdout
    root:
        level: DEBUG
        handlers: [console]"""

    logging.config.dictConfig(yaml.load(loggerConfig))
    log = logging.getLogger(__name__)

    return log


## LAST MODIFIED : August 17, 2013
## CREATED : August 17, 2013
## AUTHOR : DRYX
def py_get_help_for_python_module(
        argv=None):
    """print the help for python module

    **Key Arguments:**
        - ``argv`` -- arguments for the function
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import sys
    import os
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    log = _set_up_command_line_tool()

    ## VARIABLES ##
    if argv is None:
       argv = sys.argv

    if len(argv) != 2:
       print "Usage: get_help_for_python_module <pathToModuleFile>"
       return -1
    else:
        print "argv:", argv

    pathToModuleFile = argv[1]

    basename = os.path.basename(pathToModuleFile).replace(".py","")
    print basename

    return None


## LAST MODIFIED : August 20, 2013
## CREATED : August 20, 2013
## AUTHOR : DRYX
def dft_print_fits_header(clArgs=None):
    """
    Print a fits file headers to stout

    Usage:
        dft_print_fits_header <path-to-fits-file>
        dft_print_fits_header -p <path-to-fits-file>
        dft_print_fits_header -h

        -h, --help    show this help message
        -p, --pydict  print as python dictionary
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import sys
    import os
    ## THIRD PARTY ##
    from docopt import docopt
    import pyfits as pf
    ## LOCAL APPLICATION ##
    from dryxPython import fitstools as dft

    ## SETUP AN EMPTY LOGGER
    log = _set_up_command_line_tool()

    if clArgs == None:
        clArgs = docopt(dft_print_fits_header.__doc__)

    pathToFitsFile = clArgs["<path-to-fits-file>"]

    hduList = pf.open(pathToFitsFile)
    fitsHeader=hduList[0].header

    fitsHeader = hduList[0].header
    cardList = fitsHeader.ascardlist()
    result = cardList
    hduList.close()

    if clArgs["--pydict"]:
        thisDict = dft.convert_fits_header_to_dictionary(
            log,
            pathToFitsFile=pathToFitsFile
        )
        result = thisDict

    print result
    return None


# from . import joke

# def main():
#     print joke()
