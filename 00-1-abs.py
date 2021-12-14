import math

def abs_sign(a):
    if a < 0:
        return -a
    else:
        return a

def abs_square(a):
    b = a * a
    return math.sqrt(b)

if __name__ == "__main__":
    a = input("숫자를 입력하시오. :")
    print(abs_sign(int(a)))
    print(abs_square(int(a)))
    