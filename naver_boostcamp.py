def solution(arr):
    new_arr = []
    for i in arr:
        if i in new_arr:
            pass
        else:
            new_arr.append(i)

    count_arr = []

    if new_arr == arr:
        count_arr.append(-1)
        return count_arr

    new_arr.sort()

    for item in new_arr:
        count = 0
        for k in arr:
            if item == k:
                count += 1 

        count_arr.append(count)


    return count_arr


arr = [1,2,3]
print(solution(arr))