import time
import functools

def square(x):
    return x*x
    
def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} is runnning.")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} execution time: {end_time - start_time} seconds.")
        return result
    return wrapper

decorated_square = decorator(square)
print(decorated_square(5))

square = decorator(square)
print(square(5))

@decorator
def square(x):
    return x*x

print(square(5))

def timer(threshold):
    def decorator(func):
        @functools.wraps(func) # 保留原始函數的名稱和文檔字符串
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            if end_time - start_time > threshold:
                print(f"{func.__name__} took longer than {threshold}.")
            return result
        return wrapper
    return decorator

# 等價於 sleep_04 = timer(0.2)(sleep_04)
@timer(0.2) # timer 返回一個裝飾器，這個裝飾器會檢查函數的執行時間是否超過 0.2 秒
def sleep_04():
    time.sleep(0.4)

sleep_04()

print(sleep_04.__name__)  # 如果沒有使用 functools.wraps，這裡會輸出 wrapper，而不是 sleep_04