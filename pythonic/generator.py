# 生成器
# 解决占用资源问题
# 生成器针对函数，迭代器针对对象


def gen(max_gen):
    n = 0
    while n <= max_gen:
        # print(n)
        n += 1
        yield n


g = gen(50000)
for i in g:
    print(i)
