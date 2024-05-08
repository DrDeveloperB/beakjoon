'''
조건문,,,2884,,,알람 시계

문제
상근이는 매일 아침 알람을 듣고 일어난다. 알람을 듣고 바로 일어나면 다행이겠지만, 항상 조금만 더 자려는 마음 때문에 매일 학교를 지각하고 있다.

상근이는 모든 방법을 동원해보았지만, 조금만 더 자려는 마음은 그 어떤 것도 없앨 수가 없었다.

이런 상근이를 불쌍하게 보던 창영이는 자신이 사용하는 방법을 추천해 주었다.

바로 "45분 일찍 알람 설정하기"이다.

이 방법은 단순하다. 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다. 어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다. 이 방법을 사용하면, 매일 아침 더 잤다는 기분을 느낄 수 있고, 학교도 지각하지 않게 된다.

현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 알람 시간 H시 M분을 의미한다.

입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.

출력
첫째 줄에 상근이가 창영이의 방법을 사용할 때, 설정해야 하는 알람 시간을 출력한다. (입력과 같은 형태로 출력하면 된다.)

참고
나눗셈의 기본 공식
a / b 일때 a = bq + r(0 <= r <= |b|)
a : 피제수
b : 제수
q : 몫
r : 나머지 (0 보다 크거나 같고 제수의 절대값보다 작거나 같은 수)

올림 : +(양수) 방향으로 가까운 정수 선택
내림 : -(음수) 방향으로 가까운 정수 선택
버림 : 0의 방향으로 가까운 정수 선택

1. 파이썬에서 몫을 구하는 연산자 // 에서 몫은 구해진 수를 내림처리한 수이다. (나누기 연산자 / 사용 후 int() 함수로 처리하면 버림처리됨)
2. [1] 번 항목의 규칙으로인해 a / b 일때 파이썬에서 나머지 수의 부호는 b 의 부호와 같다. (양수로 나누면 양수, 음수로 나누면 음수)
예시 1)
6/4 = 1.5   # int(6/4) = 1
6//4 = 1    # 0 < 1 < 1.5 < 2 에서 구해진 수를 내림처리하여 구해진 수보다 작은 정수중 가장 큰 정수를 반환
6%4 = 2     # 6 = (4 * 1) + 2 (몫이 1 이므로 나머지는 2)
예시 2)
-6/4 = -1.5   # int(-6/4) = -1
-6//4 = -2    # -3 < -2 < -1.5 < -1 에서 구해진 수를 내림처리하여 구해진 수보다 작은 정수중 가장 큰 정수를 반환
-6%4 = 2    # -6 = (4 * (-2)) + 2 (몫이 -2 이므로 나머지는 2)

예시 3)
1/24 = 0.041666666666666664   # int(1/24) = 0
1//24 = 0   # -1 < 0 < 0.041 < 1 에서 구해진 수를 내림처리하여 구해진 수보다 작은 정수중 가장 큰 정수를 반환
1%24 = 1    # 1 = (24 * 0) + 1 (몫이 0 이므로 나머지는 1)
예시 4)
-1/24 = -0.041666666666666664   # int(-1/24) = 0
-1//24 = -1   # -2 < -1 < -0.041 < 0 에서 구해진 수를 내림처리하여 구해진 수보다 작은 정수중 가장 큰 정수를 반환
-1%24 = 23    # -1 = (24 * (-1)) + 23  (몫이 -1 이므로 나머지는 23)

예시 5)
2/24 = 0.08333333333333333   # int(2/24) = 0
2//24 = 0   # -1 < 0 < 0.083 < 1 에서 구해진 수를 내림처리하여 구해진 수보다 작은 정수중 가장 큰 정수를 반환
2%24 = 2    # 2 = (24 * 0) + 2 (몫이 0 이므로 나머지는 2)
예시 6)
-2/24 = -0.08333333333333333   # int(-2/24) = 0
-2//24 = -1   # -2 < -1 < -0.083 < 0 에서 구해진 수를 내림처리하여 구해진 수보다 작은 정수중 가장 큰 정수를 반환
-2%24 = 22    # -2 = (24 * (-1)) + 22  (몫이 -1 이므로 나머지는 22)

예시 7)
25/24 = 1.0416666666666667   # int(25/24) = 1
25//24 = 1   # 0 < 1 < 1.041 < 2 에서 구해진 수를 내림처리하여 구해진 수보다 작은 정수중 가장 큰 정수를 반환
25%24 = 1    # 25 = (24 * 1) + 1 (몫이 1 이므로 나머지는 1)
예시 8)
-25/24 = -1.0416666666666667   # int(-25/24) = -1
-25//24 = -2   # -3 < -2 < -1.041 < -1 에서 구해진 수를 내림처리하여 구해진 수보다 작은 정수중 가장 큰 정수를 반환
-25%24 = 23    # -25 = (24 * (-2)) + 23  (몫이 -2 이므로 나머지는 23)
예시 9)
25/-24 = -1.0416666666666667   # int(25/-24) = -1
25//-24 = -2   # -3 < -2 < -1.041 < -1 에서 구해진 수를 내림처리하여 구해진 수보다 작은 정수중 가장 큰 정수를 반환
25%-24 = -23    # 25 = ((-24) * (-2)) + (-23) = 48 - 23  (몫이 -2 이므로 나머지는 -23)
'''

# 정답 1
# h, m = map(int, input().split())
# if m >= 45:
#     m = m - 45
# else:
#     h = 23 if h == 0 else h - 1
#     m = (m + 60) - 45
# print(f'{h} {m}')

# 정답 2
# h, m = map(int, input().split())
# h = 24 if h == 0 and m < 45 else h
# h, m = divmod((((h * 60) + m) - 45), 60)
# print('{} {}'.format(h, m))

# 정답 3
# h, m = map(int, input().split())
# print('{} {}'.format(
#     (((h - 1) % 24) + (((m + 60) - 45) // 60)) % 24,
#     ((m + 60) - 45) % 60
# )
# )

# 정답 4
# h, m = map(int, input().split())
# print('{} {}'.format(
#     (h - (m < 45)) % 24,
#     (m + ((m < 45) * 60)) - 45
# )
# )

# 정답 5
h, m = map(int, input().split())
print(
    (h - (m < 45)) % 24,
    (m - 45) % 60
)

# 테스트
# print(
#     6/4, 6//4, 6%4,
#     -6/4, -6//4, -6%4,
#     sep='\n'
# )
# print(
#     1/24, 1//24, 1%24,
#     -1/24, -1//24, -1%24,
#     sep='\n'
# )
# print(
#     2/24, 2//24, 2%24,
#     -2/24, -2//24, -2%24,
#     sep='\n'
# )
# print(
#     25/24, 25//24, 25%24,
#     -25/24, -25//24, -25%24,
#     25/-24, 25//-24, 25%-24,
#     sep='\n'
# )
