import os
import nose
from ... import htmlframework as dhf

## SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
def setUpModule():
    import logging
    import logging.config
    import yaml

    "set up test fixtures"
    moduleDirectory = os.path.dirname(__file__) + "/../../tests"

    # SETUP PATHS TO COMMONG DIRECTORIES FOR TEST DATA
    global pathToInputDataDir, pathToOutputDir, pathToOutputDataDir, pathToInputDir
    pathToInputDir = moduleDirectory+"/input/"
    pathToInputDataDir = pathToInputDir + "data/"
    pathToOutputDir = moduleDirectory+"/output/"
    pathToOutputDataDir = pathToOutputDir+"data/"

    # SETUP THE TEST LOG FILE
    global testlog
    testlog = open(pathToOutputDir + "tests.log", 'w')

    # SETUP LOGGING
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
    global log
    log = logging.getLogger(__name__)

    global cheatsheet
    cheatsheet = open(pathToOutputDir + "htdocs/dryxPython_htmlframework_cheatsheet.html", 'w')

    global fillerText
    fillerText = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

    # x-setup-dbconn-for-test-module

    return None

def tearDownModule():
    "tear down test fixtures"
    # CLOSE THE TEST LOG FILE
    cheatsheet.close()
    testlog.close()
    return None

class emptyLogger:
    info=None
    error=None
    debug=None
    critical=None
    warning=None


# class test_mediaObject():
#     def test_mediaObject_works_as_expected(self):
#         ## MEDIA OBJECT
#         kwargs = {}
#         kwargs["displayType"]='div'
#         kwargs["img"]=dhf.image(
#             src='holder.js/200x200/industrial/text:test mediaobject',  # [ industrial | gray | social ]
#         )
#         kwargs["headlineText"]='This is a mediaObject'
#         kwargs["nestedMediaObjects"]=False
#         content += dhf.mediaObject(**kwargs)

# class test_well():
#     def test_well_works_as_expected(self):
#         text = "This is a well"
#         kwargs = {}
#         kwargs["wellText"]=text
#         wellSize='default'
#         content += dhf.well(**kwargs)

# class test_closeIcon():
#     def test_closeIcon_works_as_expected(self):
#         kwargs = {}
#         content = dhf.closeIcon(**kwargs)

# class test_button():
#     def test_button_works_as_expected(self):
#         kwargs = {}
#         kwargs["buttonText"]=""
#         kwargs["buttonStyle"]="default"
#         kwargs["buttonSize"]="default"
#         kwargs["href"]=False
#         kwargs["submit"]=False
#         kwargs["block"]=False
#         kwargs["disable"]=False
#         content = dhf.button(**kwargs)

# class test_buttonGroup():
#     def test_buttonGroup_works_as_expected(self):
#         kwargs = {}
#         kwargs["buttonList"]=""
#         kwargs["format"]="default"
#         content = dhf.buttonGroup(**kwargs)

# class test_code():
#     def test_code_works_as_expected(self):
#         kwargs = {}
#         kwargs["content"]=""
#         kwargs["inline"]=True
#         kwargs["scroll"]=False
#         content = dhf.code(**kwargs)


# class test_dropdown():
#     def test_dropdown_works_as_expected(self):
#         kwargs = {}
#         kwargs["buttonColor"]="default"
#         kwargs["buttonSize"]="default"
#         kwargs["buttonColor"]="default"
#         kwargs["menuTitle"]="#"
#         kwargs["splitButton"]=False
#         kwargs["linkList"]=[]
#         kwargs["separatedLinkList"]=False
#         kwargs["pull"]=False
#         kwargs["direction"]="down"
#         kwargs["onPhone"]=True
#         kwargs["onTablet"]=True
#         kwargs["onDesktop"]=True
#         content = dhf.dropdown(**kwargs)


# class test_searchForm():
#     def test_searchForm_works_as_expected(self):
#         kwargs = {}
#         kwargs["buttonText"]=""
#         kwargs["span"]=2
#         kwargs["inlineHelpText"]=False
#         kwargs["blockHelpText"]=False
#         kwargs["focusedInputText"]=False
#         content = dhf.searchForm(**kwargs)

# class test_form():
#     def test_form_works_as_expected(self):
#         kwargs = {}
#         kwargs["content"]=""
#         kwargs["formType"]="inline"
#         kwargs["navBarPull"]=False
#         content = dhf.form(**kwargs)

# class test_horizontalFormControlGroup():
#     def test_horizontalFormControlGroup_works_as_expected(self):
#         kwargs = {}
#         kwargs["content"]=""
#         kwargs["validationLevel"]=False  #  [ warning | error | info | success ]
#         content = dhf.horizontalFormControlGroup(**kwargs)

# class test_horizontalFormControlLabel():
#     def test_horizontalFormControlLabel_works_as_expected(self):
#         kwargs = {}
#         kwargs["labelText"]=""
#         kwargs["forId"]=False
#         content = dhf.horizontalFormControlLabel(**kwargs)

# class test_formInput():
#     def test_formInput_works_as_expected(self):
#         kwargs = {}
#         kwargs["ttype"]="text"  # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
#         kwargs["placeholder"]=""
#         kwargs["span"]=2
#         kwargs["searchBar"]=False
#         kwargs["pull"]=False  # [ false | right | left ]
#         kwargs["prepend"]=False
#         kwargs["append"]=False
#         button1=False
#         button2=False
#         kwargs["prependDropdown"]=False
#         kwargs["appendDropdown"]=False
#         kwargs["inlineHelpText"]=False
#         kwargs["blockHelpText"]=False
#         kwargs["focusedInput"]=False
#         kwargs["required"]=False
#         kwargs["disabled"]=False
#         content = dhf.formInput(**kwargs)

# class test_textarea():
#     def test_textarea_works_as_expected(self):
#         kwargs = {}
#         kwargs["rows"]=""
#         kwargs["span"]=2
#         kwargs["inlineHelpText"]=False
#         kwargs["blockHelpText"]=False
#         kwargs["focusedInputText"]=False
#         kwargs["required"]=False
#         kwargs["disabled"]=False
#         content = dhf.textarea(**kwargs)

# class test_checkbox():
#     def test_checkbox_works_as_expected(self):
#         kwargs = {}
#         kwargs["optionText"]=""
#         kwargs["inline"]=False
#         kwargs["optionNumber"]=1
#         kwargs["inlineHelpText"]=False
#         kwargs["blockHelpText"]=False
#         kwargs["disabled"]=False
#         content = dhf.checkbox(**kwargs)

# class test_select():
#     def test_select_works_as_expected(self):
#         kwargs = {}
#         kwargs["optionList"]=[]
#         kwargs["multiple"]=False
#         kwargs["span"]=2
#         kwargs["inlineHelpText"]=False
#         kwargs["blockHelpText"]=False
#         kwargs["required"]=False
#         kwargs["disabled"]=False
#         content = dhf.select(**kwargs)

# class test_radio():
#     def test_radio_works_as_expected(self):
#         kwargs = {}
#         kwargs["optionText"]=""
#         kwargs["optionNumber"]=1
#         kwargs["inlineHelpText"]=False
#         kwargs["blockHelpText"]=False
#         kwargs["disabled"]=False
#         content = dhf.radio(**kwargs)

# class test_controlRow():
#     def test_controlRow_works_as_expected(self):
#         kwargs = {}
#         kwargs["inputList"]=[]
#         content = dhf.controlRow(**kwargs)

# class test_uneditableInput():
#     def test_uneditableInput_works_as_expected(self):
#         kwargs = {}
#         kwargs["placeholder"]=""
#         kwargs["span"]=2
#         kwargs["inlineHelpText"]=False
#         kwargs["blockHelpText"]=False
#         content = dhf.uneditableInput(**kwargs)

# class test_formActions():
#     def test_formActions_works_as_expected(self):
#         kwargs = {}
#         kwargs["primaryButton"]=""
#         button2=False
#         button3=False
#         button4=False
#         button5=False
#         kwargs["inlineHelpText"]=False
#         kwargs["blockHelpText"]=False
#         content = dhf.formActions(**kwargs)

# # xxx-replace
# ## LAST MODIFIED : May 28, 2013
# ## CREATED : May 28, 2013
# ## AUTHOR : DRYX
# class test_unescape_html():
#     def test_unescape_html_works_as_expected(self):
#         kwargs = {}
#         kwargs["html"] = "&@$^(*^)  123 {}()_+~?><?><"
#         content = dhf.unescape_html(**kwargs)

# class test_image():
#     def test_image_works_as_expected(self):
#         kwargs = {}
#         kwargs["src"]="http://placehold.it/200x200"
#         kwargs["href"]=False
#         kwargs["display"]="False", # [ rounded | circle | polaroid ]
#         kwargs["pull"]="left", # [ "left" | "right" | "center" ]
#         kwargs["htmlClass"]=False
#         kwargs["thumbnail"]=False
#         kwargs["width"]=False
#         kwargs["onPhone"]=True
#         kwargs["onTablet"]=True
#         kwargs["onDesktop"]=True
#         content = dhf.image(**kwargs)

# class test_thumbnail():
#     def test_thumbnail_works_as_expected(self):
#         kwargs = {}
#         kwargs["htmlContent"]=""
#         content = dhf.thumbnail(**kwargs)

# class test_label():
#     def test_label_works_as_expected(self):
#         kwargs = {}
#         kwargs["text"]=''
#         level='default'  # [ "default" | "success" | "warning" | "important" | "info" | "inverse" ]
#         content = dhf.label(**kwargs)

# class test_badge():
#     def test_badge_works_as_expected(self):
#         kwargs = {}
#         kwargs["text"]=''
#         level='default'
#         content = dhf.badge(**kwargs)

# class test_alert():
#     def test_alert_works_as_expected(self):
#         kwargs = {}
#         kwargs["alertText"]=''
#         kwargs["alertHeading"]=""
#         kwargs["extraPadding"]=False
#         kwargs["alertLevel"]="warning"
#         content = dhf.alert(**kwargs)

# class test_progressBar():
#     def test_progressBar_works_as_expected(self):
#         kwargs = {}
#         kwargs["barStyle"]="plain"
#         kwargs["precentageWidth"]="10"
#         kwargs["barLevel"]="info"
#         content = dhf.progressBar(**kwargs)

class test_stackedProgressBar():
    def test_stackedProgressBar_works_as_expected(self):
        kwargs = {}
        kwargs["barStyle"]="plain"
        kwargs["infoWidth"]="10"
        kwargs["successWidth"]="10"
        kwargs["warningWidth"]="10"
        kwargs["errorWidth"]="10"

        content = dhf.stackedProgressBar(**kwargs)
        # if content is not None: cheatsheet.write(content)
#    """Generate a progress bar - TBS style
#
#    **Key Arguments:**
#        - ``barStyle`` -- style of the progress bar [ "plain" | "striped" | "striped-active" ]
#        - ``infoWidth`` -- the precentage width of the info level bar
#        - ``successWidth`` -- the precentage width of the success level bar
#        - ``warningWidth`` -- the precentage width of the warning level bar
#        - ``errorWidth`` -- the precentage width of the error level bar
#
#    **Return:**
#        - ``progressBar`` -- the progressBar
#    """
class test_responsive_navigation_bar():
    def test_responsive_navigation_bar_works_as_expected(self):
        kwargs = {}
        kwargs["brand"]=False
        kwargs["outsideNavList"]=False
        kwargs["insideNavList"]=False
        kwargs["htmlId"]=False
        kwargs["onPhone"]=True
        kwargs["onTablet"]=True
        kwargs["onDesktop"]=True

        content = dhf.responsive_navigation_bar(**kwargs)
        # if content is not None: cheatsheet.write(content)
#    """ Create a twitter bootstrap responsive nav-bar component
#
#    **Key Arguments:**
#        - ``shade`` -- if dark then colors are inverted [ False | 'dark' ]
#        - ``brand`` -- the website brand [ image | text ]
#        - ``outsideNavList`` -- nav-list to be contained outside collapsible content
#        - ``insideNavList`` -- nav-list to be contained inside collapsible content
#        - ``htmlId`` --
#        - ``onPhone`` -- does this container get displayed on a phone sized screen
#        - ``onTablet`` -- does this container get displayed on a tablet sized screen
#        - ``onDesktop`` -- does this container get displayed on a desktop sized screen
#
#    **Return:**
#        - ``navBar`` --
#    """
class test_nav_list():
    def test_nav_list_works_as_expected(self):
        kwargs = {}
        kwargs["itemList"]=[]
        kwargs["pull"]=False
        kwargs["onPhone"]=True
        kwargs["onTablet"]=True
        kwargs["onDesktop"]=True
        content = dhf.nav_list(**kwargs)
        # if content is not None: cheatsheet.write(content)
#    """Create an html list of navigation items from the required python list
#
#    **Key Arguments:**
#        - ``itemList`` -- items to be included in the navigation list
#        - ``pull`` -- float the nav-list [ False | 'right' | 'left' ]
#        - ``onPhone`` -- does this container get displayed on a phone sized screen
#        - ``onTablet`` -- does this container get displayed on a tablet sized screen
#        - ``onDesktop`` -- does this container get displayed on a desktop sized screen
#
#    **Return:**
#        - navList
#    """
# class test_get_nav_block():
#     def test_get_nav_block_works_as_expected(self):
#         kwargs = {}
#         kwargs["htmlClass"]="test"
#         kwargs["htmlId"]="test"
#         kwargs["blockContent"]="test"
#         kwargs["jsEvents"]="test"
#         kwargs["extraAttr"]="test"
#         attributeDict=kwargs
#         content = dhf.get_nav_block(**attributeDict)

#  """Create a basic ``<nav>`` code block
#
#  **Variable Attributes:**
#    - ``attributeDict`` -- dictionary of the following keywords:
#    - ``htmlClass`` -- the html element class
#    - ``htmlId`` -- the html element id
#    - ``blockContent`` -- actual content to be placed in html code block
#    - ``jsEvents`` -- inline javascript event
#    - ``extraAttr`` -- extra inline css attributes and/or handles
#
#  **Returns:**
#    - ``block`` -- the html block
#
#  attributeDict template:
#    attributeDict = dict(
#                          kwargs["htmlClass"]=___
#                          kwargs["htmlId"]=___
#                          kwargs["jsEvents"]=___
#                          kwargs["extraAttr"]=___
#                          kwargs["blockContent"]=___
#                        )
#  """
class test_searchbox():
    def test_searchbox_works_as_expected(self):
        kwargs = {}
        kwargs["size"]='medium'
        kwargs["placeHolder"]=False
        kwargs["button"]=False
        kwargs["buttonSize"]='small'
        kwargs["buttonColor"]='grey'
        kwargs["navBar"]=False
        kwargs["pull"]=False
        content = dhf.searchbox(**kwargs)
        # if content is not None: cheatsheet.write(content)
#    """Create a Search box
#
#    **Key Arguments:**
#        - ``size`` -- size = mini | small | medium | large | xlarge | xxlarge
#        - ``placeholder`` -- placeholder text
#        - ``button`` -- do you want a search button?
#        - ``buttonSize``
#        - ``buttonColor``
#
#    **Return:**
#        - ``markup`` -- markup for the searchbar
#    """
class test_tabbableNavigation():
    def test_tabbableNavigation_works_as_expected(self):
        kwargs = {}
        kwargs["contentDictionary"]={}
        kwargs["fadeIn"]=True
        kwargs["direction"]='top'
        content = dhf.tabbableNavigation(**kwargs)
        # if content is not None: cheatsheet.write(content)
#    """ Generate a tabbable Navigation
#
#    **Key Arguments:**
#        - ``contentDictionary`` -- the content dictionary { name : content }
#        - ``fadeIn`` -- make tabs fade in
#        - ``direction`` -- the position of the tabs [ above | below | left | right ]
#
#    **Return:**
#        - ``tabbableNavigation`` -- the tabbableNavigation
#    """
class test_navBar():
    def test_navBar_works_as_expected(self):
        kwargs = {}
        kwargs["brand"]=''
        kwargs["contentList"]=[]
        kwargs["dividers"]=False
        kwargs["fixedOrStatic"]=False
        kwargs["location"]='top'
        kwargs["responsive"]=False
        kwargs["dark"]=False
        content = dhf.navBar(**kwargs)
        # if content is not None: cheatsheet.write(content)
#    """ Generate a navBar - TBS style
#
#    **Key Arguments:**
#        - ``brand`` -- the website brand [ image | text ]
#        - ``contentDictionary`` -- the content dictionary { text : href }
#        - ``fixedOrStatic`` -- Fix the navbar to the top or bottom of the viewport, or create a static full-width navbar that scrolls away with the page [ False | fixed | static ]
#        - ``location`` -- location of the navigation bar if fixed or static
#        - ``dark`` -- Modify the look of the navbar by making it dark
#
#    **Return:**
#        - ``navBar`` -- the navBar
#    """
class test_pagination():
    def test_pagination_works_as_expected(self):
        kwargs = {}
        kwargs["listItems"]=""
        kwargs["size"]="default"
        kwargs["align"]="left"
        content = dhf.pagination(**kwargs)
        # if content is not None: cheatsheet.write(content)
#    """Generate pagination - TBS style. Simple pagination inspired by Rdio, great for apps and search results.
#
#    **Key Arguments:**
#        - ``listItems`` -- the numbered items to be listed within the <ul> of the pagination block
#        - ``size`` -- additional pagination block sizes [ "mini" | "small" | "default" | "large" ]
#        - ``align`` -- change the alignment of pagination links [ "left" | "center" | "right" ]
#
#    **Return:**
#        - ``pagination`` -- the pagination
#    """

#    """The doctype and html tags
#
#    **Key Arguments:**
#        - ``content`` -- the head and body of the html page
#
#    **Return:**
#        - ``doctype`` -- the HTML5 doctype
#    """



#    """Generate an html head element for your webpage
#
#    **Key Arguments:**
#        ``relativeUrlBase`` -- relative base url for js, css, image folders
#        ``pageTitle`` -- well, the page title!
#        ``mainCssFileName`` -- css file name
#        ``extras`` -- any extra info to be included in the ``head`` element
#
#    **Return:**
#        - ``head`` -- the head
#    """

#    """Generate an HTML body
#
#    **Key Arguments:**
#        - ``navBar`` -- the top navigation bar
#        - ``htmlId`` -- *id* attribute of the body
#        - ``content`` -- body content built from smaller HTML code blocks
#        - ``extraAttr`` -- an extra attributes to be added to the body definition
#        - ``relativeUrlBase`` -- how to get back to the document root
#        - ``responsive`` -- should the webpage be responsive to screen-size?
#        - ``googleAnalyticsCode`` -- google analytics code for the website
#        - ``jsFileName`` -- the name of the main javascript file
#
#    **Return:**
#        - ``body`` -- the body
#    """
class test_row():
    def test_row_works_as_expected(self):
        kwargs = {}
        kwargs["responsive"]=True
        kwargs["columns"]=''
        kwargs["htmlId"]=False
        kwargs["htmlClass"]=False
        kwargs["onPhone"]=True
        kwargs["onTablet"]=True
        kwargs["onDesktop"]=True
        content = dhf.grid_row(**kwargs)
        # if content is not None: cheatsheet.write(content)
#    """Create a row using the Twitter Bootstrap static layout grid.
#    The static Bootstrap grid system utilizes 12 columns.
#
#    **Key Arguments:**
#        - ``responsive`` -- fluid layout if true, fixed if false
#        - ``columns`` -- coulmns to be included in this row
#        - ``htmlId`` -- the id of the row
#        - ``htmlClass`` -- the class of the row
#        - ``onPhone`` -- does this row get displayed on a phone sized screen
#        - ``onTablet`` -- does this row get displayed on a tablet sized screen
#        - ``onDesktop`` -- does this row get displayed on a desktop sized screen
#
#    **Return:**
#        - ``row`` -- the row
#    """
# class test_get_simple_div():
#     def test_get_simple_div_works_as_expected(self):
#         kwargs = {}
#         kwargs["htmlId"]=None
#         blockContent=None
#         content = dhf.get_simple_div(**kwargs)

#    """ Generate a basic <div> with block-content
#
#  ****Key Arguments:****
#    - ``htmlId`` -- the html id attribute
#    - ``blockContent`` -- content to be surrounded by html div tag
#
#  **Return:**
#    - ``div``
#    """

class test_grid_column():
    def test_grid_column_works_as_expected(self):
        kwargs = {}
        kwargs["log"]=log
        kwargs["span"]=1
        kwargs["offset"]=0
        kwargs["content"]=''
        kwargs["htmlId"]=False
        kwargs["htmlClass"]=False
        kwargs["onPhone"]=True
        kwargs["onTablet"]=True
        kwargs["onDesktop"]=True
        content = dhf.grid_column(**kwargs)

class test_tr():
    def test_tr_works_as_expected(self):
        kwargs = {}
        kwargs["cellContent"]=""
        kwargs["color"]=False
        content = dhf.tr(**kwargs)

class test_th():
    def test_th_works_as_expected(self):
        kwargs = {}
        kwargs["content"]=""
        kwargs["color"]=False
        content = dhf.th(**kwargs)

class test_td():
    def test_td_works_as_expected(self):
        kwargs = {}
        kwargs["content"]=""
        kwargs["color"]=False
        content = dhf.td(**kwargs)

class test_tableCaption():
    def test_tableCaption_works_as_expected(self):
        kwargs = {}
        kwargs["content"]=""
        content = dhf.tableCaption(**kwargs)

class test_thead():
    def test_thead_works_as_expected(self):
        kwargs = {}
        kwargs["trContent"]=""
        content = dhf.thead(**kwargs)

class test_tbody():
    def test_tbody_works_as_expected(self):
        kwargs = {}
        kwargs["trContent"]=""
        content = dhf.tbody(**kwargs)

class test_table():
    def test_table_works_as_expected(self):
        kwargs = {}
        kwargs["caption"]=""
        kwargs["thead"]=""
        kwargs["tbody"]=""
        kwargs["striped"]=True
        kwargs["bordered"]=False
        kwargs["hover"]=True
        kwargs["condensed"]=False
        content = dhf.table(**kwargs)

class test_p():
    def test_p_works_as_expected(self):
        kwargs = {}
        kwargs["content"]=""
        kwargs["lead"]=False
        kwargs["textAlign"]=False
        kwargs["color"]=False
        kwargs["navBar"]=False
        kwargs["onPhone"]=True
        kwargs["onTablet"]=True
        kwargs["onDesktop"]=True
        content = dhf.p(**kwargs)

class test_emphasizeText():
    def test_emphasizeText_works_as_expected(self):
        kwargs = {}
        kwargs["style"]="em"
        kwargs["text"]=""
        content = dhf.emphasizeText(**kwargs)

class test_abbr():
    def test_abbr_works_as_expected(self):
        kwargs = {}
        kwargs["abbreviation"]=""
        kwargs["fullWord"]=""
        content = dhf.abbr(**kwargs)

class test_address():
    def test_address_works_as_expected(self):
        kwargs = {}
        kwargs["name"]=False
        addressLine1=False
        addressLine2=False
        addressLine3=False
        kwargs["phone"]=False
        kwargs["email"]=False
        kwargs["twitterHandle"]=False
        content = dhf.address(**kwargs)

class test_blockquote():
    def test_blockquote_works_as_expected(self):
        kwargs = {}
        kwargs["content"]=""
        kwargs["source"]=False
        kwargs["pullRight"]=False
        content = dhf.blockquote(**kwargs)

class test_ul():
    def test_ul_works_as_expected(self):
        kwargs = {}
        kwargs["itemList"]=[]
        kwargs["unstyled"]=False
        kwargs["inline"]=False
        kwargs["dropDownMenu"]=False
        kwargs["navStyle"]=False
        kwargs["navPull"]=False
        kwargs["navDirection"]="horizontal"
        kwargs["breadcrumb"]=False
        kwargs["pager"]=False
        kwargs["thumbnails"]=False
        kwargs["mediaList"]=False

        content = dhf.ul(**kwargs)

class test_li():
    def test_li_works_as_expected(self):
        kwargs = {}
        kwargs["content"]=""
        kwargs["span"]=False
        kwargs["disabled"]=False
        kwargs["submenuTitle"]=False
        kwargs["divider"]=False
        kwargs["navStyle"]=False
        kwargs["navDropDown"]=False
        kwargs["pager"]=False  #  [ False | "previous" | "next" ]
        content = dhf.li(**kwargs)

class test_a():
    def test_a_works_as_expected(self):
        kwargs = {}
        kwargs["content"]=""
        kwargs["href"]=False
        kwargs["tableIndex"]=False
        kwargs["triggerStyle"]=False
        content = dhf.a(**kwargs)

class test_ol():
    def test_ol_works_as_expected(self):
        kwargs = {}
        kwargs["itemList"]=[]
        content = dhf.ol(**kwargs)

class test_descriptionLists():
    def test_descriptionLists_works_as_expected(self):
        kwargs = {}
        kwargs["orderedDictionary"]={}
        kwargs["sideBySide"]=False
        content = dhf.descriptionLists(**kwargs)

class test_code():
    def test_code_works_as_expected(self):
        kwargs = {}
        kwargs["content"]=""
        kwargs["inline"]=True
        kwargs["scroll"]=False
        content = dhf.code(**kwargs)

class test_heroUnit():
    def test_heroUnit_works_as_expected(self):
        kwargs = {}
        kwargs["headline"]=""
        kwargs["tagline"]=""
        kwargs["buttonStyle"]="primary"
        kwargs["buttonText"]=""
        kwargs["buttonHref"]="#"
        content = dhf.heroUnit(**kwargs)

class test_pageHeader():
    def test_pageHeader_works_as_expected(self):
        kwargs = {}
        kwargs["headline"]=""
        kwargs["tagline"]=""
        content = dhf.pageHeader(**kwargs)

class test_0001_htmlDocument():
    def test_htmlDocument_works_as_expected(self):
        content = ""
        lt = lambda x: "<BR/><h2>%s</h2>" % (x,)
        st = lambda x: "<BR/><h4>%s</h4>" % (x,)
        ct = dhf.code

        ## PAGE DETAILS
        text = "Page Details:\n"
        content += lt(text)

        text = dhf.p(
            content="webpage-head-and-body",
            color="success",  #  [ muted | warning | info | error | success ]
        )
        content += "<br><br><em>Snippet:</em> " + text
        content += "Page constructed from a %s and %s in an %s" % (ct("head"), ct("body"), ct("htmlDocument"))



        ## BASIC GRIDS
        text = "Basic grid HTML"
        content += lt(text)
        placeHolder1 = dhf.image(
            src='holder.js/50x50/social/text:1',  # [ industrial | gray | social ]
        )
        placeHolder2 = dhf.image(
            src='holder.js/100x50/social/text:2',  # [ industrial | gray | social ]
        )
        placeHolder3 = dhf.image(
            src='holder.js/200x50/social/text:3 offset 3',  # [ industrial | gray | social ]
        )
        text = "%s with %s and %s. Use these items to structure and build your pages.<br><br>" % (ct("grid_row"),ct("grid_coulmn"),ct("placeHolders"))
        content += text
        column = dhf.grid_column(
            log,
            span=1, # 1-12
            offset=0, # 1-12
            content=placeHolder1
        )
        row = dhf.grid_row(
            responsive=True,
            columns=column*12,
        )
        content += row + "<br>"
        column = dhf.grid_column(
            log,
            span=2, # 1-12
            offset=0, # 1-12
            content=placeHolder2
        )
        row = dhf.grid_row(
            responsive=True,
            columns=column*6,
        )
        content += row + "<br>"
        column = dhf.grid_column(
            log,
            span=3, # 1-12
            offset=3, # 1-12
            content=placeHolder3
        )
        row = dhf.grid_row(
            responsive=True,
            columns=column*2,
        )
        content += row + "<br>"

        ## TEXT
        text = "Typography"
        content += lt(text) + "Use a %s with `lead = True`" % (ct("p"),)
        text = dhf.p(
            content=fillerText,
            lead=True,
            textAlign="left",  # [ left | center | right ]
            color="info",  #  [ muted | warning | info | error | success ]
            navBar=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        content += text

        textSnip = "<small>this is small, muted, left aligned %s text wrapped in %s tags</small><br>" % (ct("&ltp&gt"),ct("&ltsmall&gt"),)
        text = dhf.p(
            content=textSnip,
            textAlign="left",  # [ left | center | right ]
            color="muted"  #  [ muted | warning | info | error | success ]
        )
        content += text

        textSnip = "<strong>this is bold, warning, centred %s text wrapped in %s tags</strong><br>" % (ct("&ltp&gt"),ct("&ltstrong&gt"),)
        text = dhf.p(
            content=textSnip,
            textAlign="center",  # [ left | center | right ]
            color="warning"  #  [ muted | warning | info | error | success ]
        )
        content += text

        textSnip = "<em>this is italic, error, right aligned %s text wrapped in %s tags</em><br>" % (ct("&ltp&gt"),ct("&ltem&gt"),)
        text = dhf.p(
            content=textSnip,
            textAlign="right",  # [ left | center | right ]
            color="error"  #  [ muted | warning | info | error | success ]
        )
        content += text

        textSnip = "you can also have success %s text<br>" % (ct("&ltp&gt"),)
        text = dhf.p(
            content=textSnip,
            textAlign="left",  # [ left | center | right ]
            color="success"  #  [ muted | warning | info | error | success ]
        )
        content += text

        textSnip = "and you can have info %s text<br>" % (ct("&ltp&gt"),)
        text = dhf.p(
            content=textSnip,
            textAlign="left",  # [ left | center | right ]
            color="info"  #  [ muted | warning | info | error | success ]
        )
        content += text

        textSnip = "or the default %s text<br>" % (ct("&ltp&gt"),)
        text = dhf.p(
            content=textSnip,
            textAlign="left",  # [ left | center | right ]
            color="default"  #  [ muted | warning | info | error | success ]
        )
        content += text

        content += "use %s to create this abbreviation - hover<br><br>" % (ct("abbr"),)
        kwargs = {}
        kwargs["abbreviation"]="abbr<br><br>"
        kwargs["fullWord"]="use `abbr` to create this abbreviation"
        content += dhf.abbr(**kwargs)

        content += "use %s for an address block:<br><br>" % (ct("address"),)
        kwargs = {}
        kwargs["name"]="name"
        kwargs["addressLine1"]="addressLine1"
        kwargs["addressLine2"]="addressLine2"
        kwargs["addressLine3"]="addressLine3"
        kwargs["phone"]="phone"
        kwargs["email"]="email"
        kwargs["twitterHandle"]="@twitterHandle"
        content += dhf.address(**kwargs)

        kwargs = {}
        kwargs["content"]="for a quote use %s" % (ct("blockquote"),)
        kwargs["source"]="this is the source"
        kwargs["pullRight"]=True
        content += dhf.blockquote(**kwargs)


        ## LISTS
        text = "Lists"
        content += lt(text)

        content += "for a unordered list use %s with %s:" % (ct("ul"),ct("li"))
        kwargs = {}
        kwargs["itemList"]=["list Item","list Item","list Item","list Item","list Item"]
        kwargs["unstyled"]=False
        kwargs["inline"]=False
        kwargs["dropDownMenu"]=False
        kwargs["navStyle"]=False
        kwargs["navPull"]=False
        kwargs["navDirection"]="horizontal"
        kwargs["breadcrumb"]=False
        kwargs["pager"]=False
        kwargs["thumbnails"]=False
        kwargs["mediaList"]=False
        content += dhf.ul(**kwargs)

        content += "for a ordered list use %s with %s:" % (ct("ol"),ct("li"))
        kwargs = {}
        kwargs["itemList"]=["list Item","list Item","list Item","list Item","list Item"]
        content += dhf.ol(**kwargs)

        content += "you can also have an unstyled list using %s with %s:" % (ct("ul"),ct("li"))
        kwargs = {}
        kwargs["itemList"]=["list Item","list Item","list Item","list Item","list Item"]
        kwargs["unstyled"]=True
        kwargs["inline"]=False
        kwargs["dropDownMenu"]=False
        kwargs["navStyle"]=False
        kwargs["navPull"]=False
        kwargs["navDirection"]="horizontal"
        kwargs["breadcrumb"]=False
        kwargs["pager"]=False
        kwargs["thumbnails"]=False
        kwargs["mediaList"]=False
        content += dhf.ul(**kwargs)

        content += "for a description list use %s" % (ct("descriptionLists"),)
        kwargs = {}
        kwargs["orderedDictionary"]={"keyOne": "valueOne"}
        kwargs["sideBySide"]=False
        content += dhf.descriptionLists(**kwargs)

        content += "or line them up with `sideBySide = True`"
        kwargs = {}
        kwargs["orderedDictionary"]={"keyOne": "valueOne"}
        kwargs["sideBySide"]=True
        content += dhf.descriptionLists(**kwargs)

        ## CODE
        text = "Code"
        content += lt(text)

        content += "for inline code use %s<br><br>" % (ct("code"),)

        kwargs = {}
        kwargs["content"]="for a code block use `%s` with `inline = False`" % (ct("code"),)
        kwargs["inline"]=False
        kwargs["scroll"]=False
        content += dhf.code(**kwargs)


        ## TABLES
        text = "Tables"
        content += lt(text)
        content += "for a table use %s, with %s, %s and %ss<br><br>" % (ct("table"),ct("thead"),ct("tbody"),ct("tr"))

        kwargs = {}
        kwargs["content"]="th"
        kwargs["color"]=False
        th = dhf.th(**kwargs)

        kwargs = {}
        kwargs["content"]="td"
        kwargs["color"]=False
        td = dhf.td(**kwargs)

        kwargs = {}
        kwargs["cellContent"]=td+td+td+td
        kwargs["color"]=False
        tr = dhf.tr(**kwargs)

        kwargs = {}
        kwargs["content"]="for a caption use %s" % (ct("tableCaption"),)
        tableCaption = dhf.tableCaption(**kwargs)

        kwargs = {}
        kwargs["trContent"]=th+th+th+th
        thead = dhf.thead(**kwargs)

        kwargs = {}
        kwargs["trContent"]=tr+tr+tr
        tbody = dhf.tbody(**kwargs)

        kwargs = {}
        kwargs["caption"]=tableCaption
        kwargs["thead"]=thead
        kwargs["tbody"]=tbody
        kwargs["striped"]=False
        kwargs["bordered"]=False
        kwargs["hover"]=False
        kwargs["condensed"]=False
        content += dhf.table(**kwargs)


        content += "for a striped table set `striped = True`<br><br>"
        kwargs = {}
        kwargs["caption"]=False
        kwargs["thead"]=thead
        kwargs["tbody"]=tbody
        kwargs["striped"]=True
        kwargs["bordered"]=False
        kwargs["hover"]=False
        kwargs["condensed"]=False
        content += dhf.table(**kwargs)

        content += "for a bordered table set `bordered = True`<br><br>"
        kwargs = {}
        kwargs["caption"]=False
        kwargs["thead"]=thead
        kwargs["tbody"]=tbody
        kwargs["striped"]=False
        kwargs["bordered"]=True
        kwargs["hover"]=False
        kwargs["condensed"]=False
        content += dhf.table(**kwargs)

        content += "for hover table set `hover = True`<br><br>"
        kwargs = {}
        kwargs["caption"]=False
        kwargs["thead"]=thead
        kwargs["tbody"]=tbody
        kwargs["striped"]=False
        kwargs["bordered"]=False
        kwargs["hover"]=True
        kwargs["condensed"]=False
        content += dhf.table(**kwargs)

        kwargs = {}
        kwargs["cellContent"]=td+td+td+td
        kwargs["color"]="info"
        tri = dhf.tr(**kwargs)

        kwargs = {}
        kwargs["cellContent"]=td+td+td+td
        kwargs["color"]="warning"
        trw = dhf.tr(**kwargs)

        kwargs = {}
        kwargs["cellContent"]=td+td+td+td
        kwargs["color"]="error"
        tre = dhf.tr(**kwargs)

        kwargs = {}
        kwargs["cellContent"]=td+td+td+td
        kwargs["color"]="success"
        trs = dhf.tr(**kwargs)

        kwargs = {}
        kwargs["trContent"]=tri+tre+trs+trw
        tbody = dhf.tbody(**kwargs)

        content += "for condensed table set `condensed = True` - you can also have colored rows<br><br>"
        kwargs = {}
        kwargs["caption"]=False
        kwargs["thead"]=thead
        kwargs["tbody"]=tbody
        kwargs["striped"]=False
        kwargs["bordered"]=False
        kwargs["hover"]=False
        kwargs["condensed"]=True
        content += dhf.table(**kwargs)


        ## FORMS
        text = "Forms"
        content += lt(text)

        kwargs = {}
        kwargs["ttype"]="email"
        kwargs["placeholder"]="email"
        kwargs["prepend"]="@"
        kwargs["span"]=2
        kwargs["htmlId"]="email"
        kwargs["focusedInputText"]="email"
        emailInput = dhf.formInput(**kwargs)

        kwargs = {}
        kwargs["ttype"]="password"
        kwargs["append"]="?"
        kwargs["placeholder"]="password"
        kwargs["span"]=2
        kwargs["htmlId"]="password"
        passwordInput = dhf.formInput(**kwargs)

        kwargs = {}
        kwargs["ttype"]="date"
        kwargs["placeholder"]="date"
        kwargs["span"]=2
        kwargs["htmlId"]="date"
        dateInput = dhf.formInput(**kwargs)


        text = "<br><br>set `formType = 'horizontal'` for horizontal form. "

        content += text


        kwargs = {}
        kwargs["labelText"]="email"
        kwargs["forId"]="email"
        emailLabel = dhf.horizontalFormControlLabel(**kwargs)

        kwargs = {}
        kwargs["labelText"]="date"
        kwargs["forId"]="date"
        dateLabel = dhf.horizontalFormControlLabel(**kwargs)

        kwargs = {}
        kwargs["labelText"]="password"
        kwargs["forId"]="password"
        passwordLabel = dhf.horizontalFormControlLabel(**kwargs)

        kwargs = {}
        kwargs["inputList"]=[emailInput,]
        emailInputRow = dhf.controlRow(**kwargs)

        kwargs = {}
        kwargs["inputList"]=[passwordInput,]
        passwordInputRow = dhf.controlRow(**kwargs)

        kwargs = {}
        kwargs["inputList"]=[dateInput,]
        dateInputRow = dhf.controlRow(**kwargs)

        kwargs = {}
        kwargs["content"]=emailLabel+emailInputRow
        kwargs["validationLevel"]=False
        emailCG = dhf.horizontalFormControlGroup(**kwargs)

        kwargs = {}
        kwargs["content"]=passwordLabel+passwordInputRow
        kwargs["validationLevel"]=False
        passwordCG = dhf.horizontalFormControlGroup(**kwargs)

        kwargs = {}
        kwargs["content"]=dateLabel+dateInputRow
        kwargs["validationLevel"]=False
        dateCG = dhf.horizontalFormControlGroup(**kwargs)



        kwargs = {}
        kwargs["inputList"]=[emailInput,]
        emailInputRow = dhf.controlRow(**kwargs)
        kwargs = {}
        kwargs["labelText"]="email"
        kwargs["forId"]="email"
        emailLabel = dhf.horizontalFormControlLabel(**kwargs)
        kwargs = {}
        kwargs["inputList"]=[emailInput,]
        emailInputRow = dhf.controlRow(**kwargs)
        kwargs = {}
        kwargs["content"]=emailLabel+emailInputRow
        kwargs["validationLevel"]=False
        emailCG = dhf.horizontalFormControlGroup(**kwargs)



        label = dhf.horizontalFormControlLabel(
            labelText='radio button',
            forId="radioButton1"
        )
        radioCheck = dhf.radio(
            optionText='option 1',
            optionNumber=1,
            inlineHelpText=False,
            blockHelpText=False,
            disabled=False
        )
        radioCheck2 = dhf.radio(
            optionText='option 2',
            optionNumber=2,
            inlineHelpText=False,
            blockHelpText=False,
            disabled=False
        )
        formRow = dhf.controlRow(
            inputList=[radioCheck,radioCheck2])
        radioCG = dhf.horizontalFormControlGroup(
            content=label+formRow,
            validationLevel=False
        )

        label = dhf.horizontalFormControlLabel(
            labelText='checkbox',
            forId="checbox"
        )
        checkbox = dhf.checkbox(
            optionText='checkbox',
            inline=False,
            htmlId="checkbox",
            optionNumber=1,
            inlineHelpText=False,
            blockHelpText=False,
            disabled=False
        )
        formRow = dhf.controlRow(
            inputList=[checkbox,])
        checkboxCG = dhf.horizontalFormControlGroup(
            content=label+formRow,
            validationLevel=False
        )

        button = dhf.button(
            buttonText='default button',
            buttonStyle='primary', # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonSize='default',  # [ large | default | small | mini ]
            href="#",
            submit=True
        )

        button5 = dhf.button(
            buttonText='button5',
            buttonStyle='info', # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonSize='default',  # [ large | default | small | mini ]
            href="#",
            submit=True
        )

        button2 = dhf.button(
            buttonText='button2',
            buttonStyle='success', # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonSize='default',  # [ large | default | small | mini ]
            href="#",
            submit=True
        )

        button3 = dhf.button(
            buttonText='button3',
            buttonStyle='warning', # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonSize='mini',  # [ large | default | small | mini ]
            href="#",
            submit=True
        )

        button4 = dhf.button(
            buttonText='button4',
            buttonStyle='danger', # [ efault | primary | info | success | warning | danger | inverse | link ]
            buttonSize='small',  # [ large | default | small | mini ]
            href="#",
            submit=True
        )

        button6 = dhf.button(
            buttonText='button4',
            buttonStyle='inverse', # [ efault | primary | info | success | warning | danger | inverse | link ]
            buttonSize='large',  # [ large | default | small | mini ]
            href="#",
            submit=True
        )

        button7 = dhf.button(
            buttonText='link button',
            buttonStyle='link', # [ efault | primary | info | success | warning | danger | inverse | link ]
            buttonSize='default',  # [ large | default | small | mini ]
            href="#",
            submit=True
        )

        button8 = dhf.button(
            buttonText='large block-level and disabled',
            buttonStyle='success', # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonSize='large',  # [ large | default | small | mini ]
            href="#",
            submit=False,
            block=True,
            disable=True
        )

        text = "form Actions"
        kwargs = {}
        kwargs["primaryButton"]=button
        kwargs["button2"]=button2
        kwargs["button3"]=button3
        kwargs["button4"]=button4
        kwargs["button5"]=button5
        kwargs["inlineHelpText"]=False
        kwargs["blockHelpText"]=False
        formActions = dhf.formActions(**kwargs)

        text = "more form Actions"
        kwargs = {}
        kwargs["primaryButton"]=button6
        kwargs["button2"]=button7
        kwargs["button3"]=button8
        kwargs["inlineHelpText"]=False
        kwargs["blockHelpText"]=False
        moreformActions = dhf.formActions(**kwargs)


        htmlId="uneditable",
        label = dhf.horizontalFormControlLabel(
            labelText='uneditable input',
            forId=htmlId
        )
        kwargs = {}
        kwargs["placeholder"]="uneditableInput"
        kwargs["span"]=2
        kwargs["inlineHelpText"]=False
        kwargs["blockHelpText"]=False
        uneditableInput = dhf.uneditableInput(**kwargs)
        formRow = dhf.controlRow(
            inputList=[uneditableInput,])
        uneditableInputCG = dhf.horizontalFormControlGroup(
            content=label+formRow,
            validationLevel=False
        )


        label = dhf.horizontalFormControlLabel(
            labelText='textarea',
            forId='textarea'
        )
        textarea = dhf.textarea(
            rows='',
            span=2,
            htmlId='textarea',
            inlineHelpText=False,
            blockHelpText=False,
            focusedInputText=False,
            required=False,
            disabled=False
        )
        formRow = dhf.controlRow(
            inputList=[textarea,]
        )
        textareaCG = dhf.horizontalFormControlGroup(
            content=label+formRow,
            validationLevel=False
        )

        label = dhf.horizontalFormControlLabel(
            labelText='selection',
            forId='selection'
        )
        kwargs = {}
        kwargs["optionList"]=["select list","link","link","link","link",]
        kwargs["multiple"]=False
        kwargs["span"]=2
        kwargs["inlineHelpText"]=False
        kwargs["blockHelpText"]=False
        kwargs["required"]=False
        kwargs["disabled"]=False
        select = dhf.select(**kwargs)
        formRow = dhf.controlRow(
            inputList=[select,])
        selectionCG = dhf.horizontalFormControlGroup(
            content=label+formRow,
            validationLevel=False
        )

        htmlId="mulSelection",
        label = dhf.horizontalFormControlLabel(
            labelText='multiple selection',
            forId=htmlId
        )
        multipleselection = dhf.select(
            optionList=["select list","link","link","link","link",],
            multiple=True,
            span=2,
            htmlId=htmlId,
            inlineHelpText=False,
            blockHelpText=False,
            required=False,
            disabled=False
        )
        formRow = dhf.controlRow(
            inputList=[multipleselection,])
        multipleselectionCG = dhf.horizontalFormControlGroup(
            content=label+formRow,
            validationLevel=False
        )

        htmlId="inlineChecks",
        label = dhf.horizontalFormControlLabel(
            labelText='inline checkboxes',
            forId=htmlId
        )


        check1 = dhf.checkbox(
            optionText='1',
            inline=True,
            htmlId=htmlId,
            optionNumber=1,
            inlineHelpText=False,
            blockHelpText=False,
            disabled=False
        )

        check2 = dhf.checkbox(
            optionText='2',
            inline=True,
            htmlId=htmlId,
            optionNumber=2,
            inlineHelpText=False,
            blockHelpText=False,
            disabled=False
        )

        check3 = dhf.checkbox(
            optionText='3',
            inline=True,
            htmlId=htmlId,
            optionNumber=3,
            inlineHelpText=False,
            blockHelpText=False,
            disabled=False
        )

        inlinecheckboxes = check1+check2+check3

        formRow = dhf.controlRow(
            inputList=[inlinecheckboxes,])
        inlinecheckboxesCG = dhf.horizontalFormControlGroup(
            content=label+formRow,
            validationLevel=False
        )

        goButton = dhf.button(
            buttonText='Go',
            buttonStyle='default', # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonSize='default',  # [ large | default | small | mini ]
            href=False,
            submit=False,
            block=False,
            disable=False
        )



        htmlId="urlInput",
        label = dhf.horizontalFormControlLabel(
            labelText='url',
            forId=htmlId
        )
        url = dhf.formInput(
                    ttype='url',
                    placeholder='url',
                    span=2,
                    htmlId=False,
                    searchBar=False,
                    pull=False,
                    prepend=False,
                    append=False,
                    button1=goButton,
                    button2=False,
                    appendDropdown=False,
                    inlineHelpText=False,
                    blockHelpText=False,
                    focusedInputText=False,
                    required=False,
                    disabled=False
                )
        formRow = dhf.controlRow(
            inputList=[url,])
        urlCG = dhf.horizontalFormControlGroup(
            content=label+formRow,
            validationLevel=False
        )

        link = dhf.li(
            content='link',  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )

        dropdown = dhf.dropdown(
            buttonSize='default',
            buttonColor='default',
            menuTitle='Actions',
            splitButton=False,
            linkList=[link,link,link,link,link,],
            separatedLinkList=False,
            pull=False,
            direction='down',
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        htmlId="numner",
        label = dhf.horizontalFormControlLabel(
            labelText='input with dropdown',
            forId=htmlId
        )
        inputwithdropdown = dhf.formInput(
            ttype='number',
            placeholder='',
            span=2,
            htmlId='number',
            appendDropdown=dropdown,
            inlineHelpText=False,
            blockHelpText=False,
            focusedInputText=False,
            required=False,
            disabled=False
        )
        formRow = dhf.controlRow(
            inputList=[inputwithdropdown,])
        inputwithdropdownCG = dhf.horizontalFormControlGroup(
            content=label+formRow,
            validationLevel=False
        )

        content += "<br><br>For a form item use snippet %s" % (ct("horizontal-form-item"),)
        content += "<small>- this places a %s and a %s within a %s</small>" % (ct("horizontalFormControlLabel"),ct("controlRow"),ct("horizontalFormControlGroup"))

        kwargs = {}
        kwargs["content"]=emailCG+passwordCG+dateCG+textareaCG+radioCG+checkboxCG+selectionCG+uneditableInputCG+multipleselectionCG+inlinecheckboxesCG+urlCG+inputwithdropdownCG+formActions+moreformActions
        kwargs["formType"]="horizontal"
        kwargs["navBarPull"]=False
        content += dhf.form(**kwargs)

        kwargs = {}
        kwargs["buttonText"]="search me"
        kwargs["span"]=2
        kwargs["inlineHelpText"]=False
        kwargs["blockHelpText"]=False
        kwargs["focusedInputText"]=False
        kwargs["htmlId"]='searchForm'
        searchForm = dhf.searchForm(**kwargs)
        content += searchForm



        ## IMAGES
        text = "Images"
        content += lt(text)
        thisImage = dhf.image(
            src='holder.js/200x200/industrial/text:rounded image',
            href=False,
            display="rounded", # [ rounded | circle | polaroid ]
            pull="left", # [ "left" | "right" | "center" ]
            htmlClass=False,
            thumbnail=False,
            width=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        content += thisImage

        thisImage = dhf.image(
            src='holder.js/200x200/industrial/text:circle image',
            href=False,
            display="circle", # [ rounded | circle | polaroid ]
            pull="left", # [ "left" | "right" | "center" ]
            htmlClass=False,
            thumbnail=False,
            width=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        content += thisImage

        thisImage = dhf.image(
            src='holder.js/200x200/industrial/text:polaroid image',
            href=False,
            display="polaroid", # [ rounded | circle | polaroid ]
            pull="left", # [ "left" | "right" | "center" ]
            htmlClass=False,
            thumbnail=False,
            width=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        content += thisImage

        ## Icons
        text = "Icons"
        content += lt(text)

        content += """<span class="icon-paper"></span>"""
        content += """<i class="icon-location"></i>"""

        ## Dropdown
        text = "Dropdowns"
        content += lt(text)

        link = dhf.a(
            content='link',
            href="#",
            tableIndex=-1,
            triggerStyle=False
        )
        disabledLink = dhf.li(
            content=link,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=True,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )
        liveLink = dhf.li(
            content=link,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )

        link = dhf.a(
            content='link',
            href="#",
            tableIndex=-1,
            triggerStyle=False
        )
        linkListItem = dhf.li(
            content=link,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )


        rightAlighnDropdown = dhf.dropdown(
            buttonSize='default',
            buttonColor='default',
            menuTitle='right align',
            splitButton=False,
            linkList=[disabledLink,liveLink,disabledLink,liveLink,liveLink,liveLink,],
            separatedLinkList=False,
            pull="right",
            direction='down',
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        content += rightAlighnDropdown

        subMenu = dhf.ul(
            itemList=[liveLink,disabledLink,liveLink,liveLink,liveLink],
            unstyled=False,
            inline=False,
            dropDownMenu=True,
            navStyle=False,
            navPull=False,
            navDirection='horizontal',
            breadcrumb=False,
            pager=False,
            thumbnails=False,
            mediaList=False
        )
        subMenu = dhf.li(
            content=subMenu,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle="More Options",
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )
        thisDropdown = dhf.dropdown(
            buttonSize='default',
            buttonColor='default',
            menuTitle='dropdown with submenu',
            splitButton=False,
            linkList=[liveLink,disabledLink,liveLink,liveLink,subMenu],
            separatedLinkList=False,
            pull=False,
            direction='down',
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        content += thisDropdown


        ##Button Groups
        text = "Button Groups"
        content += lt(text)

        button1 = dhf.button(
            buttonText='button1',
            buttonStyle='default', # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonSize='default',  # [ large | default | small | mini ]
            href=False,
            submit=False,
            block=False,
            disable=False
        )
        button2 = dhf.button(
            buttonText='button2',
            buttonStyle='default', # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonSize='default',  # [ large | default | small | mini ]
            href=False,
            submit=False,
            block=False,
            disable=False
        )
        button3 = dhf.button(
            buttonText='button3',
            buttonStyle='default', # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonSize='default',  # [ large | default | small | mini ]
            href=False,
            submit=False,
            block=False,
            disable=False
        )
        buttonGroup = dhf.buttonGroup(
            buttonList=[button1,button2,button3,],
            format='default'
        )
        content += buttonGroup

        buttonGroup = dhf.buttonGroup(
            buttonList=[buttonGroup,buttonGroup,buttonGroup],
            format='toolbar'  # [ default | toolbar | vertical ]
        )
        content += buttonGroup

        buttonGroup = dhf.buttonGroup(
            buttonList=[button1,button2,button3,],
            format='vertical'  # [ default | toolbar | vertical ]
        )
        content += buttonGroup

        ##Button Dropdowns
        text = "Button Dropdowns"
        content += lt(text)

        thisDropdown = dhf.dropdown(
            buttonSize='large',
            buttonColor='info',
            menuTitle='button dropdown',
            splitButton=True,
            linkList=[liveLink,liveLink,liveLink,liveLink,],
            separatedLinkList=False,
            pull=False,
            direction='up',
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        content += thisDropdown

        ##Navs
        text = "Navs"
        content += lt(text)


        link = dhf.a(
            content='page',
            href="#",
            triggerStyle=False
        )
        linkListItem = dhf.li(
            content=link,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle="active",  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )
        tabs = dhf.ul(
           itemList=[liveLink, disabledLink, liveLink, linkListItem,], # e.g a list links
           unstyled=False,
           inline=False,
           dropDownMenu=False,  #  [ false | true ]
           navStyle="tabs",  # [ nav | tabs | pills | list ]
           navPull=False,  #  [ false | left | right ]
           navDirection='default',  # [ 'default' | 'stacked' | 'horizontal' ]
           breadcrumb=False,  #  [ False | True ]
           pager=False,
           thumbnails=False,
           mediaList=False
        )
        content +=  tabs


        pills = dhf.ul(
           itemList=[liveLink, disabledLink, liveLink, linkListItem,], # e.g a list links
           unstyled=False,
           inline=False,
           dropDownMenu=False,  #  [ false | true ]
           navStyle="pills",  # [ nav | tabs | pills | list ]
           navPull="right",  #  [ false | left | right ]
           navDirection='default',  # [ 'default' | 'stacked' | 'horizontal' ]
           breadcrumb=False,  #  [ False | True ]
           pager=False,
           thumbnails=False,
           mediaList=False
        )
        content +=  pills


        stackedTabs = dhf.ul(
           itemList=[liveLink, disabledLink, liveLink, linkListItem,], # e.g a list links
           unstyled=False,
           inline=False,
           dropDownMenu=False,  #  [ false | true ]
           navStyle="tabs",  # [ nav | tabs | pills | list ]
           navPull=False,  #  [ false | left | right ]
           navDirection='stacked',  # [ 'default' | 'stacked' | 'horizontal' ]
           breadcrumb=False,  #  [ False | True ]
           pager=False,
           thumbnails=False,
           mediaList=False
        )
        content +=  stackedTabs

        droplink = dhf.a(
            content='dropdown',
            href=False,
            tableIndex=False,
            triggerStyle='dropdown' # [ False | "dropdown" | "tab" ]
        )
        ul = dhf.ul(
            itemList=[link, link, link], # e.g a list links
            unstyled=False,
            inline=False,
            dropDownMenu=True,  #  [ false | true ]
            navStyle=False,  # [ nav | tabs | pills | list ]
            navPull=False,  #  [ false | left | right ]
            navDirection='horizontal',  # [ 'default' | 'stacked' | 'horizontal' ]
            breadcrumb=False,  #  [ False | True ]
            pager=False,
            thumbnails=False,
            mediaList=False
        )
        dropdown = dhf.li(
            content=droplink+ul,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=True,
            pager=False  # [ False | "previous" | "next" ]
        )
        stackedPills = dhf.ul(
           itemList=[liveLink, disabledLink, liveLink, dropdown, linkListItem], # e.g a list links
           unstyled=False,
           inline=False,
           dropDownMenu=False,  #  [ false | true ]
           navStyle="pills",  # [ nav | tabs | pills | list ]
           navPull=False,  #  [ false | left | right ]
           navDirection='default',  # [ 'default' | 'stacked' | 'horizontal' ]
           breadcrumb=False,  #  [ False | True ]
           pager=False,
           thumbnails=False,
           mediaList=False
        )
        content +=  stackedPills

        tabPills = dhf.ul(
           itemList=[liveLink, disabledLink, liveLink, dropdown, linkListItem], # e.g a list links
           unstyled=False,
           inline=False,
           dropDownMenu=False,  #  [ false | true ]
           navStyle="tabs",  # [ nav | tabs | pills | list ]
           navPull=False,  #  [ false | left | right ]
           navDirection='default',  # [ 'default' | 'stacked' | 'horizontal' ]
           breadcrumb=False,  #  [ False | True ]
           pager=False,
           thumbnails=False,
           mediaList=False
        )
        content +=  tabPills


        header = dhf.li(
            content='header title',  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle="header",  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )
        active = dhf.li(
            content=link,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle="active",  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )
        item = dhf.li(
            content=link,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )
        item = dhf.li(
            content=link,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )
        divider = dhf.li(
            content='',  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=True,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )
        navList = dhf.ul(
            itemList=[header,active,link,link,divider,header,active,link,link,], # e.g a list links
            unstyled=False,
            inline=False,
            dropDownMenu=False,  #  [ false | true ]
            navStyle="list",  # [ nav | tabs | pills | list ]
            navPull=False,  #  [ false | left | right ]
            navDirection='horizontal',  # [ 'default' | 'stacked' | 'horizontal' ]
            breadcrumb=False,  #  [ False | True ]
            pager=False,
            thumbnails=False,
            mediaList=False
        )
        content += navList

        tabbableNavigation = dhf.tabbableNavigation(
            contentDictionary={ "section 1" : "this is section 1 content", "section 2" : "this is section 2 content", "section 3" : "this is section 3 content",},  # { name : content }
            fadeIn=True,
            direction='top'
        )
        content += tabbableNavigation

        tabbableNavigation = dhf.tabbableNavigation(
            contentDictionary={ "section 1" : "this is section 1 content", "section 2" : "this is section 2 content", "section 3" : "this is section 3 content",},  # { name : content }
            fadeIn=True,
            direction='below'
        )
        content += tabbableNavigation

        tabbableNavigation = dhf.tabbableNavigation(
            contentDictionary={ "section 1" : "this is section 1 content", "section 2" : "this is section 2 content", "section 3" : "this is section 3 content",},  # { name : content }
            fadeIn=True,
            direction='left'
        )
        content += tabbableNavigation

        tabbableNavigation = dhf.tabbableNavigation(
            contentDictionary={ "section 1" : "this is section 1 content", "section 2" : "this is section 2 content", "section 3" : "this is section 3 content",},  # { name : content }
            fadeIn=True,
            direction='right'
        )
        content += tabbableNavigation

        ##Navbar
        text = "Navbar"
        content += lt(text)


        searchForm = dhf.form(
            content='',  # dictionary
            formType='navbar-search', #  [ "inline" | "horizontal" | "search" | "navbar-form" | "navbar-search" ]
            navBarPull="right"  # [ false | right | left ]
        )


        pageLink = dhf.a(
            content='Page',
            href='#'
        )
        itemName = dhf.li(
            content=pageLink,  # if a subMenu for dropdown this should be <ul>
        )
        droplink = dhf.a(
            content='dropdown',
            href=False,
            tableIndex=False,
            triggerStyle='dropdown' # [ False | "dropdown" | "tab" ]
        )
        ul = dhf.ul(
            itemList=[link, link, link], # e.g a list links
            unstyled=False,
            inline=False,
            dropDownMenu=True,  #  [ false | true ]
            navStyle=False,  # [ nav | tabs | pills | list ]
            navPull=False,  #  [ false | left | right ]
            navDirection='horizontal',  # [ 'default' | 'stacked' | 'horizontal' ]
            breadcrumb=False,  #  [ False | True ]
            pager=False,
            thumbnails=False,
            mediaList=False
        )
        dropdown = dhf.li(
            content=droplink+ul,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=True,
            pager=False  # [ False | "previous" | "next" ]
        )
        navbarForm = dhf.form(
            content='',  # dictionary
            formType='navbar-form', #  [ "inline" | "horizontal" | "search" | "navbar-form" | "navbar-search" ]
            navBarPull="left"  # [ false | right | left ]
        )

        navBar = dhf.navBar(
            brand='DRYX',
            contentList=[itemName,itemName,dropdown],  # list of li, dropdown
            forms=[searchForm, navbarForm],
            dividers=True,
            fixedOrStatic=False,
            location='top',
            responsive=False,
            dark=False
        )
        content += navBar

        navBar = dhf.navBar(
            brand='bot fixed',
            contentList=[itemName,itemName,dropdown],  # list of li, dropdown
            forms=[searchForm, navbarForm],
            dividers=True,
            fixedOrStatic="fixed",
            location='bottom',
            responsive=False,
            dark=False
        )
        content += navBar

        navBar = dhf.navBar(
            brand='top fixed',
            contentList=[itemName,itemName,dropdown],  # list of li, dropdown
            forms=[searchForm, navbarForm],
            dividers=True,
            fixedOrStatic="fixed",
            location='top',
            responsive=False,
            dark=False
        )
        content += navBar

        searchForm = dhf.form(
            formType='navbar-search', #  [ "inline" | "horizontal" | "search" | "navbar-form" | "navbar-search" ]
            navBarPull="right"  # [ false | right | left ]
        )
        pageLink = dhf.a(
            content='page',
            href='#'
        )
        itemName = dhf.li(
            content=pageLink,  # if a subMenu for dropdown this should be <ul>
        )
        outsideNavList = [searchForm]
        insideNavList=[itemName,itemName,dropdown],
        topNavBar = dhf.responsive_navigation_bar(
            shade='dark', #  [ False | 'dark' ]
            brand='resp', # [ image | text ]
            outsideNavList=outsideNavList,
            insideNavList=insideNavList,
            htmlId=False,
        )
        content += topNavBar

        ##Breadcrumbs
        text = "Breadcrumbs"
        content += lt(text)

        activeItem = dhf.li(
            content=pageLink,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle="active",  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )

        Breadcrumbs = dhf.ul(
            itemList=[itemName,itemName,activeItem], # e.g a list links
            unstyled=False,
            inline=True,
            dropDownMenu=False,  #  [ false | true ]
            navStyle=False,  # [ nav | tabs | pills | list ]
            navPull=False,  #  [ false | left | right ]
            navDirection='horizontal',  # [ 'default' | 'stacked' | 'horizontal' ]
            breadcrumb=True,  #  [ False | True ]
            pager=False,
            thumbnails=False,
            mediaList=False
        )
        content += Breadcrumbs


        ##Pagination
        text = "Pagination"
        content += lt(text)

        pagination = dhf.pagination(
            listItems=itemName+itemName+activeItem,
            size='default',
            align='left'
        )
        content += pagination

        pagination = dhf.pagination(
            listItems=itemName+itemName+activeItem,
            size='large',
            align='left'
        )
        content += pagination

        pagination = dhf.pagination(
            listItems=itemName+itemName+activeItem,
            size='small',
            align='centered'
        )
        content += pagination

        pagination = dhf.pagination(
            listItems=itemName+itemName+activeItem,
            size='mini',
            align='right'
        )
        content += pagination

        pager = dhf.ul(
            itemList=[itemName,itemName], # e.g a list links
            unstyled=False,
            inline=False,
            dropDownMenu=False,  #  [ false | true ]
            navStyle=False,  # [ nav | tabs | pills | list ]
            navPull=False,  #  [ false | left | right ]
            navDirection='horizontal',  # [ 'default' | 'stacked' | 'horizontal' ]
            breadcrumb=False,  #  [ False | True ]
            pager=True,
            thumbnails=False,
            mediaList=False
        )

        content += pager

        next = dhf.a(
            content='next',
            href="#",
            tableIndex=False,
            triggerStyle=False # [ False | "dropdown" | "tab" ]
        )
        next = dhf.li(
            content=next,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=True,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager="next"  # [ False | "previous" | "next" ]
        )


        previous = dhf.a(
            content='previous',
            href="#",
            tableIndex=False,
            triggerStyle=False # [ False | "dropdown" | "tab" ]
        )
        previous = dhf.li(
            content=previous,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager="previous"  # [ False | "previous" | "next" ]
        )

        pager = dhf.ul(
            itemList=[next,previous], # e.g a list links
            unstyled=False,
            inline=False,
            dropDownMenu=False,  #  [ false | true ]
            navStyle=False,  # [ nav | tabs | pills | list ]
            navPull=False,  #  [ false | left | right ]
            navDirection='horizontal',  # [ 'default' | 'stacked' | 'horizontal' ]
            breadcrumb=False,  #  [ False | True ]
            pager=True,
            thumbnails=False,
            mediaList=False
        )

        content += pager

        ##Labels and Badges
        text = "Labels and Badges"
        content += lt(text)

        label = dhf.label(
            text='default',
            level='default'
        )
        content += label

        label = dhf.label(
            text='success',
            level='success'
        )
        content += label

        label = dhf.label(
            text='warning',
            level='warning'
        )
        content += label

        label = dhf.label(
            text='important',
            level='important'
        )
        content += label

        label = dhf.label(
            text='info',
            level='info'
        )
        content += label

        label = dhf.label(
            text='inverse',
            level='inverse'
        )
        content += label

        badge = dhf.badge(
            text='1',
            level='default'
        )
        content += badge

        badge = dhf.badge(
            text='2',
            level='success'
        )
        content += badge

        badge = dhf.badge(
            text='3',
            level='warning'
        )
        content += badge

        badge = dhf.badge(
            text='4',
            level='important'
        )
        content += badge

        badge = dhf.badge(
            text='5',
            level='info'
        )
        content += badge

        badge = dhf.badge(
            text='6',
            level='inverse'
        )
        content += badge

        ##Typography
        text = "Typography"
        content += lt(text)

        heroUnit = dhf.heroUnit(
            headline='Hero Unit',
            tagline='This is the hero unit',
            buttonStyle='primary',
            buttonText='push'
        )
        content += heroUnit

        pageHeader = dhf.pageHeader(
            headline='Page Header',
            tagline='... and subtext'
        )
        content += pageHeader

        ##Thumbnails
        text = "Thumbnails"
        content += lt(text)



        Image = dhf.image(
            src='holder.js/200x200/industrial/text:test mediaobject',
            href=False,
            display=False, # [ rounded | circle | polaroid ]
            pull="left", # [ "left" | "right" | "center" ]
            htmlClass=False,
            thumbnail=False,
            width=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        link = dhf.a(
            content=Image,
            href="#",
            tableIndex=False,
            thumbnail=True,
            triggerStyle=False # [ False | "dropdown" | "tab" ]
        )
        itemName = dhf.li(
            content=link,  # if a subMenu for dropdown this should be <ul>
            span=4,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )
        thumbnails = dhf.thumbnails(
            listItems=[itemName]
        )
        content += thumbnails

        thumbnail_div = dhf.thumbnail_div(
            div_content="<h3>header</h3>"+Image+"<small>some text</small>"
        )
        itemName = dhf.li(
            content=thumbnail_div,  # if a subMenu for dropdown this should be <ul>
            span=4,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )
        thumbnails = dhf.thumbnails(
            listItems=[itemName]
        )
        content += thumbnails

        ##Alerts
        text = "Alerts"
        content += lt(text)

        alert = dhf.alert(
            alertText='This is an alert',
            alertHeading='Warning',
            extraPadding=False,
            alertLevel='warning'
        )
        content += alert

        alert = dhf.alert(
            alertText='This is an alert - with more padding',
            alertHeading='Warning',
            extraPadding=True,
            alertLevel='error'
        )
        content += alert
        # UNEDITED #
        # Generate a alert - TBS style #
        # alert #
        # dhf:var:get_alert_-_tbs_style.sublime-snippet #

        ##Progress Bars
        text = "Progress Bars"
        content += lt(text)

        progressBar = dhf.progressBar(
            barStyle="plain",
            precentageWidth="10",
            barLevel="info"
        )
        content += progressBar

        progressBar = dhf.progressBar(
            barStyle="striped",
            precentageWidth="10",
            barLevel="info"
        )
        content += progressBar

        progressBar = dhf.progressBar(
            barStyle="striped-active",
            precentageWidth="50",
            barLevel="danger"
        )
        content += progressBar

        stackedProgressBar = dhf.stackedProgressBar(
            barStyle='plain',
            infoWidth='10',
            successWidth='10',
            warningWidth='10',
            errorWidth='10'
        )
        content += stackedProgressBar

        Image = dhf.image(
            src='holder.js/64x64/industrial/text:test mediaobject',
            href=False,
            display=False, # [ rounded | circle | polaroid ]
            pull="left", # [ "left" | "right" | "center" ]
            htmlClass=False,
            thumbnail=False,
            width=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        link = dhf.a(
            content=Image,
            href='#',
            tableIndex=False,
            pull="left",
            triggerStyle=False # [ False | "dropdown" | "tab" ]
        )
        ##Media Object
        text = "Media Object"
        content += lt(text)
        mediaObject = dhf.mediaObject(
            displayType='div',
            img=link,
            headlineText="Media Object Headline",
            otherContent="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            nestedMediaObjects=False
        )
        content += mediaObject

        mediaObject = dhf.mediaObject(
            displayType='div',
            img=link,
            headlineText="Media Object Headline",
            otherContent="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            nestedMediaObjects=mediaObject
        )
        content += mediaObject

        ##Misc
        text = "Misc"
        content += lt(text)
        well = dhf.well(
            wellText='In a well',
            wellSize='default'
        )
        content += well

        well = dhf.well(
            wellText='In a large well',
            wellSize='large'
        )
        content += well

        well = dhf.well(
            wellText='In a small well',
            wellSize='small'
        )
        content += well

        content += dhf.closeIcon()


        button1 = dhf.button(
            buttonText='ok',
            buttonStyle='default', # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonSize='default',  # [ large | default | small | mini ]
            href="#",
            submit=False,
            block=False,
            disable=False
        )

        button2 = dhf.button(
            buttonText='save',
            buttonStyle='info', # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonSize='default',  # [ large | default | small | mini ]
            href="#",
            submit=False,
            block=False,
            disable=False,
            dataToggle=False
        )

        buttonGroup = dhf.buttonGroup(
            buttonList=[button1,button2],
            format='default'  # [ default | toolbar | vertical ]
        )

        modal = dhf.modal(
            modalHeaderContent="This is a modal",
            modalBodyContent="<p>Put text or a form in here",
            modalFooterContent=buttonGroup,
            htmlId="hookId"
        )
        content += modal

        modalButton = dhf.button(
            buttonText='Launch Modal',
            buttonStyle='default', # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonSize='default',  # [ large | default | small | mini ]
            href="#hookId",
            submit=False,
            block=False,
            disable=False,
            dataToggle="modal"
        )
        content += modalButton

        text = "mediaObject"
        content += lt(text)
        kwargs = {}
        kwargs["displayType"]='div'
        kwargs["img"]=dhf.image(
            src='holder.js/200x200/industrial/text:test mediaobject',  # [ industrial | gray | social ]
        )
        kwargs["headlineText"]='This is a mediaObject'
        kwargs["nestedMediaObjects"]=False
        content += dhf.mediaObject(**kwargs)

        text = "well"
        content += lt(text)
        kwargs = {}
        kwargs["wellText"]=text
        wellSize='default'
        content += dhf.well(**kwargs)

        text = "closeIcon"
        content += lt(text)
        kwargs = {}
        content += dhf.closeIcon(**kwargs)

        text = "button"
        content += lt(text)
        kwargs = {}
        kwargs["buttonText"]=text
        kwargs["buttonStyle"]="default"
        kwargs["buttonSize"]="default"
        kwargs["href"]="#"
        kwargs["submit"]=False
        kwargs["block"]=False
        kwargs["disable"]=False
        oneButton = dhf.button(**kwargs)
        content += oneButton

        text = "button group"
        content += lt(text)
        kwargs = {}
        kwargs["buttonList"]=[oneButton,oneButton,oneButton]
        kwargs["format"]="default"
        content += dhf.buttonGroup(**kwargs)

        link = dhf.a(
            content='a link',
            href="#",
            tableIndex=False,
            triggerStyle=False
        )

        linkItem = dhf.li(
            content=link,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager=False  # [ False | "previous" | "next" ]
        )

        text = "dropdown menu"
        content += lt(text)
        kwargs = {}
        kwargs["buttonColor"]="default"
        kwargs["buttonSize"]="default"
        kwargs["buttonColor"]="default"
        kwargs["menuTitle"]=text
        kwargs["splitButton"]=False
        kwargs["linkList"]=[linkItem,linkItem,linkItem,linkItem,linkItem]
        kwargs["separatedLinkList"]=False
        kwargs["pull"]=False
        kwargs["direction"]="down"
        kwargs["onPhone"]=True
        kwargs["onTablet"]=True
        kwargs["onDesktop"]=True
        content += dhf.dropdown(**kwargs)


        text = "unescape html"
        content += lt(text)
        kwargs = {}
        kwargs["html"] = "&@$^(*^)  123 {}()_+~?><?><"
        content += dhf.unescape_html(**kwargs)

        text = "image"
        content += lt(text)
        kwargs = {}
        kwargs["src"]="http://placehold.it/200x200"
        kwargs["href"]="#"
        kwargs["display"]="False", # [ rounded | circle | polaroid ]
        kwargs["pull"]="left", # [ "left" | "right" | "center" ]
        kwargs["htmlClass"]=False
        kwargs["thumbnail"]=False
        kwargs["width"]=False
        kwargs["onPhone"]=True
        kwargs["onTablet"]=True
        kwargs["onDesktop"]=True
        content += dhf.image(**kwargs)

        text = "thumbnail"
        content += lt(text)
        kwargs = {}
        kwargs["listItems"]=text
        content += dhf.thumbnails(**kwargs)

        text = "label"
        content += lt(text)
        kwargs = {}
        kwargs["text"]=text
        level='default'  # [ "default" | "success" | "warning" | "important" | "info" | "inverse" ]
        content += dhf.label(**kwargs)

        text = "badge"
        content += lt(text)
        kwargs = {}
        kwargs["text"]=text
        level='default'
        content += dhf.badge(**kwargs)

        text = "alert!"
        content += lt(text)
        kwargs = {}
        kwargs["alertText"]=text
        kwargs["alertHeading"]="alertHeading"
        kwargs["extraPadding"]=False
        kwargs["alertLevel"]="warning"
        content += dhf.alert(**kwargs)

        text = "progressBar"
        content += lt(text)
        kwargs = {}
        kwargs["barStyle"]="plain"
        kwargs["precentageWidth"]="10"
        kwargs["barLevel"]="info"
        content += dhf.progressBar(**kwargs)

        text = "stackedProgressBar"
        content += lt(text)
        kwargs = {}
        kwargs["barStyle"]="plain"
        kwargs["infoWidth"]="10"
        kwargs["successWidth"]="10"
        kwargs["warningWidth"]="10"
        kwargs["errorWidth"]="10"
        content += dhf.stackedProgressBar(**kwargs)

        text = "responsive_navigation_bar"
        content += lt(text)
        kwargs = {}
        kwargs["brand"]=False
        kwargs["outsideNavList"]=False
        kwargs["insideNavList"]=False
        kwargs["htmlId"]=False
        kwargs["onPhone"]=True
        kwargs["onTablet"]=True
        kwargs["onDesktop"]=True
        content += dhf.responsive_navigation_bar(**kwargs)

        text = "nav_list"
        content += lt(text)
        kwargs = {}
        kwargs["itemList"]=["list","list","list","list","list",]
        kwargs["pull"]=False
        kwargs["onPhone"]=True
        kwargs["onTablet"]=True
        kwargs["onDesktop"]=True
        content += dhf.nav_list(**kwargs)

        text = "searchbox"
        content += lt(text)
        kwargs = {}
        kwargs["size"]='medium'
        kwargs["placeHolder"]=False
        kwargs["button"]=False
        kwargs["buttonSize"]='small'
        kwargs["buttonColor"]='grey'
        kwargs["navBar"]=False
        kwargs["pull"]=False
        content += dhf.searchbox(**kwargs)

        text = "tabbableNavigation"
        content += lt(text)
        kwargs = {}
        kwargs["contentDictionary"]={"link": "link"}
        kwargs["fadeIn"]=True
        kwargs["direction"]='top'
        content += dhf.tabbableNavigation(**kwargs)

        text = "navBar"
        content += lt(text)
        kwargs = {}
        kwargs["brand"]="brand"
        kwargs["contentList"]=["link", "link"]
        kwargs["dividers"]=False
        kwargs["fixedOrStatic"]=False
        kwargs["location"]='top'
        kwargs["responsive"]=False
        kwargs["dark"]=False
        content += dhf.navBar(**kwargs)

        text = "pagination"
        content += lt(text)
        kwargs = {}
        kwargs["listItems"]="listItems"
        kwargs["size"]="default"
        kwargs["align"]="left"
        content += dhf.pagination(**kwargs)

        text = "grid_row"
        content += lt(text)
        kwargs = {}
        kwargs["responsive"]=True
        kwargs["columns"]=''
        kwargs["htmlId"]=False
        kwargs["htmlClass"]=False
        kwargs["onPhone"]=True
        kwargs["onTablet"]=True
        kwargs["onDesktop"]=True
        content += dhf.grid_row(**kwargs)

        text = "grid_column"
        content += lt(text)
        kwargs = {}
        kwargs["log"]=log
        kwargs["span"]=1
        kwargs["offset"]=0
        kwargs["content"]=text
        kwargs["htmlId"]=False
        kwargs["htmlClass"]=False
        kwargs["onPhone"]=True
        kwargs["onTablet"]=True
        kwargs["onDesktop"]=True
        content += dhf.grid_column(**kwargs)



        text = "p"
        content += lt(text)
        kwargs = {}
        kwargs["content"]=text
        kwargs["lead"]=False
        kwargs["textAlign"]=False
        kwargs["color"]=False
        kwargs["navBar"]=False
        kwargs["onPhone"]=True
        kwargs["onTablet"]=True
        kwargs["onDesktop"]=True
        content += dhf.p(**kwargs)

        text = "emphasizeText"
        content += lt(text)
        kwargs = {}
        kwargs["style"]="em"
        kwargs["text"]=text
        content += dhf.emphasizeText(**kwargs)








        text = "a"
        content += lt(text)
        kwargs = {}
        kwargs["content"]=text
        kwargs["href"]="#"
        kwargs["tableIndex"]=False
        kwargs["triggerStyle"]=False
        content += dhf.a(**kwargs)







        text = "heroUnit"
        content += lt(text)
        kwargs = {}
        kwargs["headline"]=text
        kwargs["tagline"]=text
        kwargs["buttonStyle"]="primary"
        kwargs["buttonText"]=text
        kwargs["buttonHref"]="#"
        content += dhf.heroUnit(**kwargs)

        text = "pageHeader"
        content += lt(text)
        kwargs = {}
        kwargs["headline"]="headline"
        kwargs["tagline"]="tagline"
        content += dhf.pageHeader(**kwargs)


        kwargs = {}
        kwargs["navBar"]=False
        kwargs["content"]=content
        kwargs["htmlId"]=""
        kwargs["extraAttr"]=""
        kwargs["relativeUrlBase"]=""
        kwargs["responsive"]=True
        kwargs["googleAnalyticsCode"]=False
        kwargs["jsFileName"]="main-ck.js"
        bodyContent = dhf.body(**kwargs)

        kwargs = {}
        kwargs["relativeUrlBase"]=''
        kwargs["mainCssFileName"]="main.css"
        kwargs["pageTitle"]=""
        kwargs["extras"]=""
        headContent = dhf.head(**kwargs)

        kwargs = {}
        kwargs["contentType"]=False
        kwargs["content"]=headContent+bodyContent
        content = dhf.htmlDocument(**kwargs)
        if content is not None: cheatsheet.write(content)

