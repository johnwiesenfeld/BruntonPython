import numpy as np
import datetime as dt

class Brunton:
    def __init__(self):
        number = 0
        oldtag = 0
        newtag = 0
        serialnumber = 0
        checkedOut = False
        needsRepair = False
        missing = False
        name = ''
        checkoutDate = dt.date
        checkinDate = dt.date
        
