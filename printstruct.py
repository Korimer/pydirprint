def printstruct(data,whitespace):
    thereskeys = type(data) == dict
    for item in data:
        trueitem = data[item] if thereskeys else item
        whitespace_format = whitespace + ("{" + item + ": " if thereskeys else "  ")
        if hasattr(trueitem,"__iter__") and type(trueitem) != str:
            printstruct(trueitem,whitespace_format)
        else:
            print(whitespace_format + str(trueitem))

printstruct([{"a":1},[{"b":2,"C":[5,{"d":100},7]},{8,9}],0],"")

print(hasattr(dict,"__iter__"))
print("did it")