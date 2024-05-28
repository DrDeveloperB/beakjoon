"""
1차원 배열,,,10871,,,X보다 작은 수

문제
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

출력
X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.
"""

# 정답 1
# n, x = input().split()
# print(*[i for i in input().split() if int(i) < int(x)])

# 정답 2
# print(*[i for x in input().split()[1:] for i in input().split() if int(i) < int(x)])

# 정답 3
# o = [*open(0)]
# print(*[i for i in o[1].split() if int(i) < int(o[0].split()[1])])

# 정답 4
n, x, *a = map(int, open(0).read().split())
for i in a:
    if i < x: print(i)

# 정답 5
"""
i < x != print(i)
이게 어떻게 실행되는거지???
"""
# n, x, *a = map(int, open(0).read().split())
# for i in a: i < x != print(i)

# 테스트
# o = open(0).read()
# print(o[0], o[1], o[2], o[3], o[4], o[5], o[6], sep='\n')
