def list_finder(a, name, num):
    n = len(a)
    for i in range(0, n):
        if num == a[i]:
            return name[i]

data = [39,14,67,105]
stu_name = ["Justin", "John", "Mike", "Summer"]
print(list_finder(data,stu_name, 67))