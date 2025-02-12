import builtins

def printstruct(data,whitespace):
    thereskeys = False
    dattype: type = type(data)
    
    if not(hasattr(data,"__iter__")): print(whitespace + data); return # Early return... hrmrmrmr.....
    limits = {
        builtins.dict: ("{","}"),
        builtins.set: ("{","}"),
        builtins.list: ("{","}"),
        builtins.set: ("(",")"),
    }.get(dattype,("<",">"))
    
    print(whitespace + limits[0])
    
    # Recursive case here

    print(whitespace + limits[1])


printstruct([{"a":1},[{"b":2,"C":[5,{"d":100},7]},{8,9}],0],"")

print(hasattr(dict,"__iter__"))
print("did it")