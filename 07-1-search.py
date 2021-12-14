def list_finder(a, num):
    count = 1
    for i in a:
        if i == num:
            return count

        count += 1
        if count == len(a):
            return -1

data = [17,92,18,33,58,5,33,42]
print(list_finder(data,22))