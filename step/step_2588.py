'''
문제
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
   472  # (1)
  x385  # (2)
------
  2360  # (3)
 3776   # (4)
1416    # (5)
------
181720  # (6)
(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

출력
첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

참고
ValueError 가 발생한다면 입력단계 오류일 가능성이 크다
각각 다른 라인에 입력
'''

# 정답 1
# a = input()
# b = input()
# a = int(a)
# x, y, z = map(int, b)
# print(
#     a*z,
#     a*y,
#     a*x,
#     (a*z)+(a*y*10)+(a*x*100),
#     sep='\n'
# )

# 정답 2
def change_int(v):
    return int(v) if v.isnumeric() and int(v) in range(100, 1000) else -1
a, b = map(change_int, [input(), input()])
if a > 0 and b > 0:
    x, y, z = map(int, str(b))
    print(
        a*z,
        a*y,
        a*x,
        (a*z)+(a*y*10)+(a*x*100),
        sep='\n'
    )
else:
    print('100 ~ 999 사이의 숫자만 입력 가능합니다.')

# 테스트
# print(
#     123%120,
#     123%103,
#     123-23
# )

# b = 123
# x, y, z = map(int, str(b))
# print(
#     x,
#     y,
#     z,
#     sum(map(int, str(b))),
#     sep='\n'
# )

# b = 123
# b = str(b)
# print(
#     b[-1],
#     b[-2],
#     b[:1],
#     sep='\n'
# )

# a, b = map(int, input().split())
# x, y, z = map(int, str(b))
# b = str(b)
# x = int(b[:1])
# y = int(b[-2])
# z = int(b[-1])
# print(a*z)
# print(a*y)
# print(a*x)
# print((a*z)+(a*y*10)+(a*x*100))
# print(
#     a*z,
#     a*y,
#     a*x,
#     (a*z)+(a*y*10)+(a*x*100),
#     sep='\n'
# )

# a, b = map(int, input().split())
# try:
#     b = str(b)
#     x = int(b[:1])
#     y = int(b[-2])
#     z = int(b[-1])
#     print(
#         a*z,
#         a*y,
#         a*x,
#         (a*z)+(a*y*10)+(a*x*100),
#         sep='\n'
#     )
# except ValueError as e:
#     print(e)

# a, b = input().split()
# # a, b = map(int, input().split())
# if a.isnumeric() and int(a) in range(100, 1000) and b.isnumeric() and int(b) in range(100, 1000):
#     a = int(a)
#     # b = str(b)
#     x = int(b[:1])
#     y = int(b[-2])
#     z = int(b[-1])
#     print(a*z)
#     print(a*y)
#     print(a*x)
#     print((a*z)+(a*y*10)+(a*x*100))
