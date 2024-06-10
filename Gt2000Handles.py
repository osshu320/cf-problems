# Get handles of all the active user with rating greater than 2000

import requests
import json

# gets all users who were participated in at least one contest during last month
# URL =  "https://codeforces.com/api/user.ratedList?activeOnly=true&includeRetired=false"
# res = requests.get(URL)
# data = res.json()

f = open("UsersList", "r")
res = f.read()
data = json.loads(res)

users = data["result"]

ratingGreaterThan2000Handles = []
for user in users:
    handle = user["handle"]
    mxRating = user["maxRating"]
    if mxRating<2000:
        continue
    ratingGreaterThan2000Handles.append(handle)

print(len(ratingGreaterThan2000Handles))

f = open("Gt2000Handles", "w")
for handle in ratingGreaterThan2000Handles:
    f.write(handle+"\n")
f.close()