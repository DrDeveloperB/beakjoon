"""
1차원 배열,,,10810,,,공 넣기

문제
도현이는 바구니를 총 N개 가지고 있고,
각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다.
또, 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다.
가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다.

도현이는 앞으로 M번 공을 넣으려고 한다.
도현이는 한 번 공을 넣을 때, 공을 넣을 바구니 범위를 정하고, 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다.
만약, 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다.
공을 넣을 바구니는 연속되어 있어야 한다.

공을 어떻게 넣을지가 주어졌을 때, M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.

둘째 줄부터 M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다.
각 방법은 세 정수 i j k로 이루어져 있으며, i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻이다.
예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻이다. (1 ≤ i ≤ j ≤ N, 1 ≤ k ≤ N)

도현이는 입력으로 주어진 순서대로 공을 넣는다.

출력
1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다. 공이 들어있지 않은 바구니는 0을 출력한다.

참고
문제가 거지같네.
입력
입력되는 첫째줄에 N 은 바구니번호, M 은 공을 넣기로 정한 계획의 횟수이다.
5 4 인 경우
1번 ~ 5번 바구니를 가지고 있고 4회에 걸쳐 공을 넣을 계획이다.
둘째줄부터 공을 넣을 계획을 작성한다.
1 2 3   # 1회 시도 : 1번 ~ 2번 바구니에 3번 공을 넣는다.
3 4 4   # 2회 시도 : 3번 ~ 4번 바구니에 4번 공을 넣는다.
1 4 1   # 3회 시도 : 1번 ~ 4번 바구니에 1번 공을 넣는다.
2 2 2   # 4회 시도 : 2번 ~ 2번 바구니에 2번 공을 넣는다.
바구니의 공 번호는 덮어쓰여진다.
출력은 1번 ~ N번 바구니까지 공 번호를 순서대로 표기하되 공이 없는 바구니는 0번으로 표기한다.
출력
1 2 1 1 0
3회째에서 1번 ~ 4번 바구니의 공을 모두 1번 공으로 교체함
4회째에서 2번 바구니의 공을 2번 공으로 교체함
5번 바구니는 공을 넣은 적이 없음
"""

# 정답 1
# o = [*open(0)]
# r = {}
# for s in o[1:]:
#     li = s.split()
#     for i in range(int(li[0]), int(li[1]) + 1):
#         r[i] = li[2]
# for i in range(1, int(o[0].split()[0]) + 1):
#     if i not in r:
#         r[i] = 0
# r = dict(sorted(r.items()))
# print(*r.values())

# 정답 2
# o = [*open(0)]
# r = {}
# for s in o[1:]:
#     li = s.split()
#     for i in range(1, int(o[0].split()[0]) + 1):
#         if i in range(int(li[0]), int(li[1]) + 1):
#             r[i] = li[2]
#         if i not in r:
#             r[i] = 0
# print(*r.values())

# 정답 3
# o = [*open(0)]
# r = {}
# for li in [s.split() for s in o[1:]]:
#     for i in range(1, int(o[0].split()[0]) + 1):
#         if i in range(int(li[0]), int(li[1]) + 1):
#             r[i] = li[2]
#         if i not in r:
#             r[i] = 0
# print(*r.values())

# 정답 4
"""
예시)
5 4
1 2 3
3 4 4
1 4 1
2 2 2

n = 5
_ = 4
l = 1, 2, 3, 3, 4, 4, 1, 4, 1, 2, 2, 2

r = [0] * n : n개만큼 list 확장 ([0, 0, 0, 0, 0, ...])

i, j, k, *l = l
i, j, k = 1, 2, 3

r[i - 1:j] = [k] * (j - i + 1)
r[0:2] = [3] * 2 ([3, 3])
리스트 0번째부터 1번째까지 3, 3 값으로 수정한다.

반복
l = 3, 4, 4, 1, 4, 1, 2, 2, 2
i, j, k = 3, 4, 4
l = 1, 4, 1, 2, 2, 2
i, j, k = 1, 4, 1
l = 2, 2, 2
i, j, k = 2, 2, 2
l = ''
"""
# n, _, *l = map(int, open(0).read().split())
# r = [0] * n
# while l:
#     i, j, k, *l = l
#     r[i - 1:j] = [k] * (j - i + 1)
# print(*r)

# 정답 5
"""
I = lambda: map(int, input().split())
매개변수가 없는 함수
    입력하는 행위가 없음
    input 객체를 받음
    입력값을 모두 int 처리
<function <lambda> at 0x000002589B41F0D0>

n, m = I()
입력 첫번째 줄

'i, j, k = I(); a[i - 1:j] = [k] * (j - i + 1);' * m
입력 두번째 줄부터 m 회 반복
"""
# I = lambda: map(int, input().split())
# n, m = I()
# a = [0] * n
# exec('i, j, k = I(); a[i - 1:j] = [k] * (j - i + 1);' * m)
# print(*a)

# 테스트
# 백준에서 틀렸다는데 어디가 틀린건지 모르겠다.
# 결과물은 잘 나오는데...
# n, m = map(int, input().split())
# r = {}
# for i, j, k in [s.split() for s in [*open(0)]]:
#     for i2 in range(1, n + 1):
#         if i2 in range(int(i), int(j) + 1):
#             r[i2] = int(k)
#         if i2 not in r:
#             r[i2] = 0
# print(*r.values())

# print([0] * 5)

"""
매개변수가 없는 함수
    입력하는 행위가 없음
    input 객체를 받음
    입력값을 모두 int 처리
<function <lambda> at 0x000002589B41F0D0>
https://dojang.io/mod/page/view.php?id=2359
"""
# I = lambda: map(int, input().split())
# print(I)

"""
한줄 입력받음
<map object at 0x000001ED2A0534C0>
"""
# I = map(int, input().split())
# print(I)

"""
입력하는 행위가 없음
input 객체를 받음
<built-in function input>
"""
# I = input
# print(I)
