'''
조건문,,,2739,,,구구단

문제
N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

출력
출력형식과 같게 N*1부터 N*9까지 출력한다.
'''

# 정답 1
# n = int(input())
# for i in range(1, 10):
#     print(f'{n} * {i} = {n * i}')

# 정답 2
# n = int(input())
# print(
#     '\n'.join([f'{n} * {i} = {n * i}' for i in range(1, 10)])
# )

# 정답 3
'''
exec : 문자열로 된 코드를 실행
print : 함수안의 쉼표 구분자는 출력시 공백으로 대체됨
"print(a, '*', b//a, '=', b); b += a;" : 콘솔에서 print 코드 입력 후 enter -> b 변수값 수정 후 enter
"print(a, '*', b//a, '=', b); b += a;" * 9 : 문자열로 된 코드를 9회 실행
예시)
입력값 = 3

1차 수행
a = b = 3
b//a = 1
print(a, '*', b//a, '=', b); : print(3, '*', 1, '=', 3);
; 코드에의한 print 문 종료
b 변수에 새로운 값 대입
b += a; : 3 + 3 = 6
; 코드에의한 b 변수값 수정 종료

2차 수행
a = 3
b = 6   # 이전 코드에서 입력된 b 값
b//a = 2
print(a, '*', b//a, '=', b); : print(3, '*', 2, '=', 6);
; 코드에의한 print 문 종료
b 변수에 새로운 값 대입
b += a; : 6 + 3 = 9
; 코드에의한 b 변수값 수정 종료
'''
a = b = int(input()); exec("print(a, '*', b//a, '=', b); b += a;" * 9)

# 테스트
# n = int(input())
# # print(' = \n'.join(map(str, range(1, 10))))
# print(f'{n} * ' + f' = \n{n} * '.join(map(str, range(1, 10))) + ' = ')

# a=b=int(input());exec("print(a,'*',b//a,'=',b);b+=a;"*9)
