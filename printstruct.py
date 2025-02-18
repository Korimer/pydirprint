import builtins

def printstruct(data,base_whitespace):
    dattype: type = type(data)
    
    if not(hasattr(dattype,"__iter__")) or dattype == builtins.str: print(base_whitespace + str(data)); return # Early return... hrmrmrmr.....
    
    limits = {
        builtins.dict: ("{","}"),
        builtins.set: ("{","}"),
        builtins.list: ("[","]"),
        builtins.set: ("(",")"),
    }.get(dattype,("<",">"))
    
    cur_whitespace = base_whitespace + " "
    print(base_whitespace + limits[0])

    if hasattr(dattype,"keys") and hasattr(dattype,"values"):
        for key,val in zip(data.keys(), data.values()):
            print(cur_whitespace + key + ":")
            printstruct(val,cur_whitespace + "  ")
    elif hasattr(dattype,"items"):
        for val in data.items():
            printstruct(val,cur_whitespace + "  ")
    else:
        for val in data:
            printstruct(val,cur_whitespace + "  ")

    print(base_whitespace + limits[1])


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