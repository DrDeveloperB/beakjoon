'''
조건문,,,2480,,,주사위 세개

문제
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

입력
첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.

출력
첫째 줄에 게임의 상금을 출력 한다.
'''

# 정답 1
# a, b, c = map(int, input().split())
# if a == b == c:
#     print(10000 + (a * 1000))
# elif a == b or a == c:
#     print(1000 + (a * 100))
# elif b == c:
#     print(1000 + (b * 100))
# else:
#     print(max([a, b, c]) * 100)

# 정답 2
# a, b, c = map(int, input().split())
# if a == b == c:
#     print(10000 + (a * 1000))
# elif a == b or a == c or b == c:
#     print(1000 + ((b if b == c else a) * 100))
# else:
#     print(max([a, b, c]) * 100)

# 정답 3
# a, b, c = map(int, input().split())
# print(
#     [
#         [
#             max([a, b, c]) * 100,
#             1000 + ((b if b == c else a) * 100)
#         ][a == b or a == c or b == c],
#         10000 + (a * 1000)
#     ][a == b == c]
# )

# 정답 4
# a, b, c = map(int, input().split())
# print(
#     ([
#         [
#             max([a, b, c]),
#             [a, b][b == c]
#         ][a == b or a == c or b == c],
#         a
#     ][a == b == c] * [100, 1000][a == b == c])
#     + [[0, 1000][a == b or a == c or b == c], 10000][a == b == c]
# )

# 정답 5
'''
문제에 포함된 규칙
첫번째 숫자는 1 또는 가장 큰 수
0 의 개수는 2개 또는 3개

sorted : 기본값 순방향 정렬
a < b < c
c 가 제일 큰 수
숫자가 2개이상 같을 경우 10000 또는 1000 을 더해줌으로 앞에 1을 붙임
숫자가 2개이상 같을 경우는 a == b or a == c or b == c 이므로 문자 1에 a 또는 b 값을 붙임 (정답에서는 b 선택)
a < b < c 조건은 숫자가 모두 다를 경우에만 성립
숫자가 모두 다를 경우 제일 큰 숫자로 계산 (c)
a < c 조건이 성립할 경우 a == b == c 조건이 성립되지않으므로 0 의 개수는 2개
'''
*_, a, b, c = sorted(input())
print(
    ['1' + b, c][a < b < c] + '000'[(a < c):]
)

# 테스트
# a, b, c = map(int, input().split())
# print(
#     # [0, 1][1],
#     # max([a, b, c]) == min([a, b, c]),
#     # [0, 10000 + (a * 1000)][max([a, b, c]) == min([a, b, c])],
#     a == b == c,
#     # a != b != c,
#     # a ^ b ^ c,
#     a == b or a == c or b == c,
#     a < b < c, 
#     [
#         [
#             '모두 다르다.',
#             '2개만 같다.'
#         ][a == b or a == c or b == c],
#         '모두 같다.'
#     ][a == b == c],
#     [
#         [
#             max([a, b, c]) * 100,
#             1000 + ((b if b == c else a) * 100)
#         ][a == b or a == c or b == c],
#         10000 + (a * 1000)
#     ][a == b == c],
#     ([
#         [
#             max([a, b, c]),
#             [a, b][b == c]
#         ][a == b or a == c or b == c],
#         a
#     ][a == b == c] * [100, 1000][a == b == c])
#     + [[0, 1000][a == b or a == c or b == c], 10000][a == b == c],
#     sep='\n'
# )

# a, b, c = map(int, input().split())
# list = [
#     [
#         1000 + ((b if b == c else a) * 100),
#         max([a, b, c]) * 100
#     ],
#     10000 + (a * 1000)
# ]
# if a == b == c:
#     print(list[a == b == c])
# elif a == b or a == c or b == c:
#     # 1 2 1 일때 실패
#     print(list[a == b == c][a != b != c])
# else:
#     print(list[a == b == c][1])

# *_, a, b, c = sorted(input())
# print(
#     *_, a, b, c, '1' + b, a < b < c, '000'[(a < c):]
# )