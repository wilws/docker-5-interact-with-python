print('---- Wilson \'s Bill Split Calculator  ----')
people_number = int(input('How many people in the meal: '))
price = float(input('How much is the meal ($): '))
tip = float(input('How may tip you would like to give (%): '))
total = price * (1+tip/100)
share =  total / people_number
print(f'Total of the bill is $ {"{:.2f}".format(total)}')
print(f'Each one should pay $ {"{:.2f}".format(share)}')
 