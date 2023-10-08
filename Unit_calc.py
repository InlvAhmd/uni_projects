import operator as op

"""
This file is just used for mapping the units to
the needed operation
"""


operations = {
            "kWh,Wh"  : [op.mul,1000],
            "kWh,KJ"  : [op.mul,3600],
            "kWh,J"   : [op.mul,3600000],
            "Wh,kWh"  : [op.truediv,1000],
            "Wh,KJ"   : [op.mul,3.6],
            "Wh,J"    : [op.mul,3600],
            "KJ,kWh"  : [op.truediv,3600],
            "KJ,Wh"   : [op.truediv,3.6],
            "KJ,J"    : [op.mul,1000],
            "J,kWh"   : [op.truediv,3600000],
            "J,Wh"    : [op.truediv, 3600],
            "J,KJ"    : [op.truediv, 1000]
            }




def get_operation(currentUnit,newUnit):
    return operations["%s,%s" % (currentUnit,newUnit)]

