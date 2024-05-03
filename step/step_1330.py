'''
문제
두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

출력
첫째 줄에 다음 세 가지 중 하나를 출력한다.

A가 B보다 큰 경우에는 '>'를 출력한다.
A가 B보다 작은 경우에는 '<'를 출력한다.
A와 B가 같은 경우에는 '=='를 출력한다.

제한
-10,000 ≤ A, B ≤ 10,000

참고
문자열에서 인덱스번호를 붙이면 리스트처럼 조회할 수 있다.
예를 들어 
qwe 문자가 있고
qwe[0] 으로 조회하면 q 가 조회된다.
qwe[1] 은 w 다.
True 는 1 False 는 0 이므로 qwe[False] == q, qwe[True] == w 다.
'''

# 정답 1
# a, b = map(int, input().split())
# if a < b:
#     print('<')
# elif a > b:
#     print('>')
# else:
#     print('==')

# 정답 2
# import sys, re
# def change_int(v, s, e):
#     p = re.compile("^-?[0-9]+$")
#     if not v:
#         return "숫자로 변환할 값이 주어지지않았습니다."
#         # return False
#     if p.search(v) is None:
#         return "{} 은(는) 숫자가 아닙니다.".format(v)
#     v = int(v)
#     if s and not e:
#         return "수의 범위중 최대값이 없습니다."
#     if not s and e:
#         return "수의 범위중 최소값이 없습니다."
#     if s and e:
#         if isinstance(s, int) == False:
#             return "{} 은(는) 숫자가 아닙니다.".format(s)
#         if isinstance(e, int) == False:
#             return "{} 은(는) 숫자가 아닙니다.".format(e)
#         if s > e:
#             return "수의 범위중 최소값이 최대값보다 큽니다."
#         if v not in range(s, e, 1):
#             return "{} 은(는) {} ~ {} 사이의 숫자가 아닙니다.".format(v, s, e-1)
#     return v
# i = sys.stdin.readline()
# a, b = map(lambda x : change_int(x, -10000, 10001), i.split())
# if not isinstance(a, int) or not isinstance(b, int):
#     print(a, b, sep='\n')
# else:
#     if a > b:
#         print('>')
#     elif a < b:
#         print('<')
#     else:
#         print('==')

# 정답 3
# import sys, re
# def change_int(v, s, e):
#     p = re.compile("^-?[0-9]+$")
#     if not v:
#         return "숫자로 변환할 값이 주어지지않았습니다."
#         # return False
#     if p.search(v) is None:
#         return "{} 은(는) 숫자가 아닙니다.".format(v)
#     v = int(v)
#     if s and not e:
#         return "수의 범위중 최대값이 없습니다."
#     if not s and e:
#         return "수의 범위중 최소값이 없습니다."
#     if s and e:
#         if isinstance(s, int) == False:
#             return "{} 은(는) 숫자가 아닙니다.".format(s)
#         if isinstance(e, int) == False:
#             return "{} 은(는) 숫자가 아닙니다.".format(e)
#         if s > e:
#             return "수의 범위중 최소값이 최대값보다 큽니다."
#         if v not in range(s, e, 1):
#             return "{} 은(는) {} ~ {} 사이의 숫자가 아닙니다.".format(v, s, e-1)
#     return v
# i = sys.stdin.readline()
# a, b = map(lambda x : change_int(x, -10000, 10001), i.split())
# if not isinstance(a, int) or not isinstance(b, int):
#     print(a, b, sep='\n')
#     exit()
# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else:
#     print('==')

# 정답 4
# import sys, re
# def change_int(v, s, e):
#     p = re.compile("^-?[0-9]+$")
#     if not v:
#         return "숫자로 변환할 값이 주어지지않았습니다."
#         # return False
#     if p.search(v) is None:
#         return "{} 은(는) 숫자가 아닙니다.".format(v)
#     v = int(v)
#     if s and not e:
#         return "수의 범위중 최대값이 없습니다."
#     if not s and e:
#         return "수의 범위중 최소값이 없습니다."
#     if s and e:
#         if isinstance(s, int) == False:
#             return "{} 은(는) 숫자가 아닙니다.".format(s)
#         if isinstance(e, int) == False:
#             return "{} 은(는) 숫자가 아닙니다.".format(e)
#         if s > e:
#             return "수의 범위중 최소값이 최대값보다 큽니다."
#         if v not in range(s, e, 1):
#             return "{} 은(는) {} ~ {} 사이의 숫자가 아닙니다.".format(v, s, e-1)
#     return v
# i = sys.stdin.readline()
# if re.search(" ", i) is None:
#     print('숫자 2개를 한 줄에 공백으로 구분하여 입력해주세요.')
#     exit()
# a, b, *_ = map(lambda x : change_int(x, -10000, 10001), i.split())
# if not isinstance(a, int) or not isinstance(b, int):
#     print(a, b, sep='\n')
#     exit()
# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else:
#     print('==')

# 정답 5
# import sys, re
# def change_int(v):
#     if not v:
#         return "숫자로 변환할 값이 주어지지않았습니다."
#     if re.search("^-?[0-9]+$", v) is None:
#         return "{} 은(는) 숫자가 아닙니다.".format(v)
#     v = int(v)
#     if v not in range(-10000, 10001, 1):
#         return "{} 은(는) 수의 범위에 포함되지 않습니다.".format(v)
#     return v
# i = sys.stdin.readline()
# if re.search(" ", i) is None:
#     print('숫자 2개를 한 줄에 공백으로 구분하여 입력해주세요.')
#     exit()
# a, b, *_ = map(change_int, i.split())
# if not isinstance(a, int) or not isinstance(b, int):
#     print(a, b, sep='\n')
#     exit()
# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else:
#     print('==')

# 정답 6
a,b = map(int, input().split())
print(['><'[a<b], '=='][a==b])



# 테스트
# a, b = map(int, input().split())
# print(a, b, sep='\n')

# import sys, re
# a = input()
# print(re.search("^-?[0-9]+$", a))
# if re.search("^-?[0-9]+$", a) is None:
#     print("{} 은(는) 숫자가 아닙니다.".format(a))
# else:
#     print(int(a))

# import sys, re
# a = sys.stdin.readline()
# print(re.search("^-?[0-9]+$", a))
# p = re.compile("^-?[0-9]+$")
# if p.search(a) is None:
#     print("{} 은(는) 숫자가 아닙니다.".format(a))
# else:
#     print(int(a))

# import sys, re
# i = sys.stdin.readline()
# try:
#     a, b = map(lambda x : change_int(x, -10000, 10001), i.split())
#     if a > b:
#         print('>')
#     elif a < b:
#         print('<')
#     else:
#         print('==')
# except Exception as e:
#     print(e)

# a,b = map(int, input().split())
# print('><'[a<b])