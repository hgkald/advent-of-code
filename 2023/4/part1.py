from sys import stdin 

def main():
    total = 0
    for line in stdin: 
        line = line.split(":")[1].split("|")
        nums = [int(x) for x in line[0].split()]
        my_nums = [int(x) for x in line[1].split()]

        winning_nums = 0
        for n in nums: 
            if n in my_nums: 
                winning_nums += 1
        if winning_nums: 
            score = 2**(winning_nums-1)
            #print(score)
            total += score 

    print(total)


if __name__=='__main__': 
    main()
