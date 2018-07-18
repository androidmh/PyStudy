# 列表推导式
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# b = [i ** 3 for i in a if i >= 5]
# print(b)

# dict
students = {
    'aa': 18,
    'bb': 20,
    'cc': 15
}
b = [key for key, value in students.items()]
print(b)
