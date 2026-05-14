class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        self.ledger.append({'amount': -amount, 'description': description})

        if not self.check_funds(amount):
            return False

        return True

    def transfer(self, amount, category):
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')

        if not self.check_funds(amount):
            return False

        return True

    def get_balance(self):
        # balance = 0
        
        # for i in self.ledger:
            # balance += i['amount']

        balance = sum(i['amount'] for i in self.ledger)

        return balance

    def check_funds(self, amount):
        balance = self.get_balance()

        if balance < amount:
            return False

        return True

    def __str__(self):
        title = self.name.center(30, '*')

        items = []

        for i in self.ledger:
            description = i['description'][:23]
            amount = i['amount']
            items.append(f"{description:<23}{amount:>7.2f}")

        total = f'Total: {self.get_balance():.2f}'

        return title + '\n' + '\n'.join(items) + '\n' + total

def create_spend_chart(categories):
    pass

def main():
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    print(food)

if __name__ == '__main__':
    main()
