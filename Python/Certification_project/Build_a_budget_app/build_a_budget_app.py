class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
        print(self.ledger)

    def withdraw(self, amount, description = ''):
        amount = amount - amount * 2

        self.ledger.append({'amount': amount, 'description': description})

        ingresos = 0
        retiros = 0

        for i in self.ledger:
            if i['amount'] > 0:
                ingresos += i['amount']
            else:
                retiros += abs(i['amount'])

        if ingresos >= retiros:
            return True

    def get_balance(self):
        ingresos = 0
        retiros = 0

        for i in self.ledger:
            if i['amount'] > 0:
                ingresos += i['amount']
            else:
                retiros += abs(i['amount'])

        return ingresos - retiros

    def transfer(self, amount, category):
        category.withdraw(amount, f'Transfer to {category.name}')

def create_spend_chart(categories):
    pass

def main():
    food = Category('food')
    food.deposit(900, 'deposit')
    food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
    print(food.get_balance())

if __name__ == '__main__':
    main()
