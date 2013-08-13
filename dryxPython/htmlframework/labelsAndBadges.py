#!/usr/bin/python
# -*- coding: utf-8 -*-

""" _dryxLabelsAndBadges
===============================
:Summary:
    Partial for dryxTwitterBootstrap

:Author:
    David Young

:Date Created:
    20130508

:dryx syntax:
    - ``xxx`` = come back here and do some more work
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this code please email me: d.r.young@qub.ac.uk """
###################################################################
# CLASSES                                                         #
###################################################################
###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
## LAST MODIFIED : 20130508
## CREATED : 20130508
## AUTHOR : DRYX

def label(text='', level='default'):
    """ Generate a label - TBS style

    **Key Arguments:**
        - ``text`` -- the text content
        - ``level`` -- the level colour of the label [ "default" | "success" | "warning" | "important" | "info" | "inverse" ]

    **Return:**
        - ``label`` -- the label """

    if level == 'default':
        level = ''
    else:
        level = 'label-%s' % (level, )
    label = """
        <span class="label %s" id="  ">
            %s
        </span>""" % (level, text)
    return label


def badge(text='', level='default'):
    """ Generate a badge - TBS style

    **Key Arguments:**
        - ``text`` -- the text content
        - ``level`` -- the level colour of the badge [ "default" | "success" | "warning" | "important" | "info" | "inverse" ]

    **Return:**
        - ``badge`` -- the badge """

    if level == 'default':
        level = ''
    else:
        level = 'badge-%s' % (level, )
    badge = """
        <span class="badge %s" id="  ">
            %s
        </span>""" % (level, text)
    return badge


## LAST MODIFIED : 20130508
## CREATED : 20130508
## AUTHOR : DRYX

def alert(alertText='',
    alertHeading="",
    extraPadding=False,
    alertLevel="warning"):
    """ Generate a alert - TBS style

    **Key Arguments:**
        - ``alertText`` -- the text to be displayed in the alert
        - ``extraPadding`` -- for longer messages, increase the padding on the top and bottom of the alert wrapper
        - ``alertLevel`` -- the level of the alert [ "warning" | "error" | "success" | "info" ]

    **Return:**
        - ``alert`` -- the alert """

    falseList = [extraPadding,]
    for i in range(len(falseList)):
            if not falseList[i]:
                falseList[i] = ""
    [extraPadding,]  = falseList

    if alertLevel == "warning":
        alertLevel = ""
    else:
        alertHeading = "alert-%s" % (alertLevel,)

    if extraPadding:
        extraPadding = "alert-block"
        alertHeading = "<h4>%s</h4>" % (alertHeading,)
    else:
        alertHeading = "<strong>%s</strong>" % (alertHeading,)


    alert = \
        """
        <div class="alert %s %s">
          <button type="button" class="close" data-dismiss="alert">&times;</button>
          %s %s
        </div>""" \
        % (extraPadding, alertLevel, alertHeading, alertText, )
    return alert


## LAST MODIFIED : 20130508
## CREATED : 20130508
## AUTHOR : DRYX
def progressBar(
        barStyle="plain",
        precentageWidth="10",
        barLevel="info"):
    """Generate a progress bar - TBS style

    **Key Arguments:**
        - ``barStyle`` -- style of the progress bar [ "plain" | "stripped" | "stripped-active" ]
        - ``precentageWidth`` -- the current progress of the bar
        - ``barLevel`` -- the level color of the bar [ "info" | "warning" | "success" | "error" ]

    **Return:**
        - ``progressBar`` -- the progressBar
    """
    barLevel = "progress-%s" % (barLevel,)

    if barStyle == "stripped":
        barStyle == "progess-stripped"
    elif barStyle == "stripped-active":
        barStyle == "progess-stripped active"
    else:
        barStyle = ""

    progressBar = """
        <div class="progress %s %s">
          <div class="bar" style="width: %s%%;"></div>
        </div>""" % (barLevel, barStyle, precentageWidth,)

    return progressBar


## LAST MODIFIED : 20130508
## CREATED : 20130508
## AUTHOR : DRYX
def stackedProgressBar(
        barStyle="plain",
        infoWidth="10",
        successWidth="10",
        warningWidth="10",
        errorWidth="10"
        ):
    """Generate a progress bar - TBS style

    **Key Arguments:**
        - ``barStyle`` -- style of the progress bar [ "plain" | "stripped" | "stripped-active" ]
        - ``infoWidth`` -- the precentage width of the info level bar
        - ``successWidth`` -- the precentage width of the success level bar
        - ``warningWidth`` -- the precentage width of the warning level bar
        - ``errorWidth`` -- the precentage width of the error level bar

    **Return:**
        - ``progressBar`` -- the progressBar
    """
    barLevel = "progress-%s" % (barLevel,)

    if barStyle == "stripped":
        barStyle == "progess-stripped"
    elif barStyle == "stripped-active":
        barStyle == "progess-stripped active"
    else:
        barStyle = ""

    stackedProgressBar = """
        <div class="progress %s %s">
          <div class="bar bar-info" style="width: %s%%;"></div>
          <div class="bar bar-success" style="width: %s%%;"></div>
          <div class="bar bar-warning" style="width: %s%%;"></div>
          <div class="bar bar-error" style="width: %s%%;"></div>
        </div>""" % (barLevel, barStyle, infoWidth, successWidth, warningWidth, errorWidth)

    return stackedProgressBar




###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################
###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
