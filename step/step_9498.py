'''
조건문,,,9498,,,시험 성적

문제
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
시험 성적을 출력한다.
'''

# 정답 1
# a = int(input())
# if not 0 <= a <= 100:
#     print('0 ~ 100 사이의 숫자를 입력해주세요.')
#     exit()
# if a >= 90:
#     print('A')
# elif a in range(80, 90):
#     print('B')
# elif a in range(70, 80):
#     print('C')
# elif a in range(60, 70):
#     print('D')
# else:
#     print('F')

# 정답 2
# list = [
#     {
#         'score':'A',
#         'min':90,
#         'max':100,
#     },
#     {
#         'score':'B',
#         'min':80,
#         'max':89,
#     },
#     {
#         'score':'C',
#         'min':70,
#         'max':79,
#     },
#     {
#         'score':'D',
#         'min':60,
#         'max':69,
#     },
#     {
#         'score':'F',
#         'min':0,
#         'max':59,
#     },
# ]
# a = int(input())
# for item in list:
#     if item['min'] <= a <= item['max']:
#         print(item['score'])
#         exit()
# print('0 ~ 100 사이의 숫자를 입력해주세요.')

# 정답 3
# import sys, re
# list = [
#     {
#         'score':'A',
#         'min':90,
#         'max':100,
#     },
#     {
#         'score':'B',
#         'min':80,
#         'max':89,
#     },
#     {
#         'score':'C',
#         'min':70,
#         'max':79,
#     },
#     {
#         'score':'D',
#         'min':60,
#         'max':69,
#     },
#     {
#         'score':'F',
#         'min':0,
#         'max':59,
#     },
# ]
# def change_int(v):
#     v = v.strip()
#     if bool(re.sub("\s", "", v)) == False:
#         return "숫자로 변환할 값이 주어지지않았습니다."
#     if re.search("^-?[0-9]+$", v) is None:
#         return "{} 은(는) 숫자가 아닙니다.".format(v)
#     v = int(v)
#     if v not in range(0, 101, 1):
#         return "{} 은(는) 수의 범위에 포함되지 않습니다.".format(v)
#     return v
# a = change_int(sys.stdin.readline())
# if not isinstance(a, int):
#     print(a)
#     exit()
# for item in list:
#     if item['min'] <= a <= item['max']:
#         print(item['score'])
#         break

# 정답 4
# a = int(input())
# print(
#     [
#         [
#             [
#                 ['F', 'D'][a>=60], 
#                 'C'
#             ][a>=70], 
#             'B'
#         ][a>=80], 
#         'A'
#     ][a>=90]
# )

# 정답 5
print('FFFFFFDCBAA'[int(input())//10])

# 테스트
# list = [
#     {
#         'score':'A',
#         'min':90,
#         'max':100,
#     },
#     {
#         'score':'B',
#         'min':80,
#         'max':89,
#     },
#     {
#         'score':'C',
#         'min':70,
#         'max':79,
#     },
#     {
#         'score':'D',
#         'min':60,
#         'max':69,
#     },
#     {
#         'score':'F',
#         'min':0,
#         'max':59,
#     },
# ]
# a = int(input())
# for item in list:
#     # print(
#     #     item, item['score'], 
#     #     sep='\n'
#     # )
#     if item['min'] <= a <= item['max']:
#         print(item['score'])
#         exit()
# print('0 ~ 100 사이의 숫자를 입력해주세요.')
    
# print(
#     list, list[0], list[0]['score'], 
#     sep='\n'
# )

