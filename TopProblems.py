# find top 400 frequent problems

import json

with open("ProblemsFrequency") as file:
    problems = json.loads(file.read())

    pl = []
    for p,f in problems.items():
        pl.append({"pid":p, "frq":f})

    pl = sorted(pl, key=lambda d: d['frq'])
    pl.reverse()

    for i in range(800):
        print(pl[i])

    