def getPriority(char): 
    priority = ord(char)
    if priority > 90: 
        priority = priority-96
    else: #uppercase
        priority = priority-38

    #print(charInBoth,priority)
    return priority 

#PART 1
sum = 0
lines = []
with open("input","r") as infile: 
    for line in infile:
        lines.append(line) 

        halfIndex = int(len(line)/2)
        a = line[:halfIndex]
        b = line[halfIndex:]

        #print(a,b)
        charInBoth = None
        for char1 in a: 
            for char2 in b: 
                #print(char1,  char2)
                if char1 == char2: 
                    charInBoth = char1 
                    break
            if charInBoth is not None: 
                break 

        sum += getPriority(charInBoth)
print(sum)

#PART 2
sum = 0
for i in range(len(lines)):
    if (i+1) % 3 == 0:
        a = lines[i-2]
        b = lines[i-1]
        c = lines[i] 

        possibleChars = []
        for char1 in a: 
            for char2 in b: 
                 if char1 == char2: 
                    possibleChars.append(char1) 

        charInAll = None
        for char in possibleChars: 
            for char3 in c: 
                if char == char3: 
                    charInAll = char 
                    break
            if charInAll is not None: 
                break 
        
        sum += getPriority(charInAll)
print(sum) 
