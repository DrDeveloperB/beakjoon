"""
조건문,,,2438,,,별 찍기 - 1

문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
"""

# 정답 1
# for i in range(int(input())):
#     print("*" * (i + 1))

# 정답 2
# print("\n".join(["*" * (i + 1) for i in range(int(input()))]))

# 정답 3
for i in range(int(input())): print('*' * (-(~i)))
