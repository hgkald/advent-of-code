from sys import stdin 

def main(): 
    directions = input()

    nodes = {}
    for line in stdin:
        if line == '\n': continue

        nid, children = line.replace(' ', '').strip().split('=')
        lid, rid = children.strip('()').split(',')
       
        nodes[nid] = (lid, rid) 

    steps, d = 0, 0 
    curr = 'AAA'  
    while True:
        direction = 0 if directions[d]=='L' else 1
        curr = nodes[curr][direction]
        steps += 1
        
        if curr=='ZZZ': 
            break

        if d == len(directions)-1:
            d = 0
        else: d += 1

    print(steps)

if __name__=='__main__':
    main()
