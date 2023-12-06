def main(): 
    times = [int(x) for x in input().split(":")[1].split()]
    dists = [int(x) for x in input().split(":")[1].split()]

    wins = []
    for i in range(len(times)):
        time = times[i]
        dist = dists[i]

        min_t = None
        for t in range(time): 
            t_dist = t*(time-t)
            if t_dist > dist: 
                min_t = t
                break

        max_t = None
        for t in range(time, min_t, -1): 
            t_dist = t*(time-t)
            if t_dist > dist: 
                max_t = t
                break

        wins.append(max_t-min_t+1)

    prod = wins[0]
    for w in wins[1:]: 
        prod = prod*w
    print(prod)

if __name__=='__main__':
    main()
