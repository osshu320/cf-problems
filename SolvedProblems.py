# find problems solved by rating >2000 from <1600 users

import requests
import json

problemsFrequency = dict()

with open("Gt2000Lt1600Handles") as file:
    for handle in file:
        handle = handle.rstrip()

        ldict = set()
        try:
            URL = "https://codeforces.com/api/user.status?handle="+handle
            res = requests.get(URL).json()
            subs = res["result"]
            for sub in subs:
                problem = sub["problem"]
                contestId = problem.get("contestId")
                if contestId is None:
                    continue
                index = problem.get("index")
                if index is None:
                    continue
                problemId = str(contestId)+"-"+index

                author = sub["author"]
                ptype = author["participantType"]
                if ptype != "PRACTICE":
                    continue

                ldict.add(problemId)
        except:
            print("ERROR for handle", handle)

        for pid in ldict:
            problemsFrequency[pid] = problemsFrequency.get(pid, 0)+1
        
        print("done handle", handle)


print(len(problemsFrequency))

f = open("ProblemsFrequency", "w")
f.write(json.dumps(problemsFrequency)+"\n")
f.close()