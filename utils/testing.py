# import the main window object (mw) from aqt
from aqt import mw

# import all of the Qt GUI library
from aqt import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction() -> None:
    # get the number of cards in the current collection, which is stored in
    # the main window
    cardCount = mw.col.cardCount()
    # show a message box



