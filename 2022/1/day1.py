#Day 1: Calorie Counting 

elves = [0]
with open("input", "r") as infile:
    i = 0
    for line in infile:
        if not line==("\n"):
            #print(str(i) + " " + line)
            elves[i] += int(line)
        else:
            elves.append(0)
            i = i+1

#Part 1
print(max(elves))

#Part 2
elves.sort() 
print(sum(elves[-3:])) 

#print(str(len(elves)))
