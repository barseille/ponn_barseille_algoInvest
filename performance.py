from time import perf_counter


def performance(func):
    """Monitor process time for a function"""

    def wrapper(*args, **kawrgs):
        t1 = perf_counter()
        result = func(*args, **kawrgs)
        t2 = perf_counter()
        print(f"\nThe function {func.__name__} took {round(t2 - t1, 5)} s")
        return result
    return wrapper