from functools import reduce

class Category:
  ledger = None
  category = None
  balance = None

  def __init__(self, category):
    self.ledger = []
    self.balance = 0
    self.category = category

  def deposit(self, amount, description=''):
    
    self.ledger.append({
      'amount': amount,
      'description': description
    })
    
    # add new amount to balance
    self.balance += amount

  def withdraw(self, amount, description=''):

    # if not enough balance, do not add new transaction
    if not self.check_funds(amount):
      return False
    
    self.ledger.append({
      'amount': amount * -1,
      'description': description
    })
    # subtract new amount from balance
    self.balance -= amount
    return True

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    # ignore transfer if there are not enough foundings
    if not self.check_funds(amount):
      return False

    self.withdraw(amount, f"Transfer to {category.category}")
    category.deposit(amount, f"Transfer from {self.category}")

    return True

  def check_funds(self, amount):
    return self.get_balance() >= amount

  def __str__(self):
    resume = self.category.center(30, '*') + '\n'
    
    for transaction in self.ledger:
      description = transaction['description'][:23]
      amount = str("{:.2f}".format(transaction['amount'])).rjust(30 - len(description), ' ')
      resume += description + amount + '\n'
    
    total = f'Total: {self.get_balance()}'
    resume += total
    
    return resume


def _get_withdraw(total_wihdraw, transaction):
  amount = transaction['amount']
  if amount < 0:
    total_wihdraw += amount * -1
  return total_wihdraw

def create_spend_chart(categories):
    total_spendings = 0
    spendings_by_category = {}

    for category in categories:
      # retrieve only negative values
      total_spending_in_category = reduce(_get_withdraw, category.ledger, 0)
      spendings_by_category[category.category] = total_spending_in_category

      total_spendings += total_spending_in_category

    chart = 'Percentage spent by category\n'

    spendings = spendings_by_category.values()
    percentages = list(
      map(
        lambda value: value * 100 / total_spendings, 
        spendings
      )
    )
  
    for percentage_indicator in range(100, -10, -10):
      indicator = str(percentage_indicator) + '|'
      chart += indicator.rjust(4)

      placeholder = ''
      for percentage in percentages:
        placeholder += 'o' if (percentage_indicator <= percentage) else ' '
      
      chart += ' ' + ('  '.join(list(placeholder))) + '  \n'
    
    indicator_sep = ' ' * 4
    divider =  indicator_sep + (('-' * 3) * len(spendings)) + '-'
    chart += divider + '\n'

    categories_names = spendings_by_category.keys()
    highest_category_name = max(map(len, categories_names))

    names_formatted = list(
        map(
          lambda c: list(c) if len(c) >= highest_category_name else list(c) + ([False] * (highest_category_name - len(c))), 
      categories_names
    ))
  
    for index in range(0, highest_category_name):
      letter_line = ''
      
      for name in names_formatted:
        letter = name[index]
        letter_line += letter or ' '
      
      chart += indicator_sep + ' ' + ('  '.join(list(letter_line))) + '  \n'
  
    return chart[:len(chart)-1]
