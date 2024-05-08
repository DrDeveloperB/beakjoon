'''
입출력과 사칙연산,,,10430,,,나머지

문제
(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

출력
첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
'''

# 정답 1
# a, b, c = map(int, input().split())
# print(
#     (a+b)%c,
#     ((a%c)+(b%c))%c,
#     (a*b)%c,
#     ((a%c)*(b%c))%c,
#     sep='\n'
# )

# 정답 2
'''
본문의 입력 내용을
입력된 A, B, C 숫자가 모두 2 ~ 10000 사이라고 해석
'''
def change_int(v):
    return int(v) if v.isnumeric() and int(v) in range(2, 10001) else -1
a, b, c = map(change_int, input().split())
if a >= 0 and b >= 0 and c >= 0:
    print(
        (a+b)%c,
        ((a%c)+(b%c))%c,
        (a*b)%c,
        ((a%c)*(b%c))%c,
        sep='\n'
    )
else:
    print('숫자만 입력 가능합니다.')

'''
본문의 입력 내용을
2 ≤ A
0 ≤ B 
C ≤ 10000
와 같이 각각의 조건으로 해석
'''
# def change_int(v):
#     return int(v) if v.isnumeric() else -1
# a, b, c = map(change_int, input().split())
# if a >= 2 and b >= 0 and c <= 10000:
#     print(
#         (a+b)%c,
#         ((a%c)+(b%c))%c,
#         (a*b)%c,
#         ((a%c)*(b%c))%c,
#         sep='\n'
#     )
# else:
#     print('숫자만 입력 가능합니다.')

# 테스트
# a, b, c = map(int, input().split())
# print(
#     a,
#     b,
#     c,
#     sep='\n'
# )

# def change_int(v):
#     return int(v) if v.isnumeric() and int(v) in range(2, 10001) else -1
    # if v.isnumeric():
    #     return int(v)
    #     # if int(v) in range(2, 10001):
    #     #     return int(v)
    #     # else:
    #     #     return ''
    # else:
    #     return -1
# a, b, c = map(change_int, input().split())
# if a and b and c:
#     print(
#         (a+b)%c,
#         ((a%c)+(b%c))%c,
#         (a*b)%c,
#         ((a%c)*(b%c))%c,
#         sep='\n'
#     )
# else:
#     print('숫자만 입력 가능합니다.')
# print(
#     type(a),
#     type(b),
#     type(c),
#     sep='\n'
# )
# if a >= 2:
#     print(a)
# else:
#     print('숫자 아님')

# if a >= 2 and b >= 0 and c <= 10000:
#     print(
#         (a+b)%c,
#         ((a%c)+(b%c))%c,
#         (a*b)%c,
#         ((a%c)*(b%c))%c,
#         sep='\n'
#     )
# else:
#     print('숫자만 입력 가능합니다.')

# 0 으로 나누기 오류 발생
# print(1/0)