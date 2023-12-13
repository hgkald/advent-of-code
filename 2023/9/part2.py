from sys import stdin

def main(): 
    totals = [] 
    for line in stdin: 
        vals = [int(x) for x in line.split()]
        
        totals.append(vals[0]-next_summand(vals))
    print(sum(totals))

def next_summand(vals, indent=""): 
    if set(vals) == {0}: 
        return 0

    diffs = []
    for i in range(1,len(vals),1):
        diffs.append(vals[i]-vals[i-1])
    diffs.insert(0, diffs[0]-next_summand(diffs, indent+"  "))

    #print(indent, diffs)
    return diffs[0] 


if __name__=='__main__':
    main()
