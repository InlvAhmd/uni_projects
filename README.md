What does the script do? 

The script reads a given json file and changes the data inside if needed and then writes it back to another json file which name is given by the operator. 

how to execute the script: 

The script NEEDS following arguments: 

--filepath 

    - this argument tells the program which json file to read from (NO DEFAULT)

optional arguments:

--output 
    
    - this argument tells the program how the json file should be named f.e. --output test.json

--interval 

    - since the json file that we read has a specific interval for the data it is holding, the user can change that interval if he wishes. If no new interval is given by the user, we will just take the same interval as in the reading json file. 

--unit 

    - since the json file that we read has a specific unit for the data it is holding, the user can change that unit if he wishes. If no new unit is given by the user, we will just take the same unit as in the reading json file.


IMPORTANT 

Accepted units are: 

    - kWh
    - Wh
    - KJ
    - J

    - The given units are Case Insensitive, but please do keep in mind, that the way you hand them over, is the way they get written into the new json file. 
