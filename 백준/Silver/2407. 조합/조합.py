# 조합
# nCm을 출력

n, m = map(int, input().split())

def fact(n):
    fac = 1
    for i in range(2, n+1):
        fac*=i
    return fac

print(fact(n) //(fact(m)*fact(n-m)) )