# Clase Category que acepta un nombre como argumento
class Category:
    # Constructor
    def __init__(self, name):
        self.name = name
        self.ledger = [] # Inicializamos la lista que tendrá los ingresos y los retiros

    # Método deposit, que acepta una cantidad y una descripción, si no hay descripción por defecto es un string vacío
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description}) # Lo agregamos el depósito en formato de diccionario a la lista

    def withdraw(self, amount, description = ''):
        self.ledger.append({'amount': -amount, 'description': description})

    def get_balance(self):
        # balance = 0
        
        # for i in self.ledger:
            # balance += i['amount']

        balance = sum(i['amount'] for i in self.ledger)

        return balance

    def transfer(self, amount, category):
        category.withdraw(amount, f'Transfer to {category.name}')

    def check_funds(self, amount):
        balance = self.get_balance()

        if balance < amount:
            return False

        return True

def create_spend_chart(categories):
    pass

def main():
    food = Category('food')
    food.deposit(900, 'deposit')
    food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
    print(food.get_balance())
    print(food.check_funds(853.33))

if __name__ == '__main__':
    main()
