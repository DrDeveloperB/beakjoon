"""
1차원 배열,,,2562,,,최댓값

문제
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

입력
첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

출력
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
"""

# 정답 1
# print(x := max(li := [int(i) for i in [*open(0)]]), li.index(x) + 1)

# 정답 2
# print(x := max(li := [*map(int, [*open(0)])]), li.index(x) + 1)

# 정답 3
# print(x := max(li := [*map(int, open(0))]), li.index(x) + 1)

# 정답 4
# print(*max(zip(map(int, open(0)), range(1, 10))))

# 정답 5
# print(*max((int(input()), i + 1) for i in range(9)))

# 테스트
"""
<_io.TextIOWrapper name=0 mode='r' encoding='utf-8'>
"""
# print(open(0))
"""
5 4
1 2 3
3 4 4

"""
# print(open(0).read())
"""
5 4
 1 2 3
 3 4 4

"""
# print(*open(0))
"""
['5 4\n', '1 2 3\n', '3 4 4\n']
"""
# print([*open(0)])

# print(max(zip([1, 2, 3], [3, 2, 1])))
# print(max([1, 2, 3], [3, 2, 1]))
