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


    def changeUnit(self, newUnit):
        temp = Unit_calc.get_operation(self.unit,newUnit)
        self.unit = newUnit
        calc = temp[0]
        numberToUse = temp[1]
        for index,value in enumerate(self.data):
            self.data[index] = calc(value,numberToUse)
        

    def changeInterval(self, newInterval):
        newData = []
        if int(self.interval) < newInterval:
            datapoints = int(
                newInterval / int(self.interval)
            )

            for i in range(0,len(self.data),datapoints):
                if i+datapoints <= len(self.data):
                    newVal = sum(self.data[i:i+datapoints]) / datapoints
                    newData.append(newVal)

        else:
            datapoints = int(
                newInterval / int(self.interval)
            )

            for i in self.data:
                newData.extend([i]*datapoints)


        self.data = newData
        self.interval = newInterval

        return self.data
    
    
