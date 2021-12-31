import requests
import pytest
import json
import jsonpath

import jsonpath

def test_get():
    res=  requests.get("http://localhost:3000/posts")
    assert res.status_code==200, "testpassed"
    print(res)


#
# def test_post():
#
#     filejs=open("")
#     requests.post()


res= requests.get("https://gorest.co.in/public-api/users")

json_sag=res.json()
print(json_sag)
#jsondata=json.loads(json_sag)
print(type(json_sag))
id =jsonpath.jsonpath(json_sag, "data[0].id")
name=jsonpath.jsonpath(json_sag, "data[*].name")
print(id[0])
for name in name:
    print(name)
