import requests
geturl="http://127.0.0.1:5000/users"

headers={
    "Accept":"application/json",
    "User-Agent":"Python-Requests-Client"

}
response=requests.get(geturl,headers=headers,timeout=10)

response = requests.get(geturl)
print("get status code",response.status_code)
print(response.json())

posturl="http://127.0.0.1:5000/users"

body1={
   "name":"Raja"
}

r1 = requests.post(posturl, json=body1)
print("post status code",r1.status_code)
print(r1.json())

puturl="http://127.0.0.1:5000/users/3"
body2={
   "name":"Ramu"
}
r2 = requests.put(puturl, json=body2)
print("put status code",r2.status_code)
print(r2.json())

patchurl="http://127.0.0.1:5000/users/3"
body3={
   "name":"Raja"
}
r3 = requests.patch(patchurl, json=body3)
print("patch status code",r3.status_code)
print(r3.json())
deleteurl="http://127.0.0.1:5000/users/3"
r4 = requests.delete(deleteurl)
print("delete status code",r4.status_code)

