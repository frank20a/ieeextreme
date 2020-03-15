import sys

sys.setrecursionlimit(100000)


# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


F = {}
def fibo(i):
    if i == 0: return 0
    if i == 1: return 1
    if i not in F.keys(): F[i] = fibo(i - 1) + fibo(i - 2)
    return F[i]


n = get_number()

for i in range(n):
    a = get_number()
    print(fibo(a + 1) % 10)
