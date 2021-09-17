# -*- coding: utf-8 -*-
# Copyright: (c) 2019 Andreas U. Schmidhauser <https://github.com/schmidhauser>
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

"""
NUMBER OF DECKS

Adds a menu item to the Tools menu on the Decks screen, so that one can easily determine one’s total number of decks.
"""

from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *

def deckCountFunction():
    deckCount = len(mw.col.decks.all_names_and_ids())
    showInfo("<br><b>You have %d decks.</b>" % deckCount)

action = QAction("Number of Decks", mw)
action.setShortcut("Alt+Ctrl+Shift+D")
action.triggered.connect(deckCountFunction)
mw.form.menuTools.addAction(action)
