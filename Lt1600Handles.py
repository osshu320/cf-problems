# find users whos rating change to >2000 from <1600 in last three years (1623265016)

import requests

handles = set()
with open("Gt2000Handles") as file:
    for handle in file:
        handle = handle.rstrip()

        URL = "https://codeforces.com/api/user.rating?handle="+handle
        res = requests.get(URL).json()
        subs = res["result"]
        for sub in subs:
            oldRating = sub["oldRating"]
            updTime = sub["ratingUpdateTimeSeconds"]
            if updTime > 1623265016 and oldRating<1600:
                handles.add(handle)
        
        print("done handle", handle)

print(len(handles))

f = open("Gt2000Lt1600Handles", "w")
for handle in handles:
    f.write(handle+"\n")
f.close()