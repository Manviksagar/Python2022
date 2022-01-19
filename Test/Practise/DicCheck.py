sc={
    "name":"Sagar",
    "id:":1,
    "marks":[2,4,5]
}

print(type(sc))
print(sc["marks"])

for x,y in sc.items():
    print(x,y)


sc["marks"].append(25)

print(sc["marks"])