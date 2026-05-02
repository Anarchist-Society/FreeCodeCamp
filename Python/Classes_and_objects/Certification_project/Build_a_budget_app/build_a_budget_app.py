class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        if not description:
            description = ''

        self.ledger.append(f'amount: {amount}, description: {description}')

    def withdraw(self, amount, description):
        pass

def create_spend_chart(categories):
    pass

def main():
    categoria_01 = Category('Juegos')
    categoria_02 = Category('Libros')

    categoria_01.deposit(100, 'Brawl Star')
    categoria_02.deposit(50, '')

if __name__ == '__main__':
    main()
