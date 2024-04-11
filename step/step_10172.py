'''
문제
아래 예제와 같이 개를 출력하시오.

입력
없음.

출력
개를 출력한다.

예제 출력 1
|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|

참고
row string 코딩시 쌍따옴표나 홑따옴표는 2개까지만 연속으로 사용 가능
3개이상 사용시 3개가 닫힘 문자열로 인식됨
쌍따옴표 3개로 시작시 쌍따옴표 3개 사용불가
홑따옴표 3개로 시작시 홑따옴표 3개 사용불가
굳이 사용하고자 한다면 2개 사용 후 3개로 닫고 (5개 연속 입력)
다시 3개로 열어서 1개 사용 후 (4개 연속 입력) 문자열을 연결 (+ 등등)
이때 strip() 함수가 필요할 수 있음
'''

# 정답 1
# print("""
# |\_/|
# |q p|   /}
# ( 0 )\"\"\"\\
# |"^"`    |
# ||_/=\\\\__|
# """.strip())

# 정답 2
print(r'''
|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|
'''.strip())

# 테스트
# print(r"""what"ev'er""")
# print(r"""
# |\_/|
# |q p|   /}
# ( 0 )""
# """.strip()
# +
# r"""
# "\
# |"^"`    |
# ||_/=\\__|
# """.strip())