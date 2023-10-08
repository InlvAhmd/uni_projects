import json
import math
import Unit_calc

"""
This class is made to read and manipulate
the data of the json file
"""

class JsonFileReader():
    def __init__(self,jsonobj):
        self.entry =  json.load(jsonobj)
        self.name = self.entry["name"]
        self.interval = self.entry["interval_in_minutes"]
        self.unit = self.entry["unit"]
        self.data = self.entry["data"]


