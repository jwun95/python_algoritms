def find_name(a):
    n = len(a)
    result = set()

    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
    
    return result


name = ["Tom", "Mike", "Jerry", "Tom"]
name2 = ["Tom", "Mike", "Jerry", "Tom", "Mike"]
print(find_name(name))
print(find_name(name2))