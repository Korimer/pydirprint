from enum import Enum
import builtins
class Behavior(Enum):
    KEYVAL = 1
    ITMCOL = 2
    ITER   = 3

def printstruct(data,base_whitespace):
    dattype: type = type(data)
    
    match dattype:
        case builtins.str: print(base_whitespace + data + ","); return
        case _ if hasattr(dattype,"keys") and hasattr(dattype,"values"): behav = Behavior.KEYVAL
        case _ if hasattr(dattype,"items"):                              behav = Behavior.ITMCOL
        case _ if hasattr(dattype,"__iter__"):                           behav = Behavior.ITER
        case _: data = str(data); print(base_whitespace + data + ","); return
    
    limits = {
        builtins.dict: ("{","}"),
        builtins.set: ("{","}"),
        builtins.list: ("[","]"),
        builtins.tuple: ("(",")"),
    }.get(dattype,("<",">"))
    
    cur_whitespace = base_whitespace + " "
    print(base_whitespace + limits[0])

    match behav:
        case Behavior.KEYVAL:
            for key,val in zip(data.keys(), data.values()):
                print(cur_whitespace + key + ":")
                printstruct(val,cur_whitespace + "  ")
        case Behavior.ITMCOL:
            for val in data.items():
                printstruct(val,cur_whitespace + "  ")
        case Behavior.ITER:
            for val in data:
                printstruct(val,cur_whitespace + "  ")

    print(base_whitespace + limits[1] + ",")


printstruct([{"a":1},[{"b":2,"C":[5,{"d":100},7]},{8,9}],0],"")

# Desired output
'''
[
    {
        "a":
            1
    }
    [
        {
            "b":
                2,
            "C":
                [
                    5,
                    {"d":100},
                    7
                ]
        },
        {
            8,
            9
        }
    ],
    0
]
'''