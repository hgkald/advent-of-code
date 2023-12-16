def main():
    line = input().strip('\n').split(',')

    hashes = {}
    indeces = {}

    for x in line: 
        if '-' in x: 
            x = x.split('-')
            if x[0] not in indeces: 
                continue 

            id_ = x[0]
            h = hash(id_)
            i = indeces.pop(id_)

            hashes[h][i] = None 

        elif '=' in x: 
            x = x.split('=')
            id_ = x[0]
            h = hash(id_)

            i = indeces.get(id_,None)
            if i is None:
                if h not in hashes: 
                    hashes[h] = []
                hashes[h].append((id_,int(x[1])))
                indeces[id_] = len(hashes[h])-1
            else: 
                hashes[h][i] = (id_,int(x[1]))

    total = 0
    for k in hashes:
        curr = 1
        for v in hashes[k]: 
            if v is not None:
                total += (k+1)*curr*v[1]
                curr += 1

    #print(hashes)
    print(total)


def hash(x): 
    total = ord(x[0])
    for char in x[1:]: 
        total = f(total)+ord(char)
    return f(total)

def f(x):
    return x*17%256

if __name__=='__main__':
    main()
