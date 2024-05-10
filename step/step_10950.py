'''
조건문,,,10950,,,A+B - 3

문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.
'''

# 정답 1
# t, *lines = open(0)
# for line in lines:
#     a, b = line.split()
#     print(int(a) + int(b))



# 테스트
# 두 수가 모두 한자리 숫자일경우에만 바이너리 계산 가능 (0 < A, B < 10)
i = '1 4\n'
print(b'%a'%i, sum(b'%a'%i), sum(b'%a'%i) % 24)

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
    