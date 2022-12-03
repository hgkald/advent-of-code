#Day 1: Calorie Counting 

elves = [0]
with open("input", "r") as infile:
    i = 0
    max = 0
    for line in infile:
        if not line==("\n"):
            #print(str(i) + " " + line)
            elves[i] += int(line)
        else:
            if elves[i] > max: 
                max = elves[i]
            elves.append(0)
            i = i+1

    #print(max)

    elves.sort() 
    sums = 0 
    for elf in elves[-3:]: 
        sums += elf 
    print(sums) 

    #print(elves[-3:])
    #print(str(len(elves)))
