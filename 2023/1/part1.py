from sys import stdin

def main():
    digits = ['0','1','2','3','4','5','6','7','8','9']
    total = 0
    for line in stdin:
        num = None
        for char in line:
            if char in digits:
                if num is None: 
                    num = char
                else: 
                    num += char

        if len(num) == 1: 
            num += num 
        elif len(num) > 1: 
            num = num[0] + num[-1]

        total += int(num)

    print(total)

if __name__=='__main__': 
    main() 
