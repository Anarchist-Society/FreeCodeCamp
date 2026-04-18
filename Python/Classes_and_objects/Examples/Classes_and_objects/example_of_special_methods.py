print('What Are Special Methods and What Are They Used For?\n')

print('Example 1:\n')

class Book_01:
    def __init__(self, title, pages) -> None:
        self.title = title
        self.pages = pages

book1 = Book_01('Built Wealth Like a Boss', 420)
book2 = Book_01('Be Your Own Start', 420)

# print(len(book1)) # TypeError: object of type 'Book' has no len()
# print(str(book1)) # <__main__.Book object at 0x102ed2900>
# print(book1 == book2) # False even though they have the same number of pages


print('Example 2:\n')

class Book_02:
    def __init__(self, title, pages) -> None:
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"

    def __eq__(self, other):
        return self.pages == other.pages

book1 = Book_02('Built Wealth Like a Boss', 420)
book2 = Book_02('Be Your Own Start', 420)

print(len(book1)) # 420
print(len(book2)) # 420
print(str(book1)) # 'Built Wealth Like a Boss' has 420 pages
print(str(book2)) # 'Be Your Own Start' has 420 pages
print(book1 == book2) # True

print('Example 3:\n')

class Cart:
    def __init__(self) -> None:
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def list_items(self):
        return self.items

    # __len__() to get the length of the items in the cart
    def __len__(self):
        return len(self.items)

    # to return or display an item at a specific index in the cart
    def __getitem__(self, index):
        return self.items[index]

    # to check if a specific item is in the cart
    def __contains__(self, item):
        return item in self.items

    # __iter__() to loop through the items in the cart so you can see them
    def __iter__(self):
        return iter(self.items)

cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
    print(item, end = ' ') # Laptop Wireless mouse Ergo keyboard Monitor

print(len(cart)) # 4
print(cart[3]) # Monitor

print('Monitor' in cart) # True
print('banana' in cart) # False

cart.remove('Ergo keyboard')

print(cart.list_items()) # ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove('banana') # banana is not in cart
