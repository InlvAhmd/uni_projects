import operator as op

"""
This file is just used for mapping the units to
the needed operation
"""


operations = {
            "kWh,Wh".lower()  : [op.mul,1000],
            "kWh,KJ".lower()  : [op.mul,3600],
            "kWh,J".lower()   : [op.mul,3600000],
            "Wh,kWh".lower    : [op.truediv,1000],
            "Wh,KJ".lower()   : [op.mul,3.6],
            "Wh,J".lower()    : [op.mul,3600],
            "KJ,kWh".lower()  : [op.truediv,3600],
            "KJ,Wh".lower()   : [op.truediv,3.6],
            "KJ,J".lower()    : [op.mul,1000],
            "J,kWh".lower()   : [op.truediv,3600000],
            "J,Wh".lower()    : [op.truediv, 3600],
            "J,KJ".lower()    : [op.truediv, 1000]
            }




def get_operation(currentUnit,newUnit):
    return operations["%s,%s" % (currentUnit,newUnit)]

