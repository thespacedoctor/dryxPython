#!/usr/local/bin/python
# encoding: utf-8
"""
forms.py
=============================
:Summary:
    Forms for TBS htmlframework

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

# LAST MODIFIED : April 16, 2013
# CREATED : April 16, 2013
# AUTHOR : DRYX


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
        span = "span%(span)s" % locals()
    else:
        span = ""

    if not focusedInputText:
        focusedInputText = ""
        focusId = ""
    else:
        focusId = "focusedInput"

    if inlineHelpText:
        inlineHelpText = """<span class="help-inline">%(inlineHelpText)s</span>""" % locals(
        )
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%(blockHelpText)s</span>""" % locals(
        )
    else:
        blockHelpText = ""

    if not htmlId:
        htmlId = ""

    searchForm = """
    <form class="form-search">
    <div class="input-append">
      <input type="text" class="search-query %(span)s" id="%(htmlId)s"  id="%(focusId)s" value="%(focusedInputText)s">
      <button type="submit" class="btn">%(buttonText)s</button>
            %(inlineHelpText)s%(blockHelpText)s
    </div>
    </form>""" % locals()

    return searchForm

# LAST MODIFIED : April 16, 2013
# CREATED : April 16, 2013
# AUTHOR : DRYX


def form(
        content="",
        formType="inline",
        postToScript="",
        htmlId=False,
        htmlClass=False,
        navBarPull=False,
        postInBackground=False,
        redirectUrl=False,
        span=False,
        offset=False,
        openInNewTab=False):
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
        span = "span%(span)s" % locals()

    if offset is False:
        offset = ""
    else:
        offset = "offset%(offset)s" % locals()

    if not htmlClass:
        htmlClass = ""

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
        navBarPull = "pull-%(navBarPull)s" % locals()

    thisList = ["inline", "horizontal", "search"]
    if formType in thisList:
        formType = """form-%(formType)s""" % locals()

    htmlInput = ""
    if formType == "navbar-search":
        htmlInput = """%(htmlInput)s<input type="text" class="search-query" placeholder="search">""" % locals()

    if htmlId:
        htmlId = """id="%(htmlId)s" """ % locals()
    else:
        htmlId = ""

    if openInNewTab is not False:
        openInNewTab = """ target="_blank" """

    form = """<form class="%(formType)s %(navBarPull)s %(postInBackground)s %(span)s %(offset)s %(htmlClass)s" %(htmlId)s action="%(postToScript)s" method="post" %(openInNewTab)s>%(content)s%(htmlInput)s%(redirectUrl)s</form>""" % locals(
    )

    return form


# LAST MODIFIED : April 16, 2013
# CREATED : April 16, 2013
# AUTHOR : DRYX
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


# LAST MODIFIED : April 16, 2013
# CREATED : April 16, 2013
# AUTHOR : DRYX
def horizontalFormControlLabel(
        labelText="",
        forId=False,
        sideLabel=False,
        location="left"):
    """set a horizontal form label

    **Key Arguments:**
        - ``labelText`` -- the label text
        - ``forId`` -- what is the label for (id of the associated object)?

    **Return:**
        - ``horizontalFormRowLabel`` -- the horizontalFormRowLabel
    """
    if forId is False:
        forId = ""

    if sideLabel:
        sideLabel = "sideLabel"
    else:
        sideLabel = ""

    horizontalFormRowLabel = """<label class="control-label %(sideLabel)s %(location)s" for="%(forId)s">%(labelText)s</label>""" % locals(
    )

    return horizontalFormRowLabel


# LAST MODIFIED : April 16, 2013
# CREATED : April 16, 2013
# AUTHOR : DRYX
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
        rightText=False,
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
        hidden = u"""hidden"""
    else:
        hidden = u""

    falseList = [searchBar, span, prepend, prependContent, append,
                 appendContent, inputId, pull, htmlId, appendClass, prependClass]

    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = u""

    [searchBar, span, prepend, prependContent, append, appendContent,
        inputId, pull, htmlId, appendClass, prependClass] = falseList

    if pull:
        pull = u"pull-%(pull)s" % locals()

    if span:
        span = u"span%(span)s" % locals()

    if searchBar:
        searchClass = u"search-query"
    else:
        searchClass = u""

    if prepend:
        prependClass = u"input-prepend"
        prependContent = u"""<span class="add-on">%(prepend)s</span>""" % locals(
        )

    if append:
        appendClass = u"input-append"
        appendContent = u"""<span class="add-on">%(append)s</span>""" % locals()

    # if prepend:
    #     if append:
    #         inputId = "appendedPrependedInput "
    #     else:
    #         inputId = "prependedInput "
    # elif append:
    #     inputId = "appendedInput "

    if button1:
        appendClass = u"input-append"
        appendContent = button1
        # inputId = "appendedInputButton "

    if button2:
        appendClass = u"input-append"
        appendContent = u"""%(appendContent)s %(button2)s""" % locals()
        # inputId = "appendedInputButtons "

    if appendDropdown:
        appendClass = u"input-append"
        # inputId = "appendedDropdownButton "
        appendContent = u"""
        <div class="btn-group">
            %(appendDropdown)s
        </div>""" % locals()

    if prependDropdown:
        prependClass = u"input-prepend"
        # inputId = "prependedDropdownButton "
        prependContent = u"""
        <div class="btn-group">
            %(prependDropdown)s
        </div>""" % locals()

    step = u""
    if ttype == "float":
        step = u""" step="any" """
        ttype = u"number"

    if prependDropdown and appendDropdown:
        pass
        # inputId = "appendedPrependedDropdownButton "

    if inlineHelpText:
        inlineHelpText = u"""<span class="help-inline">%(inlineHelpText)s</span>""" % locals(
        )
    else:
        inlineHelpText = u""

    if blockHelpText:
        blockHelpText = u"""<span class="help-block">%(blockHelpText)s</span>""" % locals(
        )
    else:
        blockHelpText = u""

    if not focusedInputText:
        focusedInputText = u""
        focusId = u""
    else:
        focusedInputText = u"""value="%(focusedInputText)s" """ % locals()
        focusId = u"focusedInput "

    if required:
        required = u"""required"""
    else:
        required = u""

    if disabled:
        disabled = u"""disabled"""
        disabledId = u""
    else:
        disabled = u""
        disabledId = u""

    if defaultValue:
        if isinstance(defaultValue, str) or isinstance(defaultValue, unicode):
            defaultValue = defaultValue.replace('"', "\"")
            defaultValue = u'"%(defaultValue)s"' % locals()

        defaultValue = u"""value=%(defaultValue)s """ % locals()
    else:
        defaultValue = u""

    thisInput = u"""
    %(prependContent)s
    <input class="%(searchClass)s %(span)s" id="%(htmlId)s%(focusId)s%(disabledId)s" %(focusedInputText)s type="%(ttype)s" %(step)s placeholder="%(placeholder)s" %(required)s %(disabled)s name="%(htmlId)s" %(defaultValue)s>
    %(appendContent)s
    """ % locals()

    if rightText is not False:
        thisInput = u"""<label class="inline">%(thisInput)s%(rightText)s </label>""" % locals(
        )

    formInput = u"""
        <div class="%(prependClass)s %(appendClass)s %(hidden)s %(pull)s">
            
            %(thisInput)s 
            
        </div>%(inlineHelpText)s%(blockHelpText)s
        """ % locals()

    # formInput = """<input class="%s %s" id="%s%s%s%s" value="%s" type="%s" placeholder="%s" %s %s>""" % (span, searchClass, htmlId, inputId, focusId, disabledId, focusedInput, ttype, placeholder, required, disabled)

    return formInput


# LAST MODIFIED : April 16, 2013
# CREATED : April 16, 2013
# AUTHOR : DRYX
def textarea(
        rows="",
        span=2,
        placeholder="",
        htmlId=False,
        inlineHelpText=False,
        blockHelpText=False,
        focusedInputText=False,
        required=False,
        disabled=False,
        prepopulate=False):
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
        span = "span%(span)s" % locals()
    else:
        span = ""

    if inlineHelpText:
        inlineHelpText = """<span class="help-inline">%(inlineHelpText)s</span>""" % locals(
        )
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%(blockHelpText)s</span>""" % locals(
        )
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

    if prepopulate is False:
        prepopulate = ""

    textarea = """<textarea rows="%(rows)s" class="%(span)s" id="%(htmlId)s%(focusId)s%(disabledId)s" value="%(focusedInputText)s" %(required)s %(disabled)s placeholder="%(placeholder)s" name="%(name)s">%(prepopulate)s</textarea>%(inlineHelpText)s%(blockHelpText)s""" % locals(
    )

    return textarea


# LAST MODIFIED : April 16, 2013
# CREATED : April 16, 2013
# AUTHOR : DRYX
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
        optionNumber = "option%(optionNumber)s" % locals()
    else:
        inline = ""
        optionNumber = ""

    if inlineHelpText:
        inlineHelpText = """<span class="help-inline">%(inlineHelpText)s</span>""" % locals(
        )
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%(blockHelpText)s</span>""" % locals(
        )
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
        name = ""
    else:
        name = """name="%(htmlId)s" """ % locals()

    checkbox = """
        <label class="checkbox %(inline)s">
          <input type="checkbox" %(name)s value="%(optionNumber)s" id="%(htmlId)s %(disabledId)s" %(disabled)s>
          %(optionText)s
        </label>%(inlineHelpText)s%(blockHelpText)s""" % locals()

    return checkbox


# LAST MODIFIED : April 16, 2013
# CREATED : April 16, 2013
# AUTHOR : DRYX
def select(
        optionList=[],
        valueList=False,
        multiple=False,
        span=2,
        htmlId=False,
        htmlClass=False,
        inlineHelpText=False,
        blockHelpText=False,
        required=False,
        disabled=False,
        popover=False,
        extraAttributeTupleList=False):
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
        - ``popover`` -- add helper text to the select

    **Return:**
        - ``select`` -- the select
    """
    if not htmlId:
        htmlId = ""

    if not htmlClass:
        htmlClass = ""

    extraAttributes = ""
    if extraAttributeTupleList:
        for attributeTuple in extraAttributeTupleList:
            attr = attributeTuple[0]
            val = attributeTuple[1]
            if isinstance(val, str) or isinstance(val, unicode):
                val = '"%(val)s"' % locals()
            extraAttributes = """%(extraAttributes)s %(attr)s=%(val)s """ % locals(
            )

    if not valueList:
        valueList = optionList

    if multiple is True:
        multiple = """multiple="multiple" """
    else:
        multiple = ""

    if span:
        span = "span%(span)s" % locals()
    else:
        span = ""

    if popover is False:
        popover = ""

    if inlineHelpText:
        inlineHelpText = """<span class="help-inline">%(inlineHelpText)s</span>""" % locals(
        )
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%(blockHelpText)s</span>""" % locals(
        )
    else:
        blockHelpText = ""

    options = ""
    for o, v in zip(optionList, valueList):
        options = """%(options)s <option value="%(v)s">%(o)s</option>""" % locals()

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
        <select %(multiple)s name="%(htmlId)s" class="%(span)s %(htmlClass)s" %(popover)s id="%(disabledId)s%(htmlId)s" %(required)s %(disabled)s %(extraAttributes)s>
            %(options)s
        </select>%(inlineHelpText)s%(blockHelpText)s
        """ % locals()

    return select


# LAST MODIFIED : April 16, 2013
# CREATED : April 16, 2013
# AUTHOR : DRYX
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
        inlineHelpText = """<span class="help-inline">%(inlineHelpText)s</span>""" % locals(
        )
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%(blockHelpText)s</span>""" % locals(
        )
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


# LAST MODIFIED : April 23, 2013
# CREATED : April 23, 2013
# AUTHOR : DRYX
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
        content = """%(content)s %(iinput)s""" % locals()

    controlRow = """
        <div class="controls %(row)s">
            %(content)s
        </div>""" % locals()

    return controlRow


# LAST MODIFIED : April 24, 2013
# CREATED : April 24, 2013
# AUTHOR : DRYX
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
        span = "span%(span)s" % locals()
    else:
        span = ""

    if inlineHelpText:
        inlineHelpText = """<span class="help-inline">%(inlineHelpText)s</span>""" % locals(
        )
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%(blockHelpText)s</span>""" % locals(
        )
    else:
        blockHelpText = ""

    uneditableInput = """
        <span class="%(span)s uneditable-input">
            %(placeholder)s
        </span>%(inlineHelpText)s%(blockHelpText)s""" % locals()

    return uneditableInput


# LAST MODIFIED : April 24, 2013
# CREATED : April 24, 2013
# AUTHOR : DRYX
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
        inlineHelpText = """<span class="help-inline">%(inlineHelpText)s</span>""" % locals(
        )
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%(blockHelpText)s</span>""" % locals(
        )
    else:
        blockHelpText = ""

    formActions = """
        <div class="form-actions">
          %(primaryButton)s
          %(button2)s
          %(button3)s
          %(button4)s
          %(button5)s
        </div>%(inlineHelpText)s%(blockHelpText)s""" % locals()

    return formActions


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
