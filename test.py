# 약수 구하기
# n = int(input())
# l = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         l.append(i)
#         print(i)
# print(l)

# 약수 판별
# return bool
def is_divisor(factor: int, n: int) -> bool:
    if n % factor == 0:
        return True
    else:
        return False


# 약수 목록 구하기
# return list
def get_divisors(n: int) -> list:
    divisors = []
    for i in range(1, n + 1):
        if is_divisor(i, n):
            divisors.append(i)
    return divisors


# 10의 약수
get_divisors(10)  # >>> [1, 2, 5, 10]

# 이진수 구하기
