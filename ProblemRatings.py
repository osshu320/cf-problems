import requests
import json

# URL =  "https://codeforces.com/api/problemset.problems"
# res = requests.get(URL)
# data = res.json()

f = open("problems", "r")
res = f.read()
data = json.loads(res)

problems = data["result"]["problems"]

problemRatings = dict()
for problem in problems:
    contestId = problem.get("contestId")
    if contestId is None:
        continue
    index = problem.get("index")
    if index is None:
        continue
    rating = problem.get("rating")
    if rating is None:
        continue

    problemId = str(contestId)+"-"+index
    problemRatings[problemId] = rating

print(len(problemRatings))

f = open("problem-ratings", "w")
f.write(json.dumps(problemRatings))
f.close()   