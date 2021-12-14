def find_max(a):
    new = 0
    locate = 0
    for i in range(0,len(a)):
        if new < a[i]:
            new = a[i]
            locate = i
        
    return new, locate

a = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(a))