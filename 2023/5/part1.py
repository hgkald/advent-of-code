from sys import stdin

def main():
    seeds = input()
    seeds = [int(x) for x in seeds.split(":")[1].split()]
    maps = []

    for line in stdin: 
        if line == 'seed-to-soil map:\n':
            maps.append(_read_map())
        if line == 'soil-to-fertilizer map:\n': 
            maps.append(_read_map())
        if line == 'fertilizer-to-water map:\n':
            maps.append(_read_map())
        if line == 'water-to-light map:\n': 
            maps.append(_read_map())
        if line == 'light-to-temperature map:\n': 
            maps.append(_read_map())
        if line == 'temperature-to-humidity map:\n': 
            maps.append(_read_map())
        if line == 'humidity-to-location map:\n': 
            maps.append(_read_map())

    location = {}
    for seed in seeds: 
        location[seed] = _find_location(seed, maps)

    #print(location)
    print(min(location.values()))

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
