class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': float(f"-{amount}"), 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = '*' * ((30 - len(self.category)) // 2) + self.category + '*' * ((30 - len(self.category)) // 2) + '\n'
        transactions = ''
        for transaction in self.ledger:
            transactions += transaction['description'][:23] + ' ' +' ' * (23 - len(transaction['description'][:23])) + f"{transaction['amount']:.2f}\n"
        total = f'Total: {self.get_balance()}'
        return title + transactions + total

def create_spend_chart(category_list):
    #Title
    title = "Percentage spent by category"
    #Barchart
    barchart = ""
    total = 0
    category_percentage = []
    category_sum_list = []
    category_fill = []
    for category in category_list:
        category_sum = 0
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                #print(transaction['amount'])
                category_sum = category_sum - transaction['amount']
        category_sum_list.append(category_sum)
    total = round(sum(category_sum_list), 2)
    for item in category_sum_list:
        category_percentage.append(round(item * 100 / total, 2))
    for item in category_percentage:
        category_fill.append(round((item // 10) * 10))
    for x in range (100, -1, -10):
        barchart += f'\n{str(x).rjust(3, " ")}| '
        for item in category_fill:
            if item >= x:
                barchart += 'o  '
            else:
                barchart += '   '
    barchart += "\n    -" + "-" * 3 * len(category_list)
    #Category
    max_string_length = 0
    names = ""
    for category in category_list:
        if len(category.category) > max_string_length:
            max_string_length = len(category.category)
    for i in range(max_string_length):
        names += "\n     "
        for x in category_list:
            if 0 <= i < len(x.category):
                litera = x.category[i]
            else:
                litera = " "
            names += litera + "  "
    return title + barchart + names
