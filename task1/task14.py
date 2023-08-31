def credit_card(number):
    digits = [int(d) for d in str(number)][::-1]
    multiplied_digits = [(d * 2 if i % 2 == 1 else d) for i, d in enumerate(digits)]
    total = sum([(d % 10) + (d // 10) for d in multiplied_digits])

    if total % 10 == 0:
        if str(number).startswith(('34', '37')):
            return 'American Express'
        elif str(number).startswith(('51', '52', '53', '54', '55')):
            return 'MasterCard'
        elif str(number).startswith('4'):
            return 'Visa'
        else:
            return 'Valid (Unknown Card Type)'
    else:
        return 'Invalid'


number = input("Enter the credit card number: ")
print(credit_card(number))





