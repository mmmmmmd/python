dict={"name":"tim","age":20}

print dict

dict["name"]

print "name" in dict
print "sex" in dict

dict["sex"]="man"
print dict

print dict.get("kkk","false")

dict.pop("sex")
print dict

print len(dict)
