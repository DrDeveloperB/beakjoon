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
# get_divisors(10)  # >>> [1, 2, 5, 10]


# 이진수 구하기

# yaml 사용
def use_yaml():
    import yaml

    yaml_data = """
color_def:
    - &col1 "#ff0000"
    - &col2 "#00ff00"
    - &col3 "#0000ff"

color:
    title1: *col1
    title2: *col2
    title3: *col3
"""

    data = yaml.load(yaml_data, Loader=yaml.FullLoader)

    print("title1 = ", data["color"]["title1"])
    print("title2 = ", data["color"]["title2"])
    print("title3 = ", data["color"]["title3"])


# use_yaml()


def use_yaml_file():
    import yaml
    file = './test/test.yml'

    # stream = open(file, 'rt', encoding='UTF8')
    # print(stream)
    # doc = yaml.load(stream, Loader=yaml.FullLoader)
    # print(doc)

    # with open(file, 'rt', encoding='UTF8') as stream:
    #     doc = yaml.load(stream, Loader=yaml.FullLoader)
    #     print(doc)

    stream = open(file, 'rt', encoding='UTF8')
    docs = yaml.load_all(stream, yaml.FullLoader)
    for doc in docs:
        print(doc)
        # for k, v in doc.items():
        #     print(k, "->", v)
        print("\n")


use_yaml_file()
