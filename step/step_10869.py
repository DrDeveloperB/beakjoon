'''
입출력과 사칙연산,,,10869,,,사칙연산

문제
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

입력
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

출력
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

참고
나누기 연산자 / 는 몫을 실수로 표현, 소수점이 항상 붙음
정수를 출력하기위해 나눗셈 후 소수점 이하를 버리는 // 연산자 사용
'''
a, b = map(int, input().split())
print(
    a+b,
    a-b,
    a*b,
    a//b,
    a%b,
    sep="\n"
)
# 콤마 붙여도 됨 sep="\n",

# print(
#     """
# {a+b}
#     """
# )

# import pprint
# stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
# stuff.insert(0, stuff[:])
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(stuff)