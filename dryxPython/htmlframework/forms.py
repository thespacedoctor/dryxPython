#!/usr/local/bin/python
# encoding: utf-8
"""
_dryxTBS_forms
=============================
:Summary:
    Forms partial for the dryxTwitterBootstrap module

:Author:
    David Young

:Date Created:
    April 16, 2013

:dryx syntax:
    - ``xxx`` = come back here and do some more work
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script please email me: d.r.young@qub.ac.uk
"""

###################################################################
# CLASSES                                                         #
###################################################################
# xxx-replace
## LAST MODIFIED : December 12, 2012
## CREATED : December 12, 2012
## AUTHOR : DRYX


class HTMLDivForm():

    """
    Create the building blocks of an HTML form -- a bunch of ``<div>``.

    **Variable Attributes:**
      - ``labelList`` -- list of labels to appear on the form
      - ``textboxList`` -- list of input textboxs to appear on the form
      - ``selectList`` -- list of dropdown select lists to appear on the form
      - ``checkboxList`` -- list of the radio buttons needed
      - ``buttonList`` -- list of the buttons needed (strings)
      - ``numberOfRows`` -- number of rows for the form

    """
    ###################### GLOBAL IMPORTS ######################
    ################ PUBLIC VARIABLE ATTRIBUTES ################
    labelList = []
    textboxList = []
    selectList = []
    checkboxList = []
    buttonList = []
    numberOfRows = 1
    ############### PRIVATE VARIABLE ATTRIBUTES ###############
    ################ INSTANSIATION METHOD ######################

    def __init__(self):
        pass

    ############### METHODS ####################################
    def get_objects(self):
        """
        Returns the components to make an HTML form:
         - ``labelDict`` -- a dictionary of dictionaries .. **key**:*label name*, **value**:*dictionary of HTML attributes*.
         - ``textDict`` -- a dictionary of dictionaries .. **key**:*textbox name*, **value**:*dictionary of HTML attributes*.
         - ``selectDict`` -- a dictionary of dictionaries .. **key**:*dropdown menu name*, **value**:*dictionary of HTML attributes*.
         - ``checkboxDict`` -- a dictionary of dictionaries .. **key**:*checkbox name*, **value**:*dictionary of HTML attributes*.
         - ``buttonDict`` -- a dictionary of dictionaries .. **key**:*button name*, **value**:*dictionary of HTML attributes*.
         - ``rowList`` -- a list of dictionaries containing HTML attributes for the row.
         - ``formContent`` -- a dictionary containing of HTML attributes for the form content.
         - ``form`` -- a dictionary containing of HTML attributes for the form.
        """

        #### GENERATE FORM LABELS (DIVS) ####
        #--------------------------------------------------------------------------------#
        labelDict = {}
        for label in self.labelList:
            htmlId = label.replace(' ', '').replace(':', '')
            labelDict[label] = dict(
                tag="div",
                htmlId=htmlId,
                htmlClass="labels",
                blockContent=label
            )

        #### GENERATE TEXTBOXES (INPUTS) ####
        #--------------------------------------------------------------------------------#
        textDict = {}
        for text in self.textboxList:
            name = text.replace(' ', '')
            textDict[text] = dict(
                htmlClass="input-medium",
                tag="input",
                type="text",
                placeholder=text,
                name=name
            )

        #### GERERATE SELECTS ####
        #--------------------------------------------------------------------------------#
        selectDict = {}
        for select in self.selectList:
            htmlId = select.replace(' ', '')
            htmlClass = select + "Select"
            selectDict[select] = dict(
                tag="select",
                htmlId=htmlId,
                htmlClass=htmlClass
            )

        #### GERERATE CHECKBOXES ####
        #--------------------------------------------------------------------------------#
        checkboxDict = {}
        for checkbox in self.checkboxList:
            htmlId = checkbox.replace(' ', '')
            checkboxDict[checkbox] = dict(
                tag="input",
                type="checkbox",
                name=checkbox,
                value=checkbox,
                htmlId=htmlId
            )

        #### GENERATE BUTTONS ####
        #--------------------------------------------------------------------------------#
        buttonDict = {}
        for button in self.buttonList:
            htmlId = button.replace(' ', '').replace('(', '').replace(')', '')
            buttonDict[button] = dict(
                tag="button",
                htmlClass="greyButton",
                blockContent=button,
                htmlId=htmlId
            )

        #### GENERATE THE ROWS ####
        #--------------------------------------------------------------------------------#
        i = 1
        rowList = []
        rowList.append("NULL")
        while(i <= self.numberOfRows):
            rowName = "row" + "{0:02.0f}".format(i)
            rowList.append(
                dict(
                    tag="div",
                    htmlClass="divHorizontalKids",
                    htmlId=rowName
                )
            )
            i += 1

        form = dict(
            tag="form",
            htmlClass="form",
            method="post",
        )
        formContent = dict(
            tag="div",
            htmlClass="formContent"
        )

        return labelDict, textDict, selectDict, checkboxDict, buttonDict, rowList, formContent, form


class dummy():

    """
    Create the building blocks of an HTML form -- a bunch of ``<div>``.

    **Variable Attributes:**
      - ``labelList`` -- list of labels to appear on the form
      - ``textboxList`` -- list of input textboxs to appear on the form
      - ``selectList`` -- list of dropdown select lists to appear on the form
      - ``checkboxList`` -- list of the radio buttons needed
      - ``buttonList`` -- list of the buttons needed (strings)
      - ``numberOfRows`` -- number of rows for the form

    """

    ## LAST MODIFIED : YYMD
    ## CREATED : YYMD
    ## AUTHOR : DRYX
    def functionName(
            self):
        """one-line summary

        **Key Arguments:**
            - ``dbConn`` -- mysql database connection
            - ``log`` -- logger

        **Return:**
            - ```` --

        **Todo**
        - [ ] when complete, clean functionName function & add logging
        """
        ################ > IMPORTS ################
        ## STANDARD LIB ##
        ## THIRD PARTY ##
        ## LOCAL APPLICATION ##
        pass


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# # xxx-replace
# ## LAST MODIFIED : December 12, 2012
# ## CREATED : December 12, 2012
# ## AUTHOR : DRYX
# def get_fieldset(attributeDict):
#   """Create a ``fieldset`` HTML code block with legend

#   **Key Arguments:**
#     - ``attributeDict`` -- dictionary of the following keywords:
#       - ``htmlClass`` -- the html element class
#       - ``htmlId`` -- the html element id
#       - ``blockContent`` -- actual content to be placed in html code block
#       - ``jsEvents`` -- inline javascript event
#       - ``extraAttr`` -- extra incline css attributes and/or handles
#       - ``legend`` -- fieldset legend

#   **Return:**
#     - ``block``

#   attributeDict template -- dict(htmlClass=___,
#                                   htmlId=___,
#                                   jsEvents=___,
#                                   extraAttr=___,
#                                   blockContent=___,
#                                   legend=___
#                                 )
#   """
#   ################ > IMPORTS ################

#   ################ > VARIABLE SETTINGS ######
#   block = "<fieldset "  # THE HTML BLOCK
#   d = attributeDict

#   ################ >ACTION(S) ################
#   ## SET THE ATTRIBUTES
#   if d.has_key("htmlClass"):
#     block += """class="%s" """ % (d["htmlClass"],)
#   if d.has_key("htmlId"):
#     block += """id="%s" """ % (d["htmlId"],)
#   if d.has_key("jsEvents"):
#     block += """%s """ % (d["jsEvents"],)
#   if d.has_key("extraAttr"):
#     block += """%s """ % (d["extraAttr"],)
#   block += ">"

#   if d["legend"]:
#     block += "<legend>%s</legend>" % (d["legend"],)

#   ## SET THE CONTENT
#   if d.has_key("blockContent"):
#     block += str(d["blockContent"])

#   ## CLOSE THE BLOCK
#   if d.has_key("htmlId"):
#     block += "</fieldset><!--- /#%s --->" % (d["htmlId"],)
#   else:
#     block += "</fieldset>"

#   return block

# # xxx-replace
# ## LAST MODIFIED : December 12, 2012
# ## CREATED : December 12, 2012
# ## AUTHOR : DRYX
# def get_input_block(attributeDict):
#   """The HTML5 input tag used mainly in forms

#   **Key Arguments:**
#     - ``attributeDict`` -- dictionary of the following keywords:
#     - ``tag`` -- input, textarea
#     - ``htmlClass`` -- the html element class
#     - ``htmlId`` -- the html element id
#     - ``blockContent`` -- actual content to be placed in html code block
#     - ``jsEvents`` -- inline javascript event
#     - ``extraAttr`` -- extra incline css attributes and/or handles
#     - ``name`` -- an extra hook (much like "id")
#     - ``type`` -- HTML input types = color, date, datetime, datetime-local, email, month, number, range, search, tel, time, url, week
#     - ``placeholder`` -- text to be displayed by default in the input box
#     - ``required`` -- make input required (boolean)
#     - ``autofocus`` -- make this the auofocus element of the form (i.e. place cursor here)
#     - ``maxlength`` -- maximum character length for the form
#     - ``row`` -- number of rows for a *textarea* (i.e. height of the textbox)

#   **Returns**
#     - ``block`` -- the input HTML code block

#   attributeDict template --
#       dict(
#             tag=___,
#             htmlClass=___,
#             htmlId=___,
#             jsEvents=___,
#             extraAttr=___,
#             blockContent=___,
#             name=___,
#             type=___,
#             placeholder=___,
#             required=___,
#             autofocus=___,
#             maxlength=___,
#             row=___,
#             value=___
#           )
#   """
  ################ > IMPORTS ################

  ################ > VARIABLE SETTINGS ######
  # d = attributeDict

  # ################ >ACTION(S) ################
  # if d.has_key("label"):
  #   block = """<label>%s<label>\n<%s """ % (d["label"],d["tag"],)
  # else:
  #   block = """<%s """ % (d["tag"],)

  # if d.has_key("htmlClass"):
  #   block += """class="%s" """ % (d["htmlClass"],)
  # if d.has_key("htmlId"):
  #   block += """id="%s" """ % (d["htmlId"],)
  # if d.has_key("jsEvents"):
  #   block += """%s """ % (d["jsEvents"],)
  # if d.has_key("extraAttr"):
  #   block += """%s """ % (d["extraAttr"],)
  # if d.has_key("name"):
  #   block += """name="%s" """ % (d["name"],)
  # if d.has_key("type"):
  #   block += """type="%s" """ % (d["type"],)
  # if d.has_key("placeholder"):
  #   block += """placeholder="%s" """ % (d["placeholder"],)
  # if d.has_key("maxlength"):
  #   block += """maxlength="%s" """ % (d["maxlength"],)
  # if d.has_key("required") and d["required"]:
  #   block += """required """
  # if d.has_key("autofocus"):
  #   block += """autofocus """
  # if d.has_key("value"):
  #   block += """value """
  # block += ">"

  # ## SET THE CONTENT
  # if d.has_key("blockContent"):
  #   block += str(d["blockContent"])
  # ## CLOSE THE BLOCK
  # if d.has_key("htmlId"):
  #   block += "</%s><!--- /#%s --->" % (d["tag"],d["htmlId"],)
  # else:
  #   block += "</%s>" % (d["tag"],)

  # return block


## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def searchForm(
        buttonText="",
        span=2,
        inlineHelpText=False,
        blockHelpText=False,
        focusedInputText=False,
        htmlId=False):
    """Generate a search-form - TBS style

    **Key Arguments:**
        - ``buttonText`` -- the button text
        - ``span`` -- column span
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line
        - ``focusedInputText`` -- make the input focused by providing some initial editable input text
        - ``htmlId`` -- htmlId

    **Return:**
        - ``searchForm`` -- the search-form
    """
    if span:
        span = "span%s" % (span,)
    else:
        span = ""

    if not focusedInputText:
        focusedInputText = ""
        focusId = ""
    else:
        focusId = "focusedInput"

    if inlineHelpText:
        inlineHelpText = """<span class="help-inline">%s</span>""" % (inlineHelpText,)
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%s</span>""" % (blockHelpText,)
    else:
        blockHelpText = ""

    if not htmlId:
        htmlId = ""

    searchForm = """
    <form class="form-search">
    <div class="input-append">
      <input type="text" class="search-query %s" id="%s"  id="%s" value="%s">
      <button type="submit" class="btn">%s</button>
            %s%s
    </div>
    </form>""" % (span, htmlId, focusId, focusedInputText, buttonText, inlineHelpText, blockHelpText)

    return searchForm


## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def form(
        content="",
        formType="inline",
        postToScript="",
        htmlId=False,
        navBarPull=False,
        postInBackground=False,
        redirectUrl=False,
        span=False,
        offset=False):
    """Generate a form - TBS style

    **Key Arguments:**
        - ``content`` -- the content
        - ``formType`` -- the type if the form required [ "inline" | "horizontal" | "search" | "navbar-form" | "navbar-search" ]
        - ``postToScript`` -- the script to post the form values to
        - ``htmlId`` -- the id for the form
        - ``navBarPull`` -- align the form is in a navBar [ false | right | left ]
        - ``postInBackground`` -- submit form in background without refreshing page
        - ``redirectUrl`` -- url to redirect to after form is submitted

    **Return:**
        - ``inlineForm`` -- the inline form
    """
    falseList = [navBarPull, ]

    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""

    [navBarPull, ] = falseList

    if span is False:
        span = ""
    else:
        span = "span%s" % (span,)

    if offset is False:
        offset = ""
    else:
        offset = "offset%s" % (offset,)

    if postInBackground is True:
        postInBackground = "postInBackground"
    else:
        postInBackground = ""

    if redirectUrl is not False:
        redirectUrl = formInput(
            # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
            ttype='text',
            htmlId="redirectURL",
            defaultValue=redirectUrl,
            hidden=True
        )
    else:
        redirectUrl = ""

    if navBarPull:
        navBarPull = "pull-%s" % (navBarPull,)

    thisList = ["inline", "horizontal", "search"]
    if formType in thisList:
        formType = """form-%s""" % (formType,)

    htmlInput = ""
    if formType == "navbar-search":
        htmlInput += """<input type="text" class="search-query" placeholder="search">"""

    if formType == "navbar-form":
        htmlInput += """<input type="text" class="span2">
        <button type="submit" class="btn">Submit</button>"""

    if htmlId:
        htmlId = """id="%s" """ % (htmlId,)
    else:
        htmlId = ""

    form = """<form class="%s %s %s %s %s" %s action="%s" method="post" target="_blank">%s%s%s</form>""" % (
        formType, navBarPull, postInBackground, span, offset, htmlId, postToScript, content, htmlInput, redirectUrl)

    return form


## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def horizontalFormControlGroup(
        content="",
        validationLevel=False,
        hidden=False):
    """Generate a horizontal form control group (row) - TBS style

    **Key Arguments:**
        - ``content`` -- the content
        - ``validationLevel`` -- validation level [ warning | error | info | success ]
        - ``hidden`` -- hide the CG from the user?

    **Return:**
        - ``horizontalFormControlGroup`` -- the horizontal form control group
    """
    falseList = [validationLevel, ]

    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""

    [validationLevel, ] = falseList

    if hidden:
        hidden = """hidden"""
    else:
        hidden = ""

    horizontalFormControlGroup = """
        <div class="control-group %(validationLevel)s %(hidden)s">
            %(content)s
        </div>""" % locals()

    return horizontalFormControlGroup


## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def horizontalFormControlLabel(
        labelText="",
        forId=False):
    """set a horizontal form label

    **Key Arguments:**
        - ``labelText`` -- the label text
        - ``forId`` -- what is the label for (id of the associated object)?

    **Return:**
        - ``horizontalFormRowLabel`` -- the horizontalFormRowLabel
    """
    if forId is False:
        forId = ""

    horizontalFormRowLabel = """<label class="control-label" for="%s">%s</label>""" % (
        forId, labelText, )

    return horizontalFormRowLabel


## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def formInput(
        ttype="text",
        placeholder="",
        span=2,
        htmlId=False,
        searchBar=False,
        pull=False,
        prepend=False,
        append=False,
        button1=False,
        button2=False,
        prependDropdown=False,
        appendDropdown=False,
        inlineHelpText=False,
        blockHelpText=False,
        focusedInputText=False,
        required=False,
        disabled=False,
        defaultValue=False,
        hidden=False):
    """Generate a form input - TBS style

    **Key Arguments:**
        - ``ttype`` -- [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
        - ``placeholder`` -- the placeholder text
        - ``span`` -- column span
        - ``htmlId`` -- html id
        - ``searchBar`` -- is this input a searchbar?
        - ``pull`` -- [ false | right | left ] align form
        - ``prepend`` -- prepend text to the input.
        - ``append`` -- append text to the input.
        - ``button1`` -- do you want a button associated with the input?
        - ``button2`` -- as above for a 2nd button
        - ``appendDropdown`` -- do you want a appended button-dropdown associated with the input?
        - ``prependDropdown`` -- do you want a prepended button-dropdown associated with the input?
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line
        - ``focusedInputText`` -- make the input focused by providing some initial editable input text
        - ``required`` -- required attribute if the field is not optional
        - ``disabled`` -- add the disabled attribute on an input to prevent user input
        - ``defaultValue`` -- a default value to be passed to action script
        - ``hidden`` -- hide the CG from the user?

    **Return:**
        - ``input`` -- the input
    """
    prependContent = False
    appendContent = False
    inputId = False
    searchClass = False
    prependClass = False
    appendClass = False

    if hidden:
        hidden = """hidden"""
    else:
        hidden = ""

    falseList = [searchBar, span, prepend, prependContent, append,
                 appendContent, inputId, pull, htmlId, appendClass, prependClass]

    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""

    [searchBar, span, prepend, prependContent, append, appendContent,
        inputId, pull, htmlId, appendClass, prependClass] = falseList

    if pull:
        pull = "pull-%s" % (pull,)

    if span:
        span = "span%s" % (span,)

    if searchBar:
        searchClass = "search-query"
    else:
        searchClass = ""

    if prepend:
        prependClass = "input-prepend"
        prependContent = """<span class="add-on">%s</span>""" % (prepend,)

    if append:
        appendClass = "input-append"
        appendContent = """<span class="add-on">%s</span>""" % (append,)

    if prepend:
        if append:
            inputId = "appendedPrependedInput "
        else:
            inputId = "prependedInput "
    elif append:
        inputId = "appendedInput "

    if button1:
        appendClass = "input-append"
        appendContent = button1
        inputId = "appendedInputButton "

    if button2:
        appendClass = "input-append"
        appendContent = appendContent + button2
        inputId = "appendedInputButtons "

    if appendDropdown:
        appendClass = "input-append"
        inputId = "appendedDropdownButton "
        appendContent = """
        <div class="btn-group">
            %s
        </div>""" % (appendDropdown,)

    if prependDropdown:
        prependClass = "input-prepend"
        inputId = "prependedDropdownButton "
        prependContent = """
        <div class="btn-group">
            %s
        </div>""" % (prependDropdown,)

    step = ""
    if ttype == "float":
        step = """ step="any" """
        ttype = "number"

    if prependDropdown and appendDropdown:
        inputId = "appendedPrependedDropdownButton "

    if inlineHelpText:
        inlineHelpText = """<span class="help-inline">%s</span>""" % (inlineHelpText,)
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%s</span>""" % (blockHelpText,)
    else:
        blockHelpText = ""

    if not focusedInputText:
        focusedInputText = ""
        focusId = ""
    else:
        focusedInputText = """value="%s" """ % (focusedInputText,)
        focusId = "focusedInput "

    if required:
        required = """required"""
    else:
        required = ""

    if disabled:
        disabled = """disabled"""
        disabledId = "disabledId "
    else:
        disabled = ""
        disabledId = ""

    if defaultValue:
        defaultValue = """value=%(defaultValue)s """ % locals()
    else:
        defaultValue = ""

    formInput = """
        <div class="%s %s %s">
            %s
            <input class="%s %s %s" id="%s%s%s%s" %s type="%s" %s placeholder="%s" %s %s name="%s" %s>
            %s
        </div>%s%s
        """ % (prependClass, appendClass, hidden, pull, prependContent, searchClass, span, htmlId, inputId, focusId, disabledId, focusedInputText, ttype, step, placeholder, required, disabled, htmlId, defaultValue, appendContent, inlineHelpText, blockHelpText)

    # formInput = """<input class="%s %s" id="%s%s%s%s" value="%s" type="%s" placeholder="%s" %s %s>""" % (span, searchClass, htmlId, inputId, focusId, disabledId, focusedInput, ttype, placeholder, required, disabled)

    return formInput


## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def textarea(
        rows="",
        span=2,
        placeholder="",
        htmlId=False,
        inlineHelpText=False,
        blockHelpText=False,
        focusedInputText=False,
        required=False,
        disabled=False):
    """Generate a textarea - TBS style

    **Key Arguments:**
        - ``rows`` -- the number of rows the text area should span
        - ``span`` -- column span
        - ``placeholder`` -- the placeholder text
        - ``htmlId`` -- html id for item
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line
        - ``focusedInputText`` -- make the input focused by providing some initial editable input text
        - ``required`` -- required attribute if the field is not optional
        - ``disabled`` -- add the disabled attribute on an input to prevent user input

    **Return:**
        - ``textarea`` -- the textarea
    """
    if span:
        span = "span%s" % (span,)
    else:
        span = ""

    if inlineHelpText:
        inlineHelpText = """<span class="help-inline">%s</span>""" % (inlineHelpText,)
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%s</span>""" % (blockHelpText,)
    else:
        blockHelpText = ""

    if not focusedInputText:
        focusedInputText = ""
        focusId = ""
    else:
        focusId = "focusedInput"

    if required:
        required = """required"""
    else:
        required = ""

    if disabled:
        disabled = """disabled"""
        disabledId = "disabledId"
    else:
        disabled = ""
        disabledId = ""

    if not htmlId:
        htmlId = ""
        name = "textarea"
    else:
        name = htmlId

    textarea = """<textarea rows="%s" class="%s" id="%s%s%s" value="%s" %s %s placeholder="%s" name="%s"></textarea>%s%s""" % (
        rows, span, htmlId, focusId, disabledId, focusedInputText, required, disabled, placeholder, name, inlineHelpText, blockHelpText)

    return textarea


## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def checkbox(
        optionText="",
        inline=False,
        optionNumber=1,
        htmlId=False,
        inlineHelpText=False,
        blockHelpText=False,
        disabled=False):
    """Generate a checkbox - TBS style

    **Key Arguments:**
        - ``optionText`` -- the text associated with this checkbox
        - ``inline`` -- display the checkboxes inline?
        - ``optionNumber`` -- option number of inline
        - ``htmlId`` -- htmlId
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line
        - ``disabled`` -- add the disabled attribute on an input to prevent user input

    **Return:**
        - ``checkbox`` -- the checkbox
    """
    if inline is True:
        inline = "inline"
        optionNumber = "option%s" % (optionNumber,)
    else:
        inline = ""
        optionNumber = ""

    if inlineHelpText:
        inlineHelpText = """<span class="help-inline">%s</span>""" % (inlineHelpText,)
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%s</span>""" % (blockHelpText,)
    else:
        blockHelpText = ""

    if disabled:
        disabled = """disabled"""
        disabledId = "disabledId"
    else:
        disabled = ""
        disabledId = ""

    if not htmlId:
        htmlId = ""

    checkbox = """
        <label class="checkbox %s">
          <input type="checkbox" value="%s" id="%s %s" %s>
          %s
        </label>%s%s""" % (inline, optionNumber, htmlId, disabledId, disabled, optionText, inlineHelpText, blockHelpText)

    return checkbox


## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def select(
        optionList=[],
        multiple=False,
        span=2,
        htmlId=False,
        inlineHelpText=False,
        blockHelpText=False,
        required=False,
        disabled=False):
    """Generate a select - TBS style

    **Key Arguments:**
        - ``optionList`` -- the list of options
        - ``multiple`` -- display all the options at once?
        - ``span`` -- column span
        - ``htmlId`` -- the html id of the element
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line
        - ``required`` -- required attribute if the field is not optional
        - ``disabled`` -- add the disabled attribute on an input to prevent user input

    **Return:**
        - ``select`` -- the select
    """
    if not htmlId:
        htmlId = ""

    if multiple is True:
        multiple = """multiple="multiple" """
    else:
        multiple = ""

    if span:
        span = "span%s" % (span,)
    else:
        span = ""

    if inlineHelpText:
        inlineHelpText = """<span class="help-inline">%s</span>""" % (inlineHelpText,)
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%s</span>""" % (blockHelpText,)
    else:
        blockHelpText = ""

    options = ""
    for option in optionList:
        options += """<option value="%(option)s">%(option)s</option>""" % locals()

    if required:
        required = """required"""
    else:
        required = ""

    if disabled:
        disabled = """disabled"""
        disabledId = "disabledId"
    else:
        disabled = ""
        disabledId = ""

    select = """
        <select %s name="%s" class="%s" id="%s%s" %s %s>
            %s
        </select>%s%s""" % (multiple, htmlId, span, disabledId, htmlId, required, disabled, options, inlineHelpText, blockHelpText)

    return select


## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def radio(
        optionText="",
        optionNumber=1,
        htmlId=False,
        inlineHelpText=False,
        blockHelpText=False,
        disabled=False,
        checked=False):
    """Generate a radio - TBS style

    **Key Arguments:**
        - ``optionText`` -- the text associated with this checkbox
        - ``optionNumber`` -- the order in the option list
        - ``htmlId`` -- the html id of the element
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line
        - ``disabled`` -- add the disabled attribute on an input to prevent user input
        - ``checked`` -- is the radio button checked by default

    **Return:**
        - ``radio`` -- the radio
    """
    if inlineHelpText:
        inlineHelpText = """<span class="help-inline">%s</span>""" % (inlineHelpText,)
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%s</span>""" % (blockHelpText,)
    else:
        blockHelpText = ""

    if disabled:
        disabled = """disabled"""
        disabledId = "disabledId"
    else:
        disabled = ""
        disabledId = ""

    if checked is False:
        checked = ""
    else:
        checked = "checked"

    if not htmlId:
        htmlId = ""

    radio = """
        <label class="radio">
          <input type="radio" name="%(htmlId)s" id="%(htmlId)s %(disabledId)s %(htmlId)s" value="%(optionText)s" %(checked)s %(disabled)s>
            %(optionText)s
        </label>%(inlineHelpText)s%(inlineHelpText)s""" % locals()

    return radio


## LAST MODIFIED : April 23, 2013
## CREATED : April 23, 2013
## AUTHOR : DRYX
def controlRow(inputList=[]):
    """generate a form row

    **Key Arguments:**
        - ``inputList`` -- list of inputs for the control row

    **Return:**
        - ``controlRow`` -- the controlRow
    """
    if len(inputList) > 1:
        row = "controls-row"
    else:
        row = ""

    content = ""
    for iinput in inputList:
        content += iinput

    controlRow = """
        <div class="controls %s">
            %s
        </div>""" % (row, content,)

    return controlRow


## LAST MODIFIED : April 24, 2013
## CREATED : April 24, 2013
## AUTHOR : DRYX
def uneditableInput(
        placeholder="",
        span=2,
        inlineHelpText=False,
        blockHelpText=False):
    """Generate a uneditableInput - TBS style

    **Key Arguments:**
        - ``placeholder`` -- the placeholder text
        - ``span`` -- column span
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line

    **Return:**
        - ``uneditableInput`` -- an uneditable input - the user can see but not interact
    """
    if span:
        span = "span%s" % (span,)
    else:
        span = ""

    if inlineHelpText:
        inlineHelpText = """<span class="help-inline">%s</span>""" % (inlineHelpText,)
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%s</span>""" % (blockHelpText,)
    else:
        blockHelpText = ""

    uneditableInput = """
        <span class="%s uneditable-input">
            %s
        </span>%s%s""" % (span, placeholder, inlineHelpText, blockHelpText)

    return uneditableInput


## LAST MODIFIED : April 24, 2013
## CREATED : April 24, 2013
## AUTHOR : DRYX
def formActions(
        primaryButton="",
        button2=False,
        button3=False,
        button4=False,
        button5=False,
        inlineHelpText=False,
        blockHelpText=False):
    """Generate a formActions - TBS style

    **Key Arguments:**
        - ``primaryButton`` -- the primary button
        - ``button2`` -- another button
        - ``button3`` -- another button
        - ``button4`` -- another button
        - ``button5`` -- another button
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line

    **Return:**
        - ``formActions`` -- the formActions
    """
    falseList = [primaryButton, button2, button3,
                 button4, button5, inlineHelpText]

    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""

    [primaryButton, button2, button3, button4,
        button5, inlineHelpText] = falseList

    if inlineHelpText:
        inlineHelpText = """<span class="help-inline">%s</span>""" % (inlineHelpText,)
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%s</span>""" % (blockHelpText,)
    else:
        blockHelpText = ""

    formActions = """
        <div class="form-actions">
          %s
          %s
          %s
          %s
          %s
        </div>%s%s""" % (primaryButton, button2, button3, button4, button5, inlineHelpText, blockHelpText)

    return formActions


## LAST MODIFIED : October 9, 2013
## CREATED : October 9, 2013
## AUTHOR : DRYX
def modal(
        modalHeaderContent="",
        modalBodyContent="",
        modalFooterContent="",
        htmlId=False,
        centerContent=False
):
    """generate a modal to by generated with a js event

    **Key Arguments:**
      - ``modalHeaderContent`` -- the heading for the modal
      - ``modalBodyContent`` -- the content (form or text)
      - ``modalFooterContent`` -- the foot (usually buttons)
      - ``htmlId`` -- id for button to hook onto with href

    **Return:**
        - ``modal`` -- the modal

    **Todo**
        - @review: when complete, clean modal function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    if htmlId is False:
        htmlId = ""
    else:
        htmlId = """id="%s" """ % (htmlId,)

    if centerContent is False:
        centerContent = ""
    else:
        centerContent = "center-content"

    ## VARIABLES ##
    modal = """<div class="modal hide fade" %s>
                  <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                    <h3>%s</h3>
                  </div>
                  <div class="modal-body %s">
                    %s
                  </div>
                  <div class="modal-footer">
                    %s
                  </div>
                </div>""" % (htmlId, modalHeaderContent, centerContent, modalBodyContent, modalFooterContent)

    return modal

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
