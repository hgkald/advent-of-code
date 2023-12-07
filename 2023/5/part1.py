from sys import stdin

def main():
    seeds = input()
    seeds = [int(x) for x in seeds.split(":")[1].split()]
    maps = []

    for line in stdin: 
        if 'map' in line: 
            maps.append(_read_map())

    location = {}
    
    #PART 1
    #for seed in seeds: 
    #    location[seed] = _find_location(seed, maps)
    #print(location)
    #print(min(location.values()))

    #PART 2
    min_location = float('inf')
    for i in range(0,len(seeds),2): 
        for seed in range(seeds[i],seeds[i]+seeds[i+1],1): 
            location = _find_location(seed, maps)
            if location < min_location: 
                min_location = location
    print(min_location)


def _get_value(x, hashmap): 
    for range_ in hashmap: 
        if range_[0] <= x <= range_[1]: 
            return x+hashmap[range_]
    return x 

def _find_location(seed, maps):
    x = _get_value(seed,maps[0])

    for m in maps[1:]:
        x = _get_value(x,m)
    return x

def _read_map():
    hashmap = {}
    for line in stdin: 
        if line=='\n': 
            break 
        dest, src, length = [int(x) for x in line.split()]
        hashmap[(src,src+length)] = dest-src
    return hashmap 

if __name__=='__main__':
    main()
