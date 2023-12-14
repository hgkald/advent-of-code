from sys import stdin

def main(): 
    totals = [] 
    for line in stdin: 
        vals = [int(x) for x in line.split()]
        totals.append(vals[-1]+next_summand(vals))
    print(sum(totals))

def next_summand(vals, indent=""): 
    if set(vals) == {0}: 
        return 0
    diffs = [vals[i]-vals[i-1] for i in range(1,len(vals),1)]

    return diffs[-1]+next_summand(diffs, indent+"  ")

if __name__=='__main__':
    main()
