'''
입출력과 사칙연산,,,18108,,,1998년생인 내가 태국에서는 2541년생?!

문제
ICPC Bangkok Regional에 참가하기 위해 수완나품 국제공항에 막 도착한 팀 레드시프트 일행은 눈을 믿을 수 없었다. 공항의 대형 스크린에 올해가 2562년이라고 적혀 있던 것이었다.

불교 국가인 태국은 불멸기원(佛滅紀元), 즉 석가모니가 열반한 해를 기준으로 연도를 세는 불기를 사용한다. 반면, 우리나라는 서기 연도를 사용하고 있다. 불기 연도가 주어질 때 이를 서기 연도로 바꿔 주는 프로그램을 작성하시오.

입력
서기 연도를 알아보고 싶은 불기 연도 y가 주어진다. (1000 ≤ y ≤ 3000)

출력
불기 연도를 서기 연도로 변환한 결과를 출력한다.

예제
입력 : 2541
출력 : 1998

참고
input() 함수는 속도가 느리다는 단점이 있다.
sys.stdin.readline() 함수는 input() 함수보다 속도가 빠르다.
sys.stdin.readline() 함수는 sys 모듈을 호출해야고 대량 데이터 처리에 용이하다.
sys.stdin.readline() 함수는 개행문자가 뒤에 붙는다.
sys.stdin.readline() 함수에 strip() 함수를 사용하여 개행문자를 제거할 수 있다.
format() 함수는 PHP 의 sprint() 함수와 유사하다.
range(start, stop, step) 함수의 인자 start 와 stop 은 start <= value < stop 이다. (between 아님, stop 범위 조건에 주의)
'''

# 정답 1
# print(int(input()) - 543)

# 정답 2
# sys.stdin.readline() 함수는 input() 함수보다 속도가 빠르다.
# import sys
# print(int(sys.stdin.readline()) - 543)

# 정답 3
# y = input()
# if not y.isnumeric():
#     print('숫자를 입력해주세요.')
# else:
#     y = int(y)
#     print(y-543 if y >= 1000 and y <= 3000 else y)

# 정답 4
# import sys
# y = sys.stdin.readline().strip()    # 개행문자 제거
# try:
#     y = int(y)  # 정수가 아닌 경우 오류 발생
#     print(y-543 if y >= 1000 and y <= 3000 else "1000 ~ 3000 사이의 양수를 입력해주세요.")
# except ValueError:
#     pass    # 예외 오류를 무시함

# 정답 5
import sys, re
y = sys.stdin.readline().strip()
print(int(y)-543 if not re.search("\D", y) and int(y) in range(1000, 3001) else "1000 ~ 3000 사이의 양수를 입력해주세요.")
# print("1000 ~ 3000 사이의 양수를 입력해주세요." if re.search("\D", y) or int(y) < 1000 or int(y) > 3000 else int(y)-543)

# 테스트
# y = input()
# print(int(y) if y.isnumeric() else 'y 는 숫자가 아닙니다.')
# print("입력값:{}\n{}는 숫자일까요?".format(y, y))
# print(int(y) if y.isdigit() else "{}는 숫자가 아닙니다.".format(y))

# y = input()
# y = int(y) if y.isnumeric() else 0
# print(y-543 if y >= 1000 and y <= 3000 else y)

# y = input()
#print(int(y)-543 if y.isnumeric() and int(y) >= 1000 and int(y) <= 3000 else y)

# import sys
# y = sys.stdin.readline()
# print(
#     y,
#     y.strip(),
#     sep='\n'
# )

# import sys
# y = sys.stdin.readline()
# if not y.strip().isdigit():
#     print('숫자를 입력해주세요.')
# else:
#     y = int(y)
#     print(y-543 if y >= 1000 and y <= 3000 else y)

