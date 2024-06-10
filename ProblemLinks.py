import json
import matplotlib.pyplot as plt
import numpy as np

NOOFPROBLEMS = 800

problemRatings = dict()

with open("problem-ratings") as file:
    pr = json.loads(file.read())
    for pi, r in pr.items():
        problemRatings[pi]=r

print(len(problemRatings))

ratingCounts = dict()
problemsByRating = dict()

with open("ProblemsFrequency") as file:
    problems = json.loads(file.read())

    pl = []
    for p,f in problems.items():
        pl.append({"pid":p, "frq":f})

    pl = sorted(pl, key=lambda d: d['frq'])
    pl.reverse()

    cnt = 0
    for i in range(NOOFPROBLEMS):
        pid = pl[i]["pid"]
        rating = problemRatings.get(pid)
        if rating is None:
            cnt += 1
            continue
        # ratingCounts[rating] = ratingCounts.get(rating, 0)+1
        if rating>1500 and rating<2500:
            upj = problemsByRating.get(rating, [])
            upj.append(pid)
            problemsByRating[rating] = upj
    print("No Rating Problems:", cnt)


f = open("problem-links", "w")
for k, v in problemsByRating.items():
    f.write(str(k)+"\n")
    for pid in v:
        dd = pid.split("-")
        link = "https://codeforces.com/problemset/problem/"+dd[0]+"/"+dd[1]
        f.write(link+"\n")
f.close()




# ratingCounts = dict(sorted(ratingCounts.items()))

# print(len(ratingCounts))
# for k, v in ratingCounts.items():
#     print(k, v)

# plt.plot(ratingCounts.keys(), ratingCounts.values())
# plt.show()
        