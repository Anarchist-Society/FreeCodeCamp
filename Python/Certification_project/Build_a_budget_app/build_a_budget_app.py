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
    resultado = 'Percentage spent by category\n'

    total_retiro_por_categoria = {}
    porcentajes_por_categoria = {}
    total_retiros = 0

    for category in categories:
        nombre = category.name
        movimientos = category.ledger
        retiros = 0

        for movimiento in movimientos:
            cantidad = movimiento['amount']

            if cantidad < 0:
                total_retiros += -cantidad
                retiros += -cantidad

        total_retiro_por_categoria[nombre] = retiros

    for nombre, cantidad in total_retiro_por_categoria.items():
        cantidad = (round(((cantidad / total_retiros) * 100) / 10)) * 10
        porcentajes_por_categoria[nombre] = cantidad

    for i in range(100, -10, -10):
        line = f'{i : > 3}| '

        for porcentaje in porcentajes_por_categoria.values():

            if porcentaje >= i:
                line += 'o '
            else:
                line += ' '

        resultado += line + '\n'

    resultado += '   ----------'

    for nombres in total_retiro_por_categoria.keys():
        for nombre in nombres:

    print(resultado)

def main():
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(105.55, "groceries")
    food.withdraw(33.40, "restaurant")
    
    clothing = Category("Clothing")
    clothing.deposit(500, "initial deposit")
    clothing.withdraw(25.55, "shirt")
    clothing.withdraw(100, "jeans")
    
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15, "gas")

    create_spend_chart([food, clothing, auto])

if __name__ == '__main__':
    main()
