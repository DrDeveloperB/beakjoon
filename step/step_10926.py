'''
문제
준하는 사이트에 회원가입을 하다가 joonas라는 아이디가 이미 존재하는 것을 보고 놀랐다. 준하는 놀람을 ??!로 표현한다. 준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어졌을 때, 놀람을 표현하는 프로그램을 작성하시오.

입력
첫째 줄에 준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어진다. 아이디는 알파벳 소문자로만 이루어져 있으며, 길이는 50자를 넘지 않는다.

출력
첫째 줄에 준하의 놀람을 출력한다. 놀람은 아이디 뒤에 ??!를 붙여서 나타낸다.

참조
id = input()
id2 = input()
print(type(id))
print(type(id2))    # id 와 id2 는 다른 값이다.
print(type(input()))    # 위에서 가져온 input() 과 여기의 input() 는 다른 값이다.
1. 기본적으로 input() 으로 전달되는 값은 하나의 라인이다.
2. 코드 실행 후 input() 함수가 실행될때마다 값을 입력받기위해 대기한다. (엔터 행위가 일어나기전까지 다음 로직 실행 안함)
3. 코드 실행 순서
ex) 코드 실행
    id = input() 로직에서 입력 대기
    input 1 입력 후 엔터
    id 에 input 1 문자열이 대입됨
    id2 = input() 로직에서 입력 대기
    input 2 입력 후 엔터
    id 에 input 2 문자열이 대입됨
    print 함수에 의한 출력 : type(id) (<class 'str'>)
    print 함수에 의한 출력 : type(id2) (<class 'str'>)
    print(type(input())) 로직에서 입력 대기
    input 3 입력 후 엔터
    print 함수에 의한 출력 : type(input()) (<class 'str'>)
    코드 실행 종료

4. 조건문 코딩시 input() 으로 코딩하면 안됨
ex) 삼항 연산자 사용
    print(input() + '??!' if input() else 'input is empty')
    첫번째 input() 과 두번째 input() 이 입력받는 행위가 달라 값을 각각 전달받으므로 동일한 값으로 if 문이 실행되지 않음

ex) 하나의 변수에 대입 후 사용해야함
    id3 = input()
    id3 변수에 대입 후
    print(id3 + '??!' if id3 else 'input is empty')
    또는 아래 로직 실행
    print('input is empty' if not id3 else id3 + '??!')
    여기서 not 의 의미는 PHP 의 empty() 와 유사함

5. 문자열 나누기
    split() 함수 : 공백을 기준으로 나눔
    문자열.split(sep='구분자', maxsplit=분할횟수)
ex) ids = input().split()
    print(type(ids), ids, sep='\n')
    1 2  3 입력시
    <class 'list'>
    ['1', '2', '3']
    기본값인 공백으로 나눌때 공백이 연속되는 횟수와 무관함
'''
# 정답 1
# print(input() + "??!")

# 정답 2
# id = input()
# if id:
#     print(str(id) + '??!')
    # print(id, '??!', sep='')

# 정답 3
id = input()
print('' if not id else id + "??!")