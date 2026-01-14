import time
from functools import wraps

def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"Function '{func.__name__}' executed in {end_time - start_time:.5f} seconds")
        return result

    return wrapper
@execution_time
def sample_function():
    for n in range(1000000):
        pass

sample_function()
