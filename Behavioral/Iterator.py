class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def get_iterator(self):
        return BookIterator(self)

class BookIterator:
    def __init__(self, book):
        self.book = book
        self.current_page = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_page < len(self.book.pages):
            page = self.book.pages[self.current_page]
            self.current_page += 1
            return page
        raise StopIteration
    
    def has_next(self):
        return self.current_page < len(self.book.pages)
    
    def current(self):
        if self.current_page < len(self.book.pages):
            return self.book.pages[self.current_page]
        return None

# Использование
book = Book("Война и мир", [
    "Страница 1: Все счастливые семьи похожи друг на друга...",
    "Страница 2: Анна Павловна Шерер, фрейлина...",
    "Страница 3: — Eh bien, mon prince...",
    "Страница 4: Говоря эти слова, он обернулся...",
])

print(f"Читаем книгу: {book.title}")
print("\nЧтение через итератор:")

iterator = book.get_iterator()
for page in iterator:
    print(page[:50] + "...")

# Или вручную
print("\nЧтение вручную с закладкой:")
iterator2 = book.get_iterator()
print(iterator2.current())  # None - сначала нужно начать

while iterator2.has_next():
    page = next(iterator2)
    print(f"Текущая страница: {page[:30]}...")