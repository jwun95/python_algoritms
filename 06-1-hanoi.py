def hanoi(n, from_, to_ , assist_):
    if n == 1 :
        print(from_ ,"->", to_)
        return
    
    hanoi(n-1, from_, assist_, to_)
    print(from_,"->",assist_)
    hanoi(n-1, assist_, to_, from_)



hanoi(2, 1,3,2)