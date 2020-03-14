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


def dictSort(x):
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}


def solve(x):
    class Thingy:
        def __init__(self, name, index):
            self.s = index
            self.f = self.s
            self.names = [name]

        def addName(self, name):
            self.names.append(name)
            self.f += 1

    t = 1
    tt = -1
    tH = 0
    r = []
    for i in x:
        if x[i] != tH:
            tH = x[i]
            r.append(Thingy(i, t))
            tt += 1
        else:
            r[tt].addName(i)
        t += 1

    res = ""
    for i in r:
        for j in sorted(i.names): res += j + " "
        res += str(i.s) + " " + str(i.f) + '\n'

    return res


A = {}
for i in range(get_number()):
    n = get_word()
    t = get_number()
    A[n] = t

print(solve(dictSort(A)))
