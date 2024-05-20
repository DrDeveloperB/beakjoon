"""
조건문,,,2439,,,별 찍기 - 2

문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
"""

# 정답 1
# for i in range(n := int(input())):
#     print((" " * (n - (i + 1))) + ("*" * (i + 1)))

# 정답 2
# n = int(input())
# for i in range(n):
#     print(("*" * (i + 1)).rjust(n, " "))

# 정답 3
# for i in range(n := int(input())):
#     print(("*" * (-(~i))).rjust(n, " "))

# 정답 4
# n = i = int(input())
# while 0 < i:
#     i -= 1
#     print((" " * i) + ("*" * (n - i)))

# 정답 5
# s, n = '', int(input())
# exec("s += '*'; print(f'%{n}s' % s);" * n)

# 정답 6
"""
문자열 정렬
:< : 왼쪽 정렬
:> : 오른쪽 정렬
:^ : 가운데 정렬
ex)
'first {0:>10} | second {1:^12} | third {2:<14}'.format('right', 'center', 'left')
0:>10 : 0 번째 문자열 right 를 공백으로 채운 10 자의 문자열로 만들어서 오른쪽 정렬로 표현
1:^11 : 1 번째 문자열 center 를 공백으로 채운 12 자의 문자열로 만들어서 가운데 정렬로 표현
2:<14 : 2 번째 문자열 left 를 공백으로 채운 14 자의 문자열로 만들어서 왼쪽 정렬로 표현
"""
# i, n = 0, int(input())
# while n - i:
#     i += 1
#     print(f'{("*" * i):>{n}}')

# 정답 7
i, n = 1, int(input())
exec('print((" " * (n - i)) + ("*" * i)); i += 1;' * n)
