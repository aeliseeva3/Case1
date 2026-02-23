print('a')
def form(number, forms):
    number = abs(number) % 100
    if 11 <= number <= 19:
        return forms[2]
