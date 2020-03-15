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


def writer(n, A):
    res = ''
    if n:
        res += 'A '
    else:
        res += 'Q '
    for i in A: res += str(i) + " "
    print(res)


n = get_number()

A = [0 for i in range(n)]

writer(False, A)

d = get_number()
for i in range(n):
    A[i] = 1
    writer(False, A)
    dd = get_number()
    if dd < d:
        A[i] = 0
    else:
        d = dd

writer(True, A)