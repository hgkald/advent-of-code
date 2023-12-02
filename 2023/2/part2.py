from sys import stdin 

def main():
    powers = {}

    for line in stdin: 
        line = line.split(":")
        game_id = int(line[0].split()[1])
        games = line[1].strip().split(";")

        max_count = {"red": 0, "green": 0, "blue":0}
        for g in games: 
            colours = g.split(",")
            for c in colours:
                c = c.strip().split()
                colour = c[1]
                num = int(c[0])
                if num > max_count[colour]:
                    max_count[colour] = num
        
        powers[game_id] = max_count["red"]*max_count["green"]*max_count["blue"]

    total = 0
    for v in powers.values():
        total += v


    print(total)

if __name__=='__main__': 
    main()
