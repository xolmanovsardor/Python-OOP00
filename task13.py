class Book:
    def __init__(self, title, author, is_read=False):
        self.title = title
        self.author = author
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True

    def status(self):
        print(f"{self.title}: {'O‘qilgan' if self.is_read else 'O‘qilmagan'}")

# Test
b1 = Book("Kitob 1", "Muallif A")
b2 = Book("Kitob 2", "Muallif B")
b3 = Book("Kitob 3", "Muallif C")
b4 = Book("Kitob 4", "Muallif D")

b1.mark_as_read()
b3.mark_as_read()

for b in [b1, b2, b3, b4]:
    b.status()
