#순열, 조합 사용시 사용되는 라이브러리
# 효율적인 루핑을 위한 이터레이터
import itertools    

while True:
    array = list(map(int, input().split()))
    
    k = array[0]
    s = array[1:]
    
    for i in itertools.combinations(s, 6): #iterable에서 원소 개수가 r개인 조합 뽑기
        print(*i)
        
    if k== 0:
        exit()
    print()    