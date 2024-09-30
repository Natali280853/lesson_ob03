class Autor():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


class Book():
    def __init__(self, title, autor):
        self.title = title
        self.autor = autor

    def get_info_book(self):
        print(f"{self.title}. {self.autor.name}, {self.autor.nationality} ")

autor = Autor("Федор Достоевский", "русский")
book = Book("Идиот", autor)

book.get_info_book()
