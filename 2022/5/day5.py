import copy 

with open("input", "r") as infile: 
    stacks = None
    stacks2 = None 
    for line in infile: 
        if stacks is None: 
            numStacks = int(len(line)/4)
            stacks = {newList: [] for newList in range(1,numStacks+1)} 
        
        if line =="\n" or line[1] =="1" :
            continue 
        elif line.startswith("move"):
            if stacks2 is None: 
                stacks2 = copy.deepcopy(stacks)

            line = line.split(" ")
            qty = int(line[1])
            frm = int(line[3])
            to = int(line[5])

            #PART 1
            for i in range(qty): 
                crate = stacks[frm].pop(0)
                stacks[to].insert(0,crate)

            #PART 2
            for i in range(qty-1,-1,-1):
                crate = stacks2[frm].pop(i)
                stacks2[to].insert(0,crate)


        else:
            for i in range(1,len(line),4): 
                if line[i] != " ": 
                    print(i, line[i])
                    key = (i+3)/4
                    stacks[key].append(line[i])

    print("\n", stacks)
    for stack in stacks.values(): 
        if len(stack) > 0: 
            print(stack[0], end="")
       
    print("\n", stacks2)
    for stack in stacks2.values(): 
        if len(stack) > 0: 
            print(stack[0], end="")

