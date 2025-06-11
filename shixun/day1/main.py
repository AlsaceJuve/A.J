# 提取公共的包装器逻辑
def create_wrapper(func, before_message, after_message):
    def wrapper(*args, **kwargs):
        print(before_message)
        result = func(*args, **kwargs)
        print(after_message)
        return result
    return wrapper

# 简单装饰器
def my_decorator(func):
    return create_wrapper(func, "Before function", "After function")

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# 带参数的装饰器
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hi, {name}!")

greet("Alice")
