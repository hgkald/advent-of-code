from sys import stdin
import re

def main():
    digit_text = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = ['0','1','2','3','4','5','6','7','8','9'] + digit_text 
    dict_values = list(range(10))
    dict_values.extend(list(range(1,10)))
    digit_dict = dict(zip(digits, [str(x) for x in dict_values])) 

    total = 0
    for line in stdin:
        num = None
        starts_at = {}
        for digit in digits: 
            if digit in line: 
                digit_i = [m.start() for m in re.finditer(f'(?={digit})', line)]
                for i in digit_i: 
                    starts_at[i] = digit

        min_i = min(starts_at.keys())
        max_i = max(starts_at.keys())
        min_digit = digit_dict[starts_at[min_i]]
        max_digit = digit_dict[starts_at[max_i]]
        num = int(min_digit+max_digit)

        print(min_digit, max_digit, num)
        total += int(num)

    print(total)


if __name__=='__main__': 
    main() 
