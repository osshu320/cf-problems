of = open("markdown-links", "w")

with open("problem-links") as file:
    for line in file:
        line = line.rstrip()
        l = ""
        if line.startswith("https"):
            # l = "<p>"+line+"</p>"
            l="<a href="+line+">"+line+"</a></br>"
        else:
            l = "<h3>"+line+"</h3>"
        of.write(l+"\n")

of.close()