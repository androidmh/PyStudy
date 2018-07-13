# 函数式编程
# 闭包


def curve_pre():
    a = 25

    def curve(x):
        return a * x * x
    return curve


a = 10
f = curve_pre()
print(f(2))