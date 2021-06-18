def find_min_value(k):
    min_value = 0
    for i in range(0,len(k)):
        if k[i] < k[min_value]:
            min_value = i

    return min_value

def sel_sort(a):
    
    e = []
    while a:
        min_value = find_min_value(a)
        value = a.pop(min_value)
        e.append(value)

    return e

a = [5,3,4,1,2]
print(sel_sort(a))