'''
문제
꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 이제 A + B + C를 계산할 차례이다!

입력
첫 번째 줄에 A, B, C (1 ≤ A, B, C ≤ 1012)이 공백을 사이에 두고 주어진다.

출력
A+B+C의 값을 출력한다.

참고
sum(map(int, list객체)) 를 사용하면 list 의 값들을 int 형으로 변환하여 sum 한다.
m 의 n 제곱근을 구하는 식은 m**n 이다.
map() 함수에 lambda 식을 사용하면 callback 함수에 유동 인자와 고정 인자값을 같이 전달할 수 있다.
isinstance() 함수로 전달받은 값이 전달받은 타입이 맞는지 비교해볼 수 있다. 
try 조건문의 예외 발생시 as (대입) 명령으로 변수에 오류 메세지를 담아 출력해볼 수 있다.
'''

# 정답 1
# print(sum(map(int, input().split())))

# 정답 2
# a, b, c = map(int, input().split())
# print(a+b+c)

# 정답 3
'''
입력값을 int 형으로 변환
최소값, 최대값 범위가 있는경우 범위 적용
'''
def change_int(v, s, e):
    if not v:
        return "숫자로 변환할 값이 주어지지않았습니다."
        # return False
    if not v.isnumeric():
        return "{} 이(가) 숫자가 아닙니다.".format(v)
    v = int(v)
    if s and not e:
        return "수의 범위중 최대값이 없습니다."
    if not s and e:
        return "수의 범위중 최소값이 없습니다."
    if s and e:
        if isinstance(s, int) == False:
            return "{} 이(가) 숫자가 아닙니다.".format(s)
        if isinstance(e, int) == False:
            return "{} 이(가) 숫자가 아닙니다.".format(e)
        if s > e:
            return "수의 범위중 최소값이 최대값보다 큽니다."
        if v not in range(s, e, 1):
            return "{} 이(가) 수의 범위에 포함되지 않습니다.".format(v)
    return v
try:
    a, b, c = map(lambda x : change_int(x, 1, (10**12)+1), input().split())
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        print(a+b+c)
    else:
        print(
            a, b, c, sep='\n'
        )
except ValueError as e:
    print(
        '숫자 3개를 한 줄에 공백으로 구분하여 입력해주세요.',
        e,
        sep='\n'
    )