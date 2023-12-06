def main(): 
    time = int("".join(input().split(":")[1].split()))
    dist = int("".join(input().split(":")[1].split()))

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

    print(max_t-min_t+1)

if __name__=='__main__':
    main()
