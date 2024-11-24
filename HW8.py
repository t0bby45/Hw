import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время работы функции {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper

@measure_time
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

def test_measure_time():
    result = example_function(1000000)
    assert result == 499999500000, "Тест не пройден"

test_measure_time()
