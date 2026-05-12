class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ""):
        amount = amount - amount * 2

        self.ledger.append({'amount': amount, 'description': description})

def create_spend_chart(categories):
    pass

def main():
    lista = []

    lista.append({'amount': 100, 'description': 'Brawl Star'})

    print(lista[0]['amount'])

if __name__ == '__main__':
    main()
