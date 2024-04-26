from numpy import sin
from numpy import arange


def Runge_method(k):
    def Runge(method):
        def wrapper(f, a, b, n):
            res = (method(f, a, b, n * 2) - method(f, a, b, n)) / ((2 ** k) - 1)
            print(f"Runge: {res}")
            return method(f, a, b, n)
        print("хуй соси")

        return wrapper

    return Runge


@Runge_method(k=2)
def pr_left_method(func, a, b, n):
    h = (b - a) / n
    return sum([h * func(x) for x in arange(a, b, h)])


@Runge_method(k=2)
def pr_right_method(func, a, b, n):
    h = (b - a) / n
    return sum([h * func(x) for x in arange(a + h, b, h)] + [h * func(b)])