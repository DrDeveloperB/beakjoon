"""
조건문,,,10951,,,A+B - 4

문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.
"""

# 정답 1
# print("\n".join([str(int(a) + int(b)) for a, _, b, _ in open(0)]))

# 정답 2
# for a, _, b, _ in open(0): print(int(a) + int(b))

# 정답 3
# import sys
# for a, _, b, _ in sys.stdin: print(int(a) + int(b))

# 정답 4
# for s in open(0): print(sum(b'%a' % s) - 408)

# 정답 5
# for s in open(0): print(sum(b'%a' % s) % 24)

# 정답 6
# for s in open(0): print(eval(f"{s[0]} + {s[2:]}"))
