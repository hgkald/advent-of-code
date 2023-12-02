from sys import stdin 

MAX_COUNT = {"red": 12, "green": 13, "blue":14}

def main():
    total = 0
    for line in stdin: 
        line = line.split(":")
        game_id = int(line[0].split()[1])
        games = line[1].strip().split(";")

        possible = True
        for g in games: 
            colours = g.split(",")
            for c in colours:
                c = c.strip().split()
                colour = c[1]
                num = int(c[0])
                if num > MAX_COUNT[colour]:
                    possible = False

        if possible: 
            total += game_id
            
    print(total)

if __name__=='__main__': 
    main()
