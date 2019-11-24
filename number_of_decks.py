# -*- coding: utf-8 -*-

"""
NUMBER OF DECKS

Adds a menu item to the Tools menu on the Decks screen, so that one can easily determine one’s total number of decks.
"""

from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *

def deckCountFunction():
    deckCount = len(mw.col.decks.allNames())
    showInfo("<br><b>You have %d decks.</b>" % deckCount)

action = QAction("Number of Decks", mw)
action.triggered.connect(deckCountFunction)
mw.form.menuTools.addAction(action)
