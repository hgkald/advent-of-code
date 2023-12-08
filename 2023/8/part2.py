from sys import stdin 

def main(): 
    directions = input()

    nodes = {}
    start_nodes = []
    for line in stdin:
        if line == '\n': continue

        nid, children = line.replace(' ', '').strip().split('=')
        lid, rid = children.strip('()').split(',')
       
        nodes[nid] = (lid, rid)

        if nid[-1]=='A':
            start_nodes.append(nid)

    steps, d = 0, 0
    curr_nodes = start_nodes
    while True:
        direction = 0 if directions[d]=='L' else 1
        done = True
        for j in range(len(curr_nodes)): 
            curr = curr_nodes[j]
            curr_nodes[j] = nodes[curr][direction]
            if curr_nodes[j][-1] != 'Z':
                done = False
        steps += 1

        if done: break

        if d == len(directions)-1:
            d = 0
        else: d += 1

    print(steps)

if __name__=='__main__':
    main()
