"""
조건문,,,8393,,,합

문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

출력
1부터 n까지 합을 출력한다.
"""

# 정답 1
# print(sum(range(1, int(input()) + 1)))

# 정답 2
n = int(input())
print((n * (n + 1)) // 2)

# 정답 3
"""
~n = -(n + 1)
"""
# n = int(input())
# print(n * -(~n) // 2)
