"""
1차원 배열,,,10807,,,개수 세기

문제
총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다.
둘째 줄에는 정수가 공백으로 구분되어져있다.
셋째 줄에는 찾으려고 하는 정수 v가 주어진다.
입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.
"""

# 정답 1
# n, s, v = open(0)
# print(s.split().count(v.strip()))

# 정답 2
"""
s 변수에 input 객체 할당
첫번째 s() : 첫째 줄에 입력된 정수의 개수
두번째 s() : 두번째 줄에 입력된 정수 목록
세번째 s() : 세번째 줄에 입력된 찾으려는 정수
"""
s = input; s(); print(s().split().count(s()))

# 테스트
# n, s, v = open(0)
# print(n, s, v, sep='\n')
# print(s.split().count(v))
# print([s.split()].count(v))
# print(s.split().count(v.strip()))

# print(type(input()))
# print(type(input))      # builtin_function_or_method

# s1 = input()
# s2 = input
# print(s2())
# print(type(s1), type(s2), sep='\n')
