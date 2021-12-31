
import requests
import json
json_data=open("./sag.json","r").read()

res=requests.post("https://reqres.in/api/users",json=json.loads(json_data))
print(res.json())
ss=res.json()

import jsonpath

print(jsonpath.jsonpath(ss,"name"))