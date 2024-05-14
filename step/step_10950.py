"""
조건문,,,10950,,,A+B - 3

문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.
"""

# 정답 1
# t, *lines = open(0)
# for line in lines:
#     a, b = line.split()
#     print(int(a) + int(b))

# 정답 2
# line 값을 문자 하나씩 분할하여 계산하므로 한 자리 숫자만 가능
# for line in [*open(0)][1:]:
#     print(sum(map(int, [i for i in line if i.isnumeric()])))

# 정답 3
"""
open(0) = sys.stdin (0 은 표준 입력)
*open(0) = 가변 인자로 전달 받기 (positional arguments / keyword arguments 를 전달 받을때는 ** 2개 사용)
[*open(0)] = 입력 값을 라인별 리스트로 반환 ([line0, line1, ...])
[*open(0)][1:] = 0번째 라인 제외
"""
for line in [*open(0)][1:]:
    print(sum([i for i in map(int, line.split())]))

# 정답 4
# line 값을 문자 하나씩 분할하여 계산하므로 한 자리 숫자만 가능
"""
repr(i) = i 주어진 값을 표현하는 문자열로 반환
ex 1) 숫자 3 입력
print 3
ex 1) 문자 3 입력
print '3'
ex) 1 4 입력 후 enter
print '1 4\n'

encode('ascii') = 바이너리 데이터 반환 (아스키 코드로 인코딩)
ex)
repr(i) 값이 '1 4\n' 일때 b"'1 4\\n'" 값 반환

sum(repr(i).encode('ascii')) = 각 문자의 ASCII 코드값 합산 (문자열을 명시하는 작은따옴표 ' 도 코드값 합산)
ex) 
repr(i) 값이 '1 4\n' 일때 
' = 39
1 = 49
공백 = 32
4 = 52
\ = 92
n = 110
' = 39
39 + 49 + 32 + 52 + 92 + 110 + 39 = 413

sum(repr(i).encode('ascii')) % 51 = ASCII 코드값 합산 결과를 51 로 나눈 나머지
ex) 
repr(i) 값이 '1 4\n' 일때 
413 % 51 = 5
"""
# for i in [*open(0)][1:]:
#     print(sum(repr(i).encode('ascii')) % 51)

# 정답 5
"""
b'%a' = 바이너리 데이터 표현식
b'%a' % i = i 값을 바이너리 데이터로 변환 (repr(i).encode('ascii') 와 동일)
ex) 1 4 입력 후 enter
i 값이 '1 4\n' 일때 b"'1 4\\n'" 값 반환

sum(b'%a' % i) = 각 문자열의 ASCII 코드값 합산 (문자열을 명시하는 작은따옴표 ' 도 코드값 합산)
ex) 
i 값이 '1 4\n' 일때 
' = 39
1 = 49
공백 = 32
4 = 52
\ = 92
n = 110
' = 39
39 + 49 + 32 + 52 + 92 + 110 + 39 = 413
"""
# for i in [*open(0)][1:]:
#     print(sum(b'%a' % i) % 51)

# 정답 6
# [정답 5] 의 51 을 24로 수정
# for i in [*open(0)][1:]: print(sum(b'%a' % i) % 24)

# 테스트
# 두 수가 모두 한자리 숫자일경우에만 바이너리 계산 가능 (0 < A, B < 10)
"""
repr = 주어진 값을 표현하는 문자열로 반환
encode = 바이너리 데이터 반환
"""
# i = '1 4\n'
# print(
#     '%a' % i, b'%a' % i, sum(b'%a' % i), sum(b'%a' % i) % 24,
#     '%s' % i,
#     repr(i).encode('ascii', 'backslashreplace'),
#     i.encode('ascii', 'backslashreplace'),
#     repr(i).encode('ascii'),
#     b'%s' % repr(i).encode('ascii', 'backslashreplace'),
#     sum(b'%s' % repr(i).encode('ascii', 'backslashreplace')),
#     sum(b'%s' % repr(i).encode('ascii', 'backslashreplace')) % 24,
#     repr(i),
#     repr(i).encode('ascii'),
#     sum(repr(i).encode('ascii')),
#     sum(repr(i).encode('ascii')) % 24,
#     sep='\n'
# )

# for i in [*open(0)][1:]:
#     print(i, b'%a'%i)
#     print(sum(b'%a'%i)%24)

# print(*open(0))
# print([*open(0)])
# print([*open(0)][1:])

# t, *lines = open(0)
# # print(type(t), type(lines), len(lines), sep='\n')
# for line in lines:
#     a, b = line.split()
#     print(int(a) + int(b))

# t, *lines = open(0)
# t = int(t)
# i = 0
# exec("print(lines[i]); i += 1;" * t)
# exec("print(lines[t += (1 - t)]);" * t)
# s = -1
# exec("line = lines[s+=1]; a, b = line.split(); print(int(a) + int(b));" * t)

# for line in [*open(0)][1:]:
#     a, b = line.split()
#     print(int(a) + int(b))

# for line in [*open(0)][1:]:
#     print(sum(map(int, line.split())))

# for j in [i for line in [*open(0)][1:] for i in line]:
#     print(j)

# a = [i for line in [*open(0)][1:] for i in line if i.isnumeric()]
# print(a)

# print(sum(map(int, [i for line in [*open(0)][1:] for i in line if i.isnumeric()])))

# for line in [*open(0)][1:]:
#     print(sum(map(int, [i for i in line if i.isnumeric()])))

# for line in [*open(0)][1:]:
#     print([i for i in map(int, line.split())])
#     print(sum([i for i in map(int, line.split())]))
