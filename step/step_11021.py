"""
조건문,,,11021,,,A+B - 7

문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
"""

# 정답 1
# t, *l = open(0)
# i = 1
# for s in l:
#     print(f"Case #{i}: " + str(sum(map(int, s.split()))))
#     i += 1

# 정답 2
# t, *l = open(0)
# for i in range(len(l)):
#     print(f"Case #{i + 1}: " + str(sum(map(int, l[i].split()))))

# 정답 3
# t, *l = open(0)
# for i in range(len(l)):
#     print(f"Case #{i + 1}: {sum(map(int, l[i].split()))}")

# 정답 4
# t, *l = open(0)
# for i in range(len(l)):
#     print(f"Case #{i + 1}: {eval(l[i].strip().replace(' ', '+'))}")

# 정답 5
"""
enumerate : 인덱스와 값을 조합한 튜플 객체가 들어있는 리스트 객체 반환
"""
# t, *l = open(0)
# for i, v in enumerate(l):
#     print(f"Case #{i + 1}: {sum(map(int, v.split()))}")

# 정답 6
# for i, v in enumerate([*open(0)][1:]): print(f"Case #{i + 1}: {sum(map(int, v.split()))}")

# 정답 7
# for i, v in enumerate([*open(0)][1:]): print(f"Case #{i + 1}: {eval(v.strip().replace(' ', '+'))}")

# 정답 8
"""
:= : 대입 연산자 
"""
# for s in [*open(i := 0)][1:]: i += 1; print(f'Case #{i}:', sum(b'%a' % s) % 34)

# 정답 9
"""
[정답 8] 에서 34 를 51로 변경
"""
# for s in [*open(i := 0)][1:]: i += 1; print(f'Case #{i}:', sum(b'%a' % s) % 51)

# 정답 10
"""
[정답 8] 에서 34 를 24로 변경
"""
for s in [*open(i := 0)][1:]: i += 1; print(f'Case #{i}:', sum(b'%a' % s) % 24)

# 정답 11
"""
[정답 10] 에서 [b'%a' % s] 를 [repr(s).encode('ascii')] 로 변경
"""
# for s in [*open(i := 0)][1:]: i += 1; print(f'Case #{i}:', sum(repr(s).encode('ascii')) % 24)

# 정답 12
# import sys
# n = int(sys.stdin.readline())
# for i in range(1, n + 1):
#     x, y = map(int, sys.stdin.readline().split())
#     print(f"Case #{i}: {x + y}")

# # 테스트
# t, *l = open(0)
# for s in l:
#     k = l.index(s) + 1
#     print(f"Case #{k}: " + str(sum(map(int, s.split()))))

