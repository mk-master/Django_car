import time

cache_dict = {}

def calc_fun(num1, num2):

    print("start")

    key = f"{calc_fun.__name__}_{num1}_{num2}" 
    if key in cache_dict:
        return cache_dict[key]

    time.sleep(5)
    value = num1 + num2
    cache_dict[key] = value
    return value

result = calc_fun(1,2)

# Механизм кеширования
num1 = 1
num2 = 2
key = f"{calc_fun.__name__}_{num1}_{num2}" 
value = result
cache_dict[key] = value

result = calc_fun(1,2)
result = calc_fun(1,2)
result = calc_fun(1,2)
result = calc_fun(1,2)
