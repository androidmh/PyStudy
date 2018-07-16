"""
    装饰器（注解）
"""
import time


def decorator(func):
    def wrapper(*args, **kwargs):
        print(time.time())
        func(*args, **kwargs)

    return wrapper


@decorator
def f1(func_name):
    print('This is a function' + func_name)


@decorator
def f2(func_name1, func_name2):
    print('This is a function' + func_name1)
    print('This is a function' + func_name2)


@decorator
def f3(func_name1, func_name2, **kw):
    print('This is a function' + func_name1)
    print('This is a function' + func_name2)
    print(kw)


f1('test')
f2('test1', 'test2')
f3('test1', 'test2', a=1, b=2, c='123')

