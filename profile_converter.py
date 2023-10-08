import JsonFileReader as jfr
import sys
import getopt
import json


"""
This script is the the one being executed by the user and the main one
"""


def usage():
    print("""\n
    Test usage: profile_converter.py --filepath FH_Prj/example.json --output output.json --interval 30 --unit Wh \n
          
        -- filepath     -> specify filepath of input json file (no default value)
        -- output       -> specify output filename of output json file (default: output.json)
        -- interval     -> interval in minutes (default: whatever is in the input json file)
        -- unit         -> the unit (choose between kWh,Wh,KJ,J) (default: the one in the json file)
          
        --help          -> prints out usage function
          """)

def main(argv):

    filepath = ""
    output = ""
    unit = ""
    interval = 0

    try:
        optList, args = getopt.getopt(argv,"", ["filepath=","interval=","unit=","output=","help"])
    except getopt.GetoptError:
        print("Wrong execution, please use profile_converter.py --help")
        sys.exit()
    
    for opt, arg in optList:
        if opt == "--interval":
            interval = arg
        elif opt == "--filepath":
            filepath = arg
        elif opt == "--unit":
            unit = arg
        elif opt == "--output":
            output = arg
        elif opt == "--help":
            usage()
            sys.exit()
            
    if filepath == "":
        print("No filepath given")
        
    try:
        f = open(filepath)
    except FileNotFoundError:
        print("Please check the given path or use following link: \n")
        print("https://letmegooglethat.com/?q=How+to+put+in+the+correct+path")
        sys.exit()

    datas = jfr.JsonFileReader(f)
    f.close()

    if output == "":
        output = "output.json"
    if interval == 0:
        interval = datas.interval
    if unit == "":
        unit = datas.unit

    if not(compareUnits(datas.unit,unit)):
        datas.changeUnit(unit)

    if not(compareInterval(datas.interval,interval)):
        datas.changeInterval(int(interval))

    dict = {"name" : datas.name,
            "interval_in_minutes" : datas.interval,
            "unit" : datas.unit,
            "data" : datas.data}
    
    with open(output, "w") as outfile:

        json.dump(dict,outfile,indent=3)

    print("""
    DONE - check the output file %s 
          """ % output)
    
def compareUnits(currentU,newU):
    return currentU == newU

def compareInterval(currentI,newI):
    return currentI == newI

main(sys.argv[1:])