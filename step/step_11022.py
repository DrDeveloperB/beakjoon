"""
조건문,,,11022,,,A+B - 8

문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
"""

# 정답 1
# for i, v in enumerate([*open(0)][1:]):
#     a, b = map(int, v.split())
#     print(f"Case #{i + 1}: {a} + {b} = {a + b}")

# 정답 2
# for i, v in enumerate([*open(0)][1:]):
#     print(f"Case #{i + 1}: {v.strip().replace(' ', ' + ')} = {sum(map(int, v.split()))}")

# 정답 3
# for i, v in enumerate([*open(0)][1:]):
#     print(f"Case #{i + 1}: {v.strip().replace(' ', ' + ')} = {eval(v.strip().replace(' ', ' + '))}")

# 정답 4
# for i, v in enumerate([*open(0)][1:]):
#     print(f"Case #{i + 1}: {v.split()[0]} + {v.split()[1]} = {sum(map(int, v.split()))}")

# 정답 5
# for i, v in enumerate([*open(0)][1:]):
#     print(f"Case #{i + 1}: {v[:1]} + {v[2:3]} = {sum(map(int, v.split()))}")

# 정답 6
# for i, v in enumerate([*open(0)][1:]):
#     print(f"Case #{i + 1}: {v[:1]} + {v[2:3]} = {int(v[:1]) + int(v[2:])}")

# 정답 7
# for i, v in enumerate([*open(0)][1:]): print(f"Case #{i + 1}: {v[:3].replace(' ', ' + ')} = {sum(b'%a' % v) % 24}")

# 정답 8
# for a, _, b, _ in [*open(i := 0)][1:]: i += 1; print(f"Case #{i}:", a, '+', b, '=', int(a) + int(b))

# 정답 9
# for a, _, b, _ in [*open(i := 0)][1:]: i += 1; print(f"Case #{i}: {a} + {b} = {int(a) + int(b)}")

# 테스트
# for i, *[v] in enumerate([*open(0)][1:]):
#     print(f"Case #{i + 1}: {v.strip().replace(' ', ' + ')} = {sum(map(int, v.split()))}")

# for i, *[v] in enumerate([*open(0)][1:]):
#     print(f"Case #{i + 1}: {v.strip().replace(' ', ' + ')} = {eval(v.strip().replace(' ', ' + '))}")

# a = '2'
# b = '4'
# # print(sum(a, b))    # error
# # print(sum(int(a), int(b)))    # error
# print(sum([int(a), int(b)]))
# print(sum(map(int, [a, b])))

# for a, _, b, _ in [*open(i := 0)][1:]:
#     i += 1
#     print(f"Case #{i}: {a} + {b} = {int(a) + int(b)}")
