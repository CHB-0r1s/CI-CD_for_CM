from main import pr_left_method


def test_pr_left_method_ok():
    func = lambda x: x**3 - x**2
    a, b = 0, 2
    n = 10
    assert abs(4/3 - pr_left_method(func, a, b, n)) < 0.1
