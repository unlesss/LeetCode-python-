def minimum_operations(self, num: str) -> int:
    n = len(num)
    ans = n - ('0' in num)

    def f(tail: str) -> int:
        i = num.rfind(tail[1])
        if i < 0:
            return n
        i = num.rfind(tail[0], 0, i)
        if i < 0:
            return n
        return n - i - 2

    return min(ans, f("00"), f("25"), f("50"), f("75"))


def minimum_operations_once(self, num: str) -> int:
    n = len(num)
    found0 = found5 = False
    for i in range(n - 1, -1, -1):
        c = num[i]
        if found0 and c in "05" or found5 and c in "27":
            return n - i - 2
        if c == '0':
            found0 = True
        elif c == '5':
            found5 = True
    return n - found0
