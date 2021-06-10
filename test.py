num = int(input('7-9자리 정수를 입력하시오:'))
list = []

while True:
    num = str(num)
    new_list = []
    length = len(num)
    for item in range(length,0,-3):
        if item < 3:
            new_list.append(num[0:item])
            break
        new_list.append(num[item-3:item])
    break

list = new_list
list.reverse()

for i in range(len(list)):
    print(list[i], end='')

    if i+1 != len(list):
        print(',',end='') 

