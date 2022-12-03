shapes = {"X":1, "Y":2, "Z":3}
scores = {"X":[3,0,6],
          "Y":[6,3,0],
          "Z":[0,6,3]}
index = {"A":0, "B":1, "C":2}

myScore = 0 
with open("input", "r") as infile: 
    for line in infile: 
        [a,b] = line.strip().split(" ") 
        print(shapes[b], scores[b][index[a]])
        myScore += shapes[b] + scores[b][index[a]]

print(myScore)


shapes = {"A":1, "B":2, "C":3}
#          shape: lose, draw, win 
results = { "A": ["C","A","B"],
            "B": ["A","B","C"],
            "C": ["B","C","A"]}
index = {"X":0, "Y":1, "Z":2}
points = {"X":0, "Y":3, "Z":6}

myScore = 0 
with open("input", "r") as infile: 
    for line in infile: 
        [a,b] = line.strip().split(" ") 
        myShape = results[a][index[b]]
        #print(results[a])
        myScore += shapes[myShape] + points[b]

print(myScore)



