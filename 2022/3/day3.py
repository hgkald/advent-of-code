def getPriority(char): 
    ordChar = ord(char)
    if ordChar >= ord("a") and ordChar <= ord("z"): 
        priority = ordChar-ord("a")+1
    elif ordChar >= ord("A") and ordChar <= ord("Z"): 
        priority = ordChar-ord("A")+27

    #print(charInBoth,priority)
    return priority 

#PART 1
sum = 0
lines = []
with open("input","r") as infile: 
    for line in infile:
        lines.append(line) 

        halfIndex = int(len(line)/2)
        a = set(line[:halfIndex].strip())
        b = set(line[halfIndex:].strip())
        charInBoth = a & b

        sum += getPriority(charInBoth.pop())
print(sum)

#PART 2
sum = 0
for i in range(len(lines)):
    if (i+1) % 3 == 0:
        a = set(lines[i-2].strip())
        b = set(lines[i-1].strip())
        c = set(lines[i].strip())
        charInAll = (a & b) & c

        sum += getPriority(charInAll.pop())
print(sum) 
