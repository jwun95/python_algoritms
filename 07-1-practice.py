def list_finder(a, num):
    n = len(a)
    k = []
    for i in range(0, n):
        if a[i] == num:
            k.append(i+1)    

    return k

data = [17,92,18,33,58,5,33,42]
print(list_finder(data,33))