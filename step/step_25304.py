"""
조건문,,,25304,,,영수증

문제
준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 정말 멋졌다.
그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다!
준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.
영수증에 적힌
구매한 각 물건의 가격과 개수, 구매한 물건들의 총 금액을 보고,
구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

입력
첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다.
둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.
이후 N개의 줄에는
각 물건의 가격 a와
개수 b가 공백을 사이에 두고 주어진다.

출력
구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다.
일치하지 않는다면 No를 출력한다.

제한
1 ≤ X ≤ 1,000,000,000
1 ≤ N ≤ 100
1 ≤ a ≤ 1,000,000
1 ≤ b ≤ 10
"""

# 정답 1
# lines = [*open(0)]
# x = int(lines[0])
# n = int(lines[1])
# for line in lines[2:]:
#     a, b = map(int, line.split())
#     x -= a * b
# print('Yes' if x == 0 else 'No')

# 정답 2
# lines = [*open(0)]
# print('Yes' if int(lines[0]) - sum([sum(map(lambda numbers: int(numbers[0]) * int(numbers[1]), [line.split()])) for line in lines[2:]]) == 0 else 'No')

# 정답 3
"""
eval(expression) : 매개변수 expression (식) 을 문자열로 받아서 실행하는 함수 
"""
# x, n, *a = open(0)
# print(['No', 'Yes'][int(x) == sum(eval(i.replace(' ', '*')) for i in a)])

# 정답 4
"""
i.replace(*' *') : 문자열 i 값에서 공백을 * 로 변환 (*' *' = ' ', '*')
문자열 ' *' 앞에 붙인 * 연산자는 튜플 언패킹 연산자
문자열 ' *' 를 문자 하나씩 언패킹하여 튜플 자료형 ' ', '*' 를 반환
"""
# x, n, *a = open(0)
# print('YNeos'[int(x) != sum(eval(i.replace(*' *')) for i in a)::2])

# 정답 5
"""
한 줄 입력 후 enter 키를 눌러서 각 줄마다 끝에 개행문자가 붙어 있음
l[:-3] : 라인의 첫 문자부터 3글자 전까지
3글자 = 공백 + 수량 또는 공백 + 수량 + 개행문자
"""
s, _, *e = open(0)
print("YNeos"[int(s) != sum(int(l[:-3]) * int(l[-3:]) for l in e)::2])

# 테스트
# lines = [*open(0)]
# print(sum([map(int, line.split())]) for line in lines[2:])  # generator
# print('\n'.join([str(sum(map(int, line.split()))) for line in lines[2:]]))  # 모든 데이터 sum
# print([sum(map(int, line.split())) for line in lines[2:]])     # 라인별 합계
# print([line.split() for line in lines[2:]])   # 리스트 자료형 출력
# 라인별 곱하기 연산 후 합계
# map 자료형을 숫자형으로 변환하기 위해서 map 함수를 sum 함수로 감쌈
# print(sum([sum(map(lambda numbers: int(numbers[0]) * int(numbers[1]), [line.split()])) for line in lines[2:]]))

# print(*' *')
# print('1 4'.replace(*' *'))
# for i in open(0):
#     print(i.replace(*' *'))
#     print(i.replace(' ', '*'))

# print('1234567 8'[:-3], '1234567 8'[-3:], '1234567 8\n'[:-3], '1234567 8\n'[-3:], sep='\n')
# print('1234567 89'[:-3], '1234567 89'[-3:], '1234567 89\n'[:-3], '1234567 89\n'[-3:], sep='\n')
# s, _, *e = open(0)
# # print(sum(int(l[:-3]) * int(l[-3:]) for l in e))
# for l in e:
#     print(l[:-3], l[-3:])
