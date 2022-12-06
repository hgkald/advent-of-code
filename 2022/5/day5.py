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
                for s in stacks.values(): 
                    s.reverse() 
                stacks2 = copy.deepcopy(stacks)

            line = line.split(" ")
            qty = int(line[1])
            frm = int(line[3])
            to = int(line[5])

            #PART 1
            for i in range(qty): 
                crate = stacks[frm].pop()
                stacks[to].append(crate)

            #PART 2
            for i in range(qty,0,-1):
                #print(i, stacks2[frm])
                crate = stacks2[frm].pop(i*-1)
                stacks2[to].append(crate)


        else:
            for i in range(1,len(line),4): 
                if line[i] != " ": 
                    key = (i+3)/4
                    stacks[key].append(line[i])

    print("\n", stacks)
    for stack in stacks.values(): 
        if len(stack) > 0: 
            print(stack[-1], end="")
       
    print("\n", stacks2)
    for stack in stacks2.values(): 
        if len(stack) > 0: 
            print(stack[-1], end="")

