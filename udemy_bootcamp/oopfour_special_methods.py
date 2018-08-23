class Book(object):
    """docstring for Book."""
    def __init__(self, title, author, pages):
        super(Book, self).__init__()
        self.title = title
        self.author = author
        self.pages = pages
        print("A book has been created !")

    def __str__(self):
        return "Title: %s, Author: %s, pages: %s " %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is deleted !")


b = Book('Jai sold his ego !', 'Jai', '23' )

print(b)
del b
# print(b) // works proper
