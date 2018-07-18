# 迭代器
# 一次性

class Book:
    pass


class BookCollection:
    def __init__(self):
        self.data = ['《往事》', '《只能》', '《回味》']
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur >= len(self.data):
            raise StopIteration()
        r = self.data[self.cur]
        self.cur += 1
        return r


books = BookCollection()
for book in books:
    print(book)
