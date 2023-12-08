from sys import stdin 

class Node: 

    def __init__(self, nid, edges=None): 
        self.id = nid
        self.edges = edges
    
    def add_edge(self, node): 
        if self.edges is None: 
            self.edges = []
        self.edges.append(node)

    def __str__(self): 
        return f'{self.id}: {self.edges}'

    def __repr__(self):
        return f'Node({self.id}, {self.edges})'

def main(): 
    directions = input()

    nodes = {}
    for line in stdin:
        if line == '\n': continue

        nid, children = line.replace(' ', '').strip().split('=')
        lid, rid = children.strip('()').split(',')
       
        for i in [nid, lid, rid]: 
            if i not in nodes: 
                nodes[i] = Node(i)

        node = nodes[nid]
        node.add_edge(nodes[lid])
        node.add_edge(nodes[rid])

    steps = 0 
    curr = nodes['AAA']  
    i = 0 
    while True:
        direction = 0 if directions[i]=='L' else 1
        curr = curr.edges[direction]
        steps += 1
        
        if curr.id=='ZZZ': 
            break

        if i == len(directions)-1:
            i = 0
        else: 
            i += 1

    print(steps)

if __name__=='__main__':
    main()
