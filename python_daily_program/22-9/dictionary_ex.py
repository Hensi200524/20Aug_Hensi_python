
stdata={
    "id":101,
    "name":"Hensi",
    "city":"Morbi"
}

#print(stdata)
#print(stdata["id"])
#print(stdata.get("name"))
#print(stdata.keys())
#print(stdata.values())
#print(len(stdata))

"""if 'name' in stdata:
    print("Yes...")
else:
    print("Noo")"""


"""if 'Sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")
"""

"""for i in stdata:
    print(i)"""
    
"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""
    
# ------------------------------ #
"""print(stdata)

stdata["id"]=102 #update
stdata["sub"]="Python"
stdata.pop("name")
stdata.clear()
del stdata["city"]
del stdata
print(stdata)"""

# ------------------------ #
"""for i,j in stdata.items():
    #print(i,j)
    print(f"Key={i} : Value={j}")"""
    
# ------------------------- #
"""print(stdata)

newst=stdata.copy()
print(newst)"""
