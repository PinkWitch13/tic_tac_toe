def board():
    b = [["_|", "_|", "_"], 
         ["_|", "_|", "_"],
         [" |", " |", " "]]
    
    ub =[]

    for f in b:
        f = ''.join(f) + '\n'
        ub.append(f)

    b = "".join(ub)
    print(b)
