"""
非闭包解决方案
"""
origin = 0


# def go(step):
#     global origin
#     origin += step
#     return origin
#
#
# print(go(2))
# print(go(3))
# print(go(6))

'''
    闭包解决方案
'''


def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go


tourist = factory(origin)
print(tourist(2))
print(tourist(3))
print(tourist(5))