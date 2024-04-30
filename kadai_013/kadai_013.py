def total(price, rate):
  tax = price*(rate*0.01)
  return tax+price

after_tax = total(480, 10)
print(after_tax)