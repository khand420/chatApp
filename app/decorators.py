import time
def timeCalculations(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        
        print(f'Time Calculations of {func.__name__} took {start_time-end_time} seconds')
        return result
    return wrapper


@timeCalculations
def add():
    return 2+4   


print(add()) 