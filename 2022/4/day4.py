with open("input", "r") as infile: 
    count1 = 0
    count2 = 0

    for line in infile: 
        a, b = line.strip().split(",")
        a = a.split("-")
        b = b.split("-")

        for i in range(0,2): 
            a[i] = int(a[i])
            b[i] = int(b[i])

        #PART 1
        if ((a[0] >= b[0] and a[1] <= b[1]) or
            (b[0] >= a[0] and b[1] <= a[1])): 
               count1 += 1

        #PART 2
        a = set(range(a[0],a[1]+1))
        b = set(range(b[0],b[1]+1))
        if len(a & b) > 0: 
            count2 += 1
            
    print(count1)
    print(count2)
