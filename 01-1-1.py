def calculate(n):
    sum = 0 
    for i in range(1, n+1):
        sum += i * i
    return sum 




if __name__ == "__main__":
    a = input("숫자를 입력하세요")
    print(calculate(int(a)))