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
    pathToInputDir = moduleDirectory + "/input/"
    pathToInputDataDir = pathToInputDir + "data/"
    pathToOutputDir = moduleDirectory + "/output/"
    pathToOutputDataDir = pathToOutputDir + "data/"

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
    cheatsheet = open(pathToOutputDir +
                      "htdocs/dryxPython_htmlframework_cheatsheet.html", 'w')

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
    info = None
    error = None
    debug = None
    critical = None
    warning = None


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
            color="success",  # [ muted | warning | info | error | success ]
        )
        content += "<br><br><em>Snippet:</em> " + text
        content += "Page constructed from a %s and %s in an %s" % (ct("head"),
                                                                   ct("body"), ct("htmlDocument"))

        ## BASIC GRIDS
        text = "Basic grid HTML"
        content += lt(text)
        text = dhf.p(
            content="grid-row-with-two-columns",
            color="success",  # [ muted | warning | info | error | success ]
        )
        content += "<br><br><em>Snippet:</em> " + text

        placeHolder1 = dhf.image(
            # [ industrial | gray | social ]
            src='holder.js/50x50/social/text:1',
        )
        placeHolder2 = dhf.image(
            # [ industrial | gray | social ]
            src='holder.js/100x50/social/text:2',
        )
        placeHolder3 = dhf.image(
            # [ industrial | gray | social ]
            src='holder.js/200x50/social/text:3 offset 3',
        )
        text = "%s with %s and %s. Use these items to structure and build your pages.<br><br>" % (
            ct("grid_row"), ct("grid_coulmn"), ct("placeHolders"))
        content += text
        column = dhf.grid_column(
            span=1,  # 1-12
            offset=0,  # 1-12
            content=placeHolder1
        )
        row = dhf.grid_row(
            responsive=True,
            columns=column * 12,
        )
        content += row + "<br>"
        column = dhf.grid_column(
            span=2,  # 1-12
            offset=0,  # 1-12
            content=placeHolder2
        )
        row = dhf.grid_row(
            responsive=True,
            columns=column * 6,
        )
        content += row + "<br>"
        column = dhf.grid_column(
            span=3,  # 1-12
            offset=3,  # 1-12
            content=placeHolder3
        )
        row = dhf.grid_row(
            responsive=True,
            columns=column * 2,
        )
        content += row + "<br>"

        ## TEXT
        text = "Typography"
        content += lt(text) + "Use a %s with `lead = True`" % (ct("p"),)
        text = dhf.p(
            content=fillerText,
            lead=True,
            textAlign="left",  # [ left | center | right ]
            color="info",  # [ muted | warning | info | error | success ]
            navBar=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        content += text

        textSnip = "<small>this is small, muted, left aligned %s text wrapped in %s tags</small><br>" % (
            ct("&ltp&gt"), ct("&ltsmall&gt"),)
        text = dhf.p(
            content=textSnip,
            textAlign="left",  # [ left | center | right ]
            color="muted"  # [ muted | warning | info | error | success ]
        )
        content += text

        textSnip = "<strong>this is bold, warning, centred %s text wrapped in %s tags</strong><br>" % (
            ct("&ltp&gt"), ct("&ltstrong&gt"),)
        text = dhf.p(
            content=textSnip,
            textAlign="center",  # [ left | center | right ]
            color="warning"  # [ muted | warning | info | error | success ]
        )
        content += text

        textSnip = "<em>this is italic, error, right aligned %s text wrapped in %s tags</em><br>" % (
            ct("&ltp&gt"), ct("&ltem&gt"),)
        text = dhf.p(
            content=textSnip,
            textAlign="right",  # [ left | center | right ]
            color="error"  # [ muted | warning | info | error | success ]
        )
        content += text

        textSnip = "you can also have success %s text<br>" % (ct("&ltp&gt"),)
        text = dhf.p(
            content=textSnip,
            textAlign="left",  # [ left | center | right ]
            color="success"  # [ muted | warning | info | error | success ]
        )
        content += text

        textSnip = "and you can have info %s text<br>" % (ct("&ltp&gt"),)
        text = dhf.p(
            content=textSnip,
            textAlign="left",  # [ left | center | right ]
            color="info"  # [ muted | warning | info | error | success ]
        )
        content += text

        textSnip = "or the default %s text<br>" % (ct("&ltp&gt"),)
        text = dhf.p(
            content=textSnip,
            textAlign="left",  # [ left | center | right ]
            color="default"  # [ muted | warning | info | error | success ]
        )
        content += text

        content += "use %s to create this abbreviation - hover<br><br>" % (ct("abbr"),)
        kwargs = {}
        kwargs["abbreviation"] = "abbr<br><br>"
        kwargs["fullWord"] = "use `abbr` to create this abbreviation"
        content += dhf.abbr(**kwargs)

        content += "use %s for an address block:<br><br>" % (ct("address"),)
        kwargs = {}
        kwargs["name"] = "name"
        kwargs["addressLine1"] = "addressLine1"
        kwargs["addressLine2"] = "addressLine2"
        kwargs["addressLine3"] = "addressLine3"
        kwargs["phone"] = "phone"
        kwargs["email"] = "email"
        kwargs["twitterHandle"] = "@twitterHandle"
        content += dhf.address(**kwargs)

        kwargs = {}
        kwargs["content"] = "for a quote use %s" % (ct("blockquote"),)
        kwargs["source"] = "this is the source"
        kwargs["pullRight"] = True
        content += dhf.blockquote(**kwargs)

        ## LISTS
        text = "Lists"
        content += lt(text)

        content += "for a unordered list use %s with %s:" % (ct("ul"), ct("li"))
        kwargs = {}
        kwargs["itemList"] = ["list Item", "list Item",
                              "list Item", "list Item", "list Item"]
        kwargs["unstyled"] = False
        kwargs["inline"] = False
        kwargs["dropDownMenu"] = False
        kwargs["navStyle"] = False
        kwargs["navPull"] = False
        kwargs["navDirection"] = "horizontal"
        kwargs["breadcrumb"] = False
        kwargs["pager"] = False
        kwargs["thumbnails"] = False
        kwargs["mediaList"] = False
        content += dhf.ul(**kwargs)

        content += "for a ordered list use %s with %s:" % (ct("ol"), ct("li"))
        kwargs = {}
        kwargs["itemList"] = ["list Item", "list Item",
                              "list Item", "list Item", "list Item"]
        content += dhf.ol(**kwargs)

        content += "you can also have an unstyled list using %s with %s:" % (ct("ul"),
                                                                             ct("li"))
        kwargs = {}
        kwargs["itemList"] = ["list Item", "list Item",
                              "list Item", "list Item", "list Item"]
        kwargs["unstyled"] = True
        kwargs["inline"] = False
        kwargs["dropDownMenu"] = False
        kwargs["navStyle"] = False
        kwargs["navPull"] = False
        kwargs["navDirection"] = "horizontal"
        kwargs["breadcrumb"] = False
        kwargs["pager"] = False
        kwargs["thumbnails"] = False
        kwargs["mediaList"] = False
        content += dhf.ul(**kwargs)

        content += "for a description list use %s" % (ct("descriptionLists"),)
        kwargs = {}
        kwargs["orderedDictionary"] = {"keyOne": "valueOne"}
        kwargs["sideBySide"] = False
        content += dhf.descriptionLists(**kwargs)

        content += "or line them up with `sideBySide = True`"
        kwargs = {}
        kwargs["orderedDictionary"] = {"keyOne": "valueOne"}
        kwargs["sideBySide"] = True
        content += dhf.descriptionLists(**kwargs)

        ## CODE
        text = "Code"
        content += lt(text)

        content += "for inline code use %s<br><br>" % (ct("code"),)

        kwargs = {}
        kwargs["content"] = "for a code block use `%s` with `inline = False`" % (
            ct("code"),)
        kwargs["inline"] = False
        kwargs["scroll"] = False
        content += dhf.code(**kwargs)

        ## TABLES
        text = "Tables"
        content += lt(text)
        content += "for a table use %s, with %s, %s and %ss<br><br>" % (ct("table"),
                                                                        ct("thead"), ct("tbody"), ct("tr"))

        kwargs = {}
        kwargs["content"] = "th"
        kwargs["color"] = False
        th = dhf.th(**kwargs)

        kwargs = {}
        kwargs["content"] = "td"
        kwargs["color"] = False
        td = dhf.td(**kwargs)

        kwargs = {}
        kwargs["cellContent"] = td + td + td + td
        kwargs["color"] = False
        tr = dhf.tr(**kwargs)

        kwargs = {}
        kwargs["content"] = "for a caption use %s" % (ct("tableCaption"),)
        tableCaption = dhf.tableCaption(**kwargs)

        kwargs = {}
        kwargs["trContent"] = th + th + th + th
        thead = dhf.thead(**kwargs)

        kwargs = {}
        kwargs["trContent"] = tr + tr + tr
        tbody = dhf.tbody(**kwargs)

        kwargs = {}
        kwargs["caption"] = tableCaption
        kwargs["thead"] = thead
        kwargs["tbody"] = tbody
        kwargs["striped"] = False
        kwargs["bordered"] = False
        kwargs["hover"] = False
        kwargs["condensed"] = False
        content += dhf.table(**kwargs)

        content += "for a striped table set `striped = True`<br><br>"
        kwargs = {}
        kwargs["caption"] = False
        kwargs["thead"] = thead
        kwargs["tbody"] = tbody
        kwargs["striped"] = True
        kwargs["bordered"] = False
        kwargs["hover"] = False
        kwargs["condensed"] = False
        content += dhf.table(**kwargs)

        content += "for a bordered table set `bordered = True`<br><br>"
        kwargs = {}
        kwargs["caption"] = False
        kwargs["thead"] = thead
        kwargs["tbody"] = tbody
        kwargs["striped"] = False
        kwargs["bordered"] = True
        kwargs["hover"] = False
        kwargs["condensed"] = False
        content += dhf.table(**kwargs)

        content += "for hover table set `hover = True`<br><br>"
        kwargs = {}
        kwargs["caption"] = False
        kwargs["thead"] = thead
        kwargs["tbody"] = tbody
        kwargs["striped"] = False
        kwargs["bordered"] = False
        kwargs["hover"] = True
        kwargs["condensed"] = False
        content += dhf.table(**kwargs)

        kwargs = {}
        kwargs["cellContent"] = td + td + td + td
        kwargs["color"] = "info"
        tri = dhf.tr(**kwargs)

        kwargs = {}
        kwargs["cellContent"] = td + td + td + td
        kwargs["color"] = "warning"
        trw = dhf.tr(**kwargs)

        kwargs = {}
        kwargs["cellContent"] = td + td + td + td
        kwargs["color"] = "error"
        tre = dhf.tr(**kwargs)

        kwargs = {}
        kwargs["cellContent"] = td + td + td + td
        kwargs["color"] = "success"
        trs = dhf.tr(**kwargs)

        kwargs = {}
        kwargs["trContent"] = tri + tre + trs + trw
        tbody = dhf.tbody(**kwargs)

        content += "for condensed table set `condensed = True` - you can also have colored rows<br><br>"
        kwargs = {}
        kwargs["caption"] = False
        kwargs["thead"] = thead
        kwargs["tbody"] = tbody
        kwargs["striped"] = False
        kwargs["bordered"] = False
        kwargs["hover"] = False
        kwargs["condensed"] = True
        content += dhf.table(**kwargs)

        ## FORMS
        text = "Forms"
        content += lt(text)

        kwargs = {}
        kwargs["ttype"] = "email"
        kwargs["placeholder"] = "email"
        kwargs["prepend"] = "@"
        kwargs["span"] = 2
        kwargs["htmlId"] = "email"
        kwargs["focusedInputText"] = "email"
        emailInput = dhf.formInput(**kwargs)

        kwargs = {}
        kwargs["ttype"] = "password"
        kwargs["append"] = "?"
        kwargs["placeholder"] = "password"
        kwargs["span"] = 2
        kwargs["htmlId"] = "password"
        passwordInput = dhf.formInput(**kwargs)

        kwargs = {}
        kwargs["ttype"] = "date"
        kwargs["placeholder"] = "date"
        kwargs["span"] = 2
        kwargs["htmlId"] = "date"
        dateInput = dhf.formInput(**kwargs)

        text = "<br><br>set `formType = 'horizontal'` for horizontal form. "

        content += text

        kwargs = {}
        kwargs["labelText"] = "email"
        kwargs["forId"] = "email"
        emailLabel = dhf.horizontalFormControlLabel(**kwargs)

        kwargs = {}
        kwargs["labelText"] = "date"
        kwargs["forId"] = "date"
        dateLabel = dhf.horizontalFormControlLabel(**kwargs)

        kwargs = {}
        kwargs["labelText"] = "password"
        kwargs["forId"] = "password"
        passwordLabel = dhf.horizontalFormControlLabel(**kwargs)

        kwargs = {}
        kwargs["inputList"] = [emailInput, ]
        emailInputRow = dhf.controlRow(**kwargs)

        kwargs = {}
        kwargs["inputList"] = [passwordInput, ]
        passwordInputRow = dhf.controlRow(**kwargs)

        kwargs = {}
        kwargs["inputList"] = [dateInput, ]
        dateInputRow = dhf.controlRow(**kwargs)

        kwargs = {}
        kwargs["content"] = emailLabel + emailInputRow
        kwargs["validationLevel"] = False
        emailCG = dhf.horizontalFormControlGroup(**kwargs)

        kwargs = {}
        kwargs["content"] = passwordLabel + passwordInputRow
        kwargs["validationLevel"] = False
        passwordCG = dhf.horizontalFormControlGroup(**kwargs)

        kwargs = {}
        kwargs["content"] = dateLabel + dateInputRow
        kwargs["validationLevel"] = False
        dateCG = dhf.horizontalFormControlGroup(**kwargs)

        kwargs = {}
        kwargs["inputList"] = [emailInput, ]
        emailInputRow = dhf.controlRow(**kwargs)
        kwargs = {}
        kwargs["labelText"] = "email"
        kwargs["forId"] = "email"
        emailLabel = dhf.horizontalFormControlLabel(**kwargs)
        kwargs = {}
        kwargs["inputList"] = [emailInput, ]
        emailInputRow = dhf.controlRow(**kwargs)
        kwargs = {}
        kwargs["content"] = emailLabel + emailInputRow
        kwargs["validationLevel"] = False
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
            inputList=[radioCheck, radioCheck2])
        radioCG = dhf.horizontalFormControlGroup(
            content=label + formRow,
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
            inputList=[checkbox, ])
        checkboxCG = dhf.horizontalFormControlGroup(
            content=label + formRow,
            validationLevel=False
        )

        button = dhf.button(
            buttonText='default button',
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='primary',
            buttonSize='default',  # [ large | default | small | mini ]
            href="#",
            submit=True
        )

        button5 = dhf.button(
            buttonText='button5',
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='info',
            buttonSize='default',  # [ large | default | small | mini ]
            href="#",
            submit=True
        )

        button2 = dhf.button(
            buttonText='button2',
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='success',
            buttonSize='default',  # [ large | default | small | mini ]
            href="#",
            submit=True
        )

        button3 = dhf.button(
            buttonText='button3',
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='warning',
            buttonSize='mini',  # [ large | default | small | mini ]
            href="#",
            submit=True
        )

        button4 = dhf.button(
            buttonText='button4',
            # [ efault | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='danger',
            buttonSize='small',  # [ large | default | small | mini ]
            href="#",
            submit=True
        )

        button6 = dhf.button(
            buttonText='button4',
            # [ efault | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='inverse',
            buttonSize='large',  # [ large | default | small | mini ]
            href="#",
            submit=True
        )

        button7 = dhf.button(
            buttonText='link button',
            # [ efault | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='link',
            buttonSize='default',  # [ large | default | small | mini ]
            href="#",
            submit=True
        )

        button8 = dhf.button(
            buttonText='large block-level and disabled',
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='success',
            buttonSize='large',  # [ large | default | small | mini ]
            href="#",
            submit=False,
            block=True,
            disable=True
        )

        text = "form Actions"
        kwargs = {}
        kwargs["primaryButton"] = button
        kwargs["button2"] = button2
        kwargs["button3"] = button3
        kwargs["button4"] = button4
        kwargs["button5"] = button5
        kwargs["inlineHelpText"] = False
        kwargs["blockHelpText"] = False
        formActions = dhf.formActions(**kwargs)

        text = "more form Actions"
        kwargs = {}
        kwargs["primaryButton"] = button6
        kwargs["button2"] = button7
        kwargs["button3"] = button8
        kwargs["inlineHelpText"] = False
        kwargs["blockHelpText"] = False
        moreformActions = dhf.formActions(**kwargs)

        htmlId = "uneditable",
        label = dhf.horizontalFormControlLabel(
            labelText='uneditable input',
            forId=htmlId
        )
        kwargs = {}
        kwargs["placeholder"] = "uneditableInput"
        kwargs["span"] = 2
        kwargs["inlineHelpText"] = False
        kwargs["blockHelpText"] = False
        uneditableInput = dhf.uneditableInput(**kwargs)
        formRow = dhf.controlRow(
            inputList=[uneditableInput, ])
        uneditableInputCG = dhf. (
            content=label + formRow,
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
            inputList=[textarea, ]
        )
        textareaCG = dhf.horizontalFormControlGroup(
            content=label + formRow,
            validationLevel=False
        )

        label = dhf.horizontalFormControlLabel(
            labelText='selection',
            forId='selection'
        )
        kwargs = {}
        kwargs["optionList"] = ["select list", "link", "link", "link", "link", ]
        kwargs["multiple"] = False
        kwargs["span"] = 2
        kwargs["inlineHelpText"] = False
        kwargs["blockHelpText"] = False
        kwargs["required"] = False
        kwargs["disabled"] = False
        select = dhf.select(**kwargs)
        formRow = dhf.controlRow(
            inputList=[select, ])
        selectionCG = dhf.horizontalFormControlGroup(
            content=label + formRow,
            validationLevel=False
        )

        htmlId = "mulSelection",
        label = dhf.horizontalFormControlLabel(
            labelText='multiple selection',
            forId=htmlId
        )
        multipleselection = dhf.select(
            optionList=["select list", "link", "link", "link", "link", ],
            multiple=True,
            span=2,
            htmlId=htmlId,
            inlineHelpText=False,
            blockHelpText=False,
            required=False,
            disabled=False
        )
        formRow = dhf.controlRow(
            inputList=[multipleselection, ])
        multipleselectionCG = dhf.horizontalFormControlGroup(
            content=label + formRow,
            validationLevel=False
        )

        htmlId = "inlineChecks",
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

        inlinecheckboxes = check1 + check2 + check3

        formRow = dhf.controlRow(
            inputList=[inlinecheckboxes, ])
        inlinecheckboxesCG = dhf.horizontalFormControlGroup(
            content=label + formRow,
            validationLevel=False
        )

        goButton = dhf.button(
            buttonText='Go',
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='default',
            buttonSize='default',  # [ large | default | small | mini ]
            href=False,
            submit=False,
            block=False,
            disable=False
        )

        htmlId = "urlInput",
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
            inputList=[url, ])
        urlCG = dhf.horizontalFormControlGroup(
            content=label + formRow,
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
            linkList=[link, link, link, link, link, ],
            separatedLinkList=False,
            pull=False,
            direction='down',
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        htmlId = "numner",
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
            inputList=[inputwithdropdown, ])
        inputwithdropdownCG = dhf.horizontalFormControlGroup(
            content=label + formRow,
            validationLevel=False
        )

        content += "<br><br>For a form item use snippet %s" % (ct("horizontal-form-item"),)
        content += "<small>- this places a %s and a %s within a %s</small>" % (
            ct("horizontalFormControlLabel"), ct("controlRow"), ct("horizontalFormControlGroup"))

        kwargs = {}
        kwargs["content"] = emailCG + passwordCG + dateCG + textareaCG + radioCG + checkboxCG + selectionCG + uneditableInputCG + \
            multipleselectionCG + inlinecheckboxesCG + urlCG + inputwithdropdownCG + \
            formActions + moreformActions
        kwargs["formType"] = "horizontal"
        kwargs["navBarPull"] = False
        content += dhf.form(**kwargs)

        kwargs = {}
        kwargs["buttonText"] = "search me"
        kwargs["span"] = 2
        kwargs["inlineHelpText"] = False
        kwargs["blockHelpText"] = False
        kwargs["focusedInputText"] = False
        kwargs["htmlId"] = 'searchForm'
        searchForm = dhf.searchForm(**kwargs)
        content += searchForm

        ## IMAGES
        text = "Images"
        content += lt(text)
        thisImage = dhf.image(
            src='holder.js/200x200/auto/industrial/text:rounded image',
            href=False,
            display="rounded",  # [ rounded | circle | polaroid ]
            pull="left",  # [ "left" | "right" | "center" ]
            htmlClass=False,
            thumbnail=False,
            width=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        content += thisImage

        thisImage = dhf.image(
            src='holder.js/200x200/auto/industrial/text:circle image',
            href=False,
            display="circle",  # [ rounded | circle | polaroid ]
            pull="left",  # [ "left" | "right" | "center" ]
            htmlClass=False,
            thumbnail=False,
            width=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        content += thisImage

        thisImage = dhf.image(
            src='holder.js/200x200/auto/industrial/text:polaroid image',
            href=False,
            display="polaroid",  # [ rounded | circle | polaroid ]
            pull="left",  # [ "left" | "right" | "center" ]
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

        rightAlignDropdown = dhf.dropdown(
            buttonSize='default',
            buttonColor='default',
            menuTitle='right align',
            splitButton=False,
            linkList=[disabledLink, liveLink, disabledLink,
                      liveLink, liveLink, liveLink, ],
            separatedLinkList=False,
            pull="right",
            direction='down',
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )
        content += rightAlignDropdown

        subMenu = dhf.ul(
            itemList=[liveLink, disabledLink, liveLink, liveLink, liveLink],
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
            linkList=[liveLink, disabledLink, liveLink, liveLink, subMenu],
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
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='default',
            buttonSize='default',  # [ large | default | small | mini ]
            href=False,
            submit=False,
            block=False,
            disable=False
        )
        button2 = dhf.button(
            buttonText='button2',
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='default',
            buttonSize='default',  # [ large | default | small | mini ]
            href=False,
            submit=False,
            block=False,
            disable=False
        )
        button3 = dhf.button(
            buttonText='button3',
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='default',
            buttonSize='default',  # [ large | default | small | mini ]
            href=False,
            submit=False,
            block=False,
            disable=False
        )
        buttonGroup = dhf.buttonGroup(
            buttonList=[button1, button2, button3, ],
            format='default'
        )
        content += buttonGroup

        buttonGroup = dhf.buttonGroup(
            buttonList=[buttonGroup, buttonGroup, buttonGroup],
            format='toolbar'  # [ default | toolbar | vertical ]
        )
        content += buttonGroup

        buttonGroup = dhf.buttonGroup(
            buttonList=[button1, button2, button3, ],
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
            linkList=[liveLink, liveLink, liveLink, liveLink, ],
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
            # e.g a list links
            itemList=[liveLink, disabledLink, liveLink, linkListItem, ],
            unstyled=False,
            inline=False,
            dropDownMenu=False,  # [ false | true ]
            navStyle="tabs",  # [ nav | tabs | pills | list ]
            navPull=False,  # [ false | left | right ]
            navDirection='default',  # [ 'default' | 'stacked' | 'horizontal' ]
            breadcrumb=False,  # [ False | True ]
            pager=False,
            thumbnails=False,
            mediaList=False
        )
        content += tabs

        pills = dhf.ul(
            # e.g a list links
            itemList=[liveLink, disabledLink, liveLink, linkListItem, ],
            unstyled=False,
            inline=False,
            dropDownMenu=False,  # [ false | true ]
            navStyle="pills",  # [ nav | tabs | pills | list ]
            navPull="right",  # [ false | left | right ]
            navDirection='default',  # [ 'default' | 'stacked' | 'horizontal' ]
            breadcrumb=False,  # [ False | True ]
            pager=False,
            thumbnails=False,
            mediaList=False
        )
        content += pills

        stackedTabs = dhf.ul(
            # e.g a list links
            itemList=[liveLink, disabledLink, liveLink, linkListItem, ],
            unstyled=False,
            inline=False,
            dropDownMenu=False,  # [ false | true ]
            navStyle="tabs",  # [ nav | tabs | pills | list ]
            navPull=False,  # [ false | left | right ]
            navDirection='stacked',  # [ 'default' | 'stacked' | 'horizontal' ]
            breadcrumb=False,  # [ False | True ]
            pager=False,
            thumbnails=False,
            mediaList=False
        )
        content += stackedTabs

        droplink = dhf.a(
            content='dropdown',
            href=False,
            tableIndex=False,
            triggerStyle='dropdown'  # [ False | "dropdown" | "tab" ]
        )
        ul = dhf.ul(
            itemList=[link, link, link],  # e.g a list links
            unstyled=False,
            inline=False,
            dropDownMenu=True,  # [ false | true ]
            navStyle=False,  # [ nav | tabs | pills | list ]
            navPull=False,  # [ false | left | right ]
            # [ 'default' | 'stacked' | 'horizontal' ]
            navDirection='horizontal',
            breadcrumb=False,  # [ False | True ]
            pager=False,
            thumbnails=False,
            mediaList=False
        )
        dropdown = dhf.li(
            # if a subMenu for dropdown this should be <ul>
            content=droplink + ul,
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=True,
            pager=False  # [ False | "previous" | "next" ]
        )
        stackedPills = dhf.ul(
            # e.g a list links
            itemList=[liveLink, disabledLink, liveLink, dropdown, linkListItem],
            unstyled=False,
            inline=False,
            dropDownMenu=False,  # [ false | true ]
            navStyle="pills",  # [ nav | tabs | pills | list ]
            navPull=False,  # [ false | left | right ]
            navDirection='default',  # [ 'default' | 'stacked' | 'horizontal' ]
            breadcrumb=False,  # [ False | True ]
            pager=False,
            thumbnails=False,
            mediaList=False
        )
        content += stackedPills

        tabPills = dhf.ul(
            # e.g a list links
            itemList=[liveLink, disabledLink, liveLink, dropdown, linkListItem],
            unstyled=False,
            inline=False,
            dropDownMenu=False,  # [ false | true ]
            navStyle="tabs",  # [ nav | tabs | pills | list ]
            navPull=False,  # [ false | left | right ]
            navDirection='default',  # [ 'default' | 'stacked' | 'horizontal' ]
            breadcrumb=False,  # [ False | True ]
            pager=False,
            thumbnails=False,
            mediaList=False
        )
        content += tabPills

        header = dhf.li(
            # if a subMenu for dropdown this should be <ul>
            content='header title',
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
            # e.g a list links
            itemList=[header, active, link, link,
                      divider, header, active, link, link, ],
            unstyled=False,
            inline=False,
            dropDownMenu=False,  # [ false | true ]
            navStyle="list",  # [ nav | tabs | pills | list ]
            navPull=False,  # [ false | left | right ]
            # [ 'default' | 'stacked' | 'horizontal' ]
            navDirection='horizontal',
            breadcrumb=False,  # [ False | True ]
            pager=False,
            thumbnails=False,
            mediaList=False
        )
        content += navList

        text = "Tabbable Navigation"
        content += lt(text)

        text = dhf.p(
            content="x-tabbableNavigation",
            color="success",  # [ muted | warning | info | error | success ]
        )
        content += "<br><br><em>Snippet:</em> " + text

        tabbableNavigation = dhf.tabbableNavigation(
            contentDictionary={"section 1": "this is section 1 content", "section 2":
                               "this is section 2 content", "section 3": "this is section 3 content", },  # { name : content }
            fadeIn=True,
            direction='top'
        )
        content += tabbableNavigation

        tabbableNavigation = dhf.tabbableNavigation(
            contentDictionary={"section 1": "this is section 1 content", "section 2":
                               "this is section 2 content", "section 3": "this is section 3 content", },  # { name : content }
            fadeIn=True,
            direction='below'
        )
        content += tabbableNavigation

        tabbableNavigation = dhf.tabbableNavigation(
            contentDictionary={"section 1": "this is section 1 content", "section 2":
                               "this is section 2 content", "section 3": "this is section 3 content", },  # { name : content }
            fadeIn=True,
            direction='left'
        )
        content += tabbableNavigation

        tabbableNavigation = dhf.tabbableNavigation(
            contentDictionary={"section 1": "this is section 1 content", "section 2":
                               "this is section 2 content", "section 3": "this is section 3 content", },  # { name : content }
            fadeIn=True,
            direction='right'
        )
        content += tabbableNavigation

        ##Navbar
        text = "Navbar"
        content += lt(text)

        searchForm = dhf.form(
            content='',  # dictionary
            # [ "inline" | "horizontal" | "search" | "navbar-form" | "navbar-search" ]
            formType='navbar-search',
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
            triggerStyle='dropdown'  # [ False | "dropdown" | "tab" ]
        )
        ul = dhf.ul(
            itemList=[link, link, link],  # e.g a list links
            unstyled=False,
            inline=False,
            dropDownMenu=True,  # [ false | true ]
            navStyle=False,  # [ nav | tabs | pills | list ]
            navPull=False,  # [ false | left | right ]
            # [ 'default' | 'stacked' | 'horizontal' ]
            navDirection='horizontal',
            breadcrumb=False,  # [ False | True ]
            pager=False,
            thumbnails=False,
            mediaList=False
        )
        dropdown = dhf.li(
            # if a subMenu for dropdown this should be <ul>
            content=droplink + ul,
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
            # [ "inline" | "horizontal" | "search" | "navbar-form" | "navbar-search" ]
            formType='navbar-form',
            navBarPull="left"  # [ false | right | left ]
        )

        navBar = dhf.navBar(
            brand='DRYX',
            contentList=[itemName, itemName, dropdown],  # list of li, dropdown
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
            contentList=[itemName, itemName, dropdown],  # list of li, dropdown
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
            contentList=[itemName, itemName, dropdown],  # list of li, dropdown
            forms=[searchForm, navbarForm],
            dividers=True,
            fixedOrStatic="fixed",
            location='top',
            responsive=False,
            dark=False
        )
        content += navBar

        text = dhf.p(
            content="responsive-navigation-bar-tmpx",
            color="success",  # [ muted | warning | info | error | success ]
        )
        content += "<br><br><em>Snippet:</em> " + text
        searchForm = dhf.form(
            # [ "inline" | "horizontal" | "search" | "navbar-form" | "navbar-search" ]
            formType='navbar-search',
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
        insideNavList = [itemName, itemName, dropdown]
        topNavBar = dhf.responsive_navigation_bar(
            shade='dark',  # [ False | 'dark' ]
            brand='resp',  # [ image | text ]
            outsideNavList=outsideNavList,
            insideNavList=insideNavList,
            htmlId=False
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
            itemList=[itemName, itemName, activeItem],  # e.g a list links
            unstyled=False,
            inline=True,
            dropDownMenu=False,  # [ false | true ]
            navStyle=False,  # [ nav | tabs | pills | list ]
            navPull=False,  # [ false | left | right ]
            # [ 'default' | 'stacked' | 'horizontal' ]
            navDirection='horizontal',
            breadcrumb=True,  # [ False | True ]
            pager=False,
            thumbnails=False,
            mediaList=False
        )
        content += Breadcrumbs

        ##Pagination
        text = "Pagination"
        content += lt(text)

        pagination = dhf.pagination(
            listItems=itemName + itemName + activeItem,
            size='default',
            align='left'
        )
        content += pagination

        pagination = dhf.pagination(
            listItems=itemName + itemName + activeItem,
            size='large',
            align='left'
        )
        content += pagination

        pagination = dhf.pagination(
            listItems=itemName + itemName + activeItem,
            size='small',
            align='centered'
        )
        content += pagination

        pagination = dhf.pagination(
            listItems=itemName + itemName + activeItem,
            size='mini',
            align='right'
        )
        content += pagination

        pager = dhf.ul(
            itemList=[itemName, itemName],  # e.g a list links
            unstyled=False,
            inline=False,
            dropDownMenu=False,  # [ false | true ]
            navStyle=False,  # [ nav | tabs | pills | list ]
            navPull=False,  # [ false | left | right ]
            # [ 'default' | 'stacked' | 'horizontal' ]
            navDirection='horizontal',
            breadcrumb=False,  # [ False | True ]
            pager=True,
            thumbnails=False,
            mediaList=False
        )

        content += pager

        next = dhf.a(
            content='next',
            href="#",
            tableIndex=False,
            triggerStyle=False  # [ False | "dropdown" | "tab" ]
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
            triggerStyle=False  # [ False | "dropdown" | "tab" ]
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
            itemList=[next, previous],  # e.g a list links
            unstyled=False,
            inline=False,
            dropDownMenu=False,  # [ false | true ]
            navStyle=False,  # [ nav | tabs | pills | list ]
            navPull=False,  # [ false | left | right ]
            # [ 'default' | 'stacked' | 'horizontal' ]
            navDirection='horizontal',
            breadcrumb=False,  # [ False | True ]
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
            src='holder.js/200x200/auto/industrial/text:test mediaobject',
            href=False,
            display=False,  # [ rounded | circle | polaroid ]
            pull="left",  # [ "left" | "right" | "center" ]
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
            triggerStyle=False  # [ False | "dropdown" | "tab" ]
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
            div_content="<h3>header</h3>" + Image + "<small>some text</small>"
        )
        itemName = dhf.li(
            # if a subMenu for dropdown this should be <ul>
            content=thumbnail_div,
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
            src='holder.js/64x64/auto/industrial/text:test mediaobject',
            href=False,
            display=False,  # [ rounded | circle | polaroid ]
            pull="left",  # [ "left" | "right" | "center" ]
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
            triggerStyle=False  # [ False | "dropdown" | "tab" ]
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
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='default',
            buttonSize='default',  # [ large | default | small | mini ]
            href="#",
            submit=False,
            block=False,
            disable=False
        )

        button2 = dhf.button(
            buttonText='save',
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='info',
            buttonSize='default',  # [ large | default | small | mini ]
            href="#",
            submit=False,
            block=False,
            disable=False,
            dataToggle=False
        )

        buttonGroup = dhf.buttonGroup(
            buttonList=[button1, button2],
            format='default'  # [ default | toolbar | vertical ]
        )

        modal = dhf.modals.modal(
            modalHeaderContent="This is a modal",
            modalBodyContent="<p>Put text or a form in here",
            modalFooterContent=buttonGroup,
            htmlId="hookId"
        )
        content += modal

        modalButton = dhf.button(
            buttonText='Launch Modal',
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='default',
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
        kwargs["displayType"] = 'div'
        kwargs["img"] = dhf.image(
            # [ industrial | gray | social ]
            src='holder.js/200x200/auto/industrial/text:test mediaobject',
        )
        kwargs["headlineText"] = 'This is a mediaObject'
        kwargs["nestedMediaObjects"] = False
        content += dhf.mediaObject(**kwargs)

        text = "well"
        content += lt(text)
        kwargs = {}
        kwargs["wellText"] = text
        wellSize = 'default'
        content += dhf.well(**kwargs)

        text = "closeIcon"
        content += lt(text)
        kwargs = {}
        content += dhf.closeIcon(**kwargs)

        text = "button"
        content += lt(text)
        kwargs = {}
        kwargs["buttonText"] = text
        kwargs["buttonStyle"] = "default"
        kwargs["buttonSize"] = "default"
        kwargs["href"] = "#"
        kwargs["submit"] = False
        kwargs["block"] = False
        kwargs["disable"] = False
        oneButton = dhf.button(**kwargs)
        content += oneButton

        text = "button group"
        content += lt(text)
        kwargs = {}
        kwargs["buttonList"] = [oneButton, oneButton, oneButton]
        kwargs["format"] = "default"
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
        kwargs["buttonColor"] = "default"
        kwargs["buttonSize"] = "default"
        kwargs["buttonColor"] = "default"
        kwargs["menuTitle"] = text
        kwargs["splitButton"] = False
        kwargs["linkList"] = [linkItem, linkItem, linkItem, linkItem, linkItem]
        kwargs["separatedLinkList"] = False
        kwargs["pull"] = False
        kwargs["direction"] = "down"
        kwargs["onPhone"] = True
        kwargs["onTablet"] = True
        kwargs["onDesktop"] = True
        content += dhf.dropdown(**kwargs)

        text = "unescape html"
        content += lt(text)
        kwargs = {}
        kwargs["html"] = "&@$^(*^)  123 {}()_+~?><?><"
        content += dhf.unescape_html(**kwargs)

        text = "image"
        content += lt(text)
        kwargs = {}
        kwargs["src"] = "http://placehold.it/200x200"
        kwargs["href"] = "#"
        kwargs["display"] = "False",  # [ rounded | circle | polaroid ]
        kwargs["pull"] = "left",  # [ "left" | "right" | "center" ]
        kwargs["htmlClass"] = False
        kwargs["thumbnail"] = False
        kwargs["width"] = False
        kwargs["onPhone"] = True
        kwargs["onTablet"] = True
        kwargs["onDesktop"] = True
        content += dhf.image(**kwargs)

        text = "thumbnail"
        content += lt(text)
        kwargs = {}
        kwargs["listItems"] = text
        content += dhf.thumbnails(**kwargs)

        text = "label"
        content += lt(text)
        kwargs = {}
        kwargs["text"] = text
        # [ "default" | "success" | "warning" | "important" | "info" | "inverse" ]
        level = 'default'
        content += dhf.label(**kwargs)

        text = "badge"
        content += lt(text)
        kwargs = {}
        kwargs["text"] = text
        level = 'default'
        content += dhf.badge(**kwargs)

        text = "alert!"
        content += lt(text)
        kwargs = {}
        kwargs["alertText"] = text
        kwargs["alertHeading"] = "alertHeading"
        kwargs["extraPadding"] = False
        kwargs["alertLevel"] = "warning"
        content += dhf.alert(**kwargs)

        text = "progressBar"
        content += lt(text)
        kwargs = {}
        kwargs["barStyle"] = "plain"
        kwargs["precentageWidth"] = "10"
        kwargs["barLevel"] = "info"
        content += dhf.progressBar(**kwargs)

        text = "stackedProgressBar"
        content += lt(text)
        kwargs = {}
        kwargs["barStyle"] = "plain"
        kwargs["infoWidth"] = "10"
        kwargs["successWidth"] = "10"
        kwargs["warningWidth"] = "10"
        kwargs["errorWidth"] = "10"
        content += dhf.stackedProgressBar(**kwargs)

        text = "responsive_navigation_bar"
        content += lt(text)
        kwargs = {}
        kwargs["brand"] = False
        kwargs["outsideNavList"] = False
        kwargs["insideNavList"] = False
        kwargs["htmlId"] = False
        kwargs["onPhone"] = True
        kwargs["onTablet"] = True
        kwargs["onDesktop"] = True
        content += dhf.responsive_navigation_bar(**kwargs)

        text = "nav_list"
        content += lt(text)
        kwargs = {}
        kwargs["itemList"] = ["list", "list", "list", "list", "list", ]
        kwargs["pull"] = False
        kwargs["onPhone"] = True
        kwargs["onTablet"] = True
        kwargs["onDesktop"] = True
        content += dhf.nav_list(**kwargs)

        text = "searchbox"
        content += lt(text)
        kwargs = {}
        kwargs["size"] = 'medium'
        kwargs["placeHolder"] = False
        kwargs["button"] = False
        kwargs["buttonSize"] = 'small'
        kwargs["buttonColor"] = 'grey'
        kwargs["navBar"] = False
        kwargs["pull"] = False
        content += dhf.searchbox(**kwargs)

        text = "tabbableNavigation"
        content += lt(text)
        kwargs = {}
        kwargs["contentDictionary"] = {"link": "link"}
        kwargs["fadeIn"] = True
        kwargs["direction"] = 'top'
        content += dhf.tabbableNavigation(**kwargs)

        text = "navBar"
        content += lt(text)
        kwargs = {}
        kwargs["brand"] = "brand"
        kwargs["contentList"] = ["link", "link"]
        kwargs["dividers"] = False
        kwargs["fixedOrStatic"] = False
        kwargs["location"] = 'top'
        kwargs["responsive"] = False
        kwargs["dark"] = False
        content += dhf.navBar(**kwargs)

        text = "pagination"
        content += lt(text)
        kwargs = {}
        kwargs["listItems"] = "listItems"
        kwargs["size"] = "default"
        kwargs["align"] = "left"
        content += dhf.pagination(**kwargs)

        text = "grid_row"
        content += lt(text)
        kwargs = {}
        kwargs["responsive"] = True
        kwargs["columns"] = ''
        kwargs["htmlId"] = False
        kwargs["htmlClass"] = False
        kwargs["onPhone"] = True
        kwargs["onTablet"] = True
        kwargs["onDesktop"] = True
        content += dhf.grid_row(**kwargs)

        text = "grid_column"
        content += lt(text)
        kwargs = {}
        kwargs["span"] = 1
        kwargs["offset"] = 0
        kwargs["content"] = text
        kwargs["htmlId"] = False
        kwargs["htmlClass"] = False
        kwargs["onPhone"] = True
        kwargs["onTablet"] = True
        kwargs["onDesktop"] = True
        content += dhf.grid_column(**kwargs)

        text = "p"
        content += lt(text)
        kwargs = {}
        kwargs["content"] = text
        kwargs["lead"] = False
        kwargs["textAlign"] = False
        kwargs["color"] = False
        kwargs["navBar"] = False
        kwargs["onPhone"] = True
        kwargs["onTablet"] = True
        kwargs["onDesktop"] = True
        content += dhf.p(**kwargs)

        text = "emphasizeText"
        content += lt(text)
        kwargs = {}
        kwargs["style"] = "em"
        kwargs["text"] = text
        content += dhf.emphasizeText(**kwargs)

        text = "a"
        content += lt(text)
        kwargs = {}
        kwargs["content"] = text
        kwargs["href"] = "#"
        kwargs["tableIndex"] = False
        kwargs["triggerStyle"] = False
        content += dhf.a(**kwargs)

        text = "heroUnit"
        content += lt(text)
        kwargs = {}
        kwargs["headline"] = text
        kwargs["tagline"] = text
        kwargs["buttonStyle"] = "primary"
        kwargs["buttonText"] = text
        kwargs["buttonHref"] = "#"
        content += dhf.heroUnit(**kwargs)

        text = "pageHeader"
        content += lt(text)
        kwargs = {}
        kwargs["headline"] = "headline"
        kwargs["tagline"] = "tagline"
        content += dhf.pageHeader(**kwargs)

        kwargs = {}
        kwargs["navBar"] = False
        kwargs["content"] = content
        kwargs["htmlId"] = ""
        kwargs["extraAttr"] = ""
        kwargs["relativeUrlBase"] = ""
        kwargs["responsive"] = True
        kwargs["googleAnalyticsCode"] = False
        kwargs["jsFileName"] = "main-ck.js"
        bodyContent = dhf.body(**kwargs)

        kwargs = {}
        kwargs["relativeUrlBase"] = ''
        kwargs["mainCssFileName"] = "main.css"
        kwargs["pageTitle"] = ""
        kwargs["extras"] = ""
        headContent = dhf.head(**kwargs)

        kwargs = {}
        kwargs["contentType"] = False
        kwargs["content"] = headContent + bodyContent
        content = dhf.htmlDocument(**kwargs)
        if content is not None:
            cheatsheet.write(content)
