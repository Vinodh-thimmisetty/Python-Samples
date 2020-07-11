"""
    Decorators are side-effect: Function(A) which takes Function(B) and returns Function(C)
    Modify existing Functions without changing the function Declaration.

"""
compensation = {
    range(1, 10): 10,
    range(10, 20): 25,
    range(20, 30): 50,
    range(30, 40): 75,
    range(40, 100): 100
}

exclude_branch = {
    'MECH': 10,
    'CIVIL': 10
}

min_grade = 60
max_grade = 90
common_grade = 75


def timer(fn):
    from functools import wraps
    from time import perf_counter, sleep

    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = fn(*args, *kwargs)
        sleep(2)  # mocking the time-taken for completing the function.
        end_time = perf_counter()
        print(f'{fn.__name__!r} took [{end_time - start_time : .4f} sec(s)]')
        return result;

    return wrapper


class Log:
    def __init__(self, enable=True):
        self._enable = enable

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    def __call__(self, fn):
        from functools import wraps
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if self.enable:
                print(f'Tracing the Fn {fn.__name__!r}')
            result = fn(*args, **kwargs)
            return result

        return wrapper


class Counter:
    def __init__(self, fn):
        self._count = 0
        self.fn = fn

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value=1):
        self._count += value

    @timer
    def __call__(self, *args, **kwargs):
        self._count += 1
        print(f"{self.fn.__name__!r} fn is invoked {self._count} times")
        return self.fn(*args, **kwargs)


def calculate_compensation(adj_percent):
    for rnge in compensation.keys():
        if round(adj_percent) in rnge:
            total_pay = compensation[rnge]
            break
    return total_pay


def adjust_grade(fn):
    from functools import wraps

    @wraps(fn)  # Preserve original function information [Introspection]
    def wrap(*args, **kwargs):
        result = fn(*args, *kwargs)
        if result < min_grade:
            adjust = (common_grade - result)
            total_pay = calculate_compensation(adjust)
            print(
                f'Actual Grade : [{result}] | '
                f'Final Grade : [{common_grade}] | '
                f'Adjusted : [+{adjust}%] | '
                f'Compensation : [${total_pay}]')
        elif result > max_grade:
            adjust = (result - common_grade)
            total_pay = calculate_compensation(adjust)
            print(
                f'Actual Grade : [{result}] | '
                f'Final Grade : [{common_grade}] | '
                f'Adjusted : [-{adjust}%] | '
                f'Compensation : [${total_pay}]')
        else:
            pass

        return common_grade

    return wrap


def adjust_compensation(_fn=None, *, branch='MECH'):  # make sure branch is keyword-arg
    def branch_specific(fn):
        from functools import wraps
        @wraps(fn)
        def wrap(*args, **kwargs):
            result = fn(*args, *kwargs)
            if branch in exclude_branch.keys():
                result += exclude_branch[branch]
                print(f'Exceptional compensation for Branch [{branch}]')
            return result

        return wrap

    if _fn is None:
        return branch_specific
    return branch_specific(_fn)


@Counter
@adjust_compensation
# @adjust_compensation(branch='CIVIL')
@adjust_grade  # pie syntax
def final_results(input):
    return sum(input) / len(input)


@Log()
# @Log(False)
def rotate_list(l):
    return l[1:] + [l[0]]


if __name__ == '__main__':
    higher_grades = [90, 90, 100, 100]
    lower_grades = [30, 40, 30, 50]
    # print(adjust_grade(marks)(subjects))
    print(final_results(higher_grades))
    print(final_results(lower_grades))
    print(f'final_results is called {final_results.count} times')

    print(rotate_list(higher_grades))
    print(rotate_list(lower_grades))
