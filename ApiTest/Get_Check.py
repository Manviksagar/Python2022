import requests

res=requests.get("https://reqres.in/api/users?page=2")

print(res.json())
payload={
    "name": "morpheus",
    "job": "leader"
}

print(res.json()["data"][0]["email"])
print(res.json()["data"][1]["id"])

resp=requests.post("https://reqres.in/api/users",data=payload)
print(resp.status_code)

assert  resp.status_code==201, "Status code is not match"
json_sag=res.json()
import jsonpath
name=jsonpath.jsonpath(json_sag, "data[*].email")

for name in name:
    print(name)