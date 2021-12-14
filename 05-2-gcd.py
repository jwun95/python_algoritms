# 유클리드 알고리즘을 이용한 최대공약수 구하기 최소공배수 구하기
def gcd(a,b):
    if b == 0:
        return a

    return gcd(b, a % b)

def lcm(a,b):
    num_gcd = gcd(a,b)
    return int(a * b) / num_gcd    

first = int(input('첫번째 정수를 입력하세요: '))
second = int(input('두번째 정수를 입력하세요: '))
print('%d와 %d의 최대 공약수는 %d, 최소 공배수는 %d입니다.' %(first,second,gcd(first,second),int(lcm(first,second))))