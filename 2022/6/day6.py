with open("input", "r") as infile: 
    code = infile.readline()
    for i in range(len(code)):
        seq1 = code[i-4:i]
        if len(set(seq1))==4: 
            print(i)
            break

    for i in range(len(code)):
        seq2 = code[i-14:i]
        if len(set(seq2))==14:
            print(i)
            break

            
