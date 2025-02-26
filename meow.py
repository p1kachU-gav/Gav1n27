with open("index.html", "r") as file:
    lines = file.readlines()

with open("output.html", "w") as file:
    for line in lines:
        file.write("<br>" + line)
