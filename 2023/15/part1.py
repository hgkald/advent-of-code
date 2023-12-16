def main():
    line = input().strip('\n').split(',')

    total = 0
    for x in line: 
        total += hash(x)
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
