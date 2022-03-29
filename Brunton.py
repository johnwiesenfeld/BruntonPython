from cmd import PROMPT
import numpy as np
import datetime as dt

class Brunton:
    def __init__(self):
        self.number = 0
        self.oldtag = 0
        self.newtag = 0
        self.serialnumber = 0
        self.checkedOut = False
        self.needsRepair = False
        self.missing = False
        self.name = ""
        self.checkoutDate = dt.date
        self.checkinDate = dt.date

    def setnumber(self, num):
        self.number = num
    
    def setoldtag(self, num):
        self.oldtag = num
    
    def setnewtag(self, num):
        self.newtag = num

    def setserialnumber(self, num):
        self.serialnumber = num

    def checkout(self):
        self.checkedOut = True
    
    def checkin(self):
        self.checkedOut = False

    def markbroken(self):
        self.needsRepair = True

    def markfixed(self):
        self.needsRepair = False
    
    def marklost(self):
        self.missing = True
    
    def markfound(self):
        self.missing = False

    def setname(self, string):
        self.name = string


