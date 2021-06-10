# 재귀 호출을 이용한 팩토리얼 구하기

def fact(n, total):
    f_total = total
    f_n = n
    f_total = f_n*(f_n-1)

    fact(f_n, f_total)

total = 0
n = 1 
fact(n, total)