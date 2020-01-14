'''
Alessia Pizzoccheri
Wholesale

Test Case #1
    3 books: wholesale $44.91, shipping $4.50, total cost $49.41

Test Case #2
    12 books: wholesale $179.64, shipping $11.25, total cost $190.89

Test Case #3
    257 book: wholesale $3847.29, shipping $195.00, total cost $4042.29
'''

def main():

    # variables needed to calculate final cost
    price = 24.95
    discount = .40
    shipping = 3
    additional_shipping = .75

    # total number of books
    books = int(input('How books are you ordering? '))

    wholesale = (price * books) * (1 - discount)

    # calculate shipping
    shipping_cost = shipping + ((books - 1) * .75)
    total_cost = wholesale + shipping_cost

    print('The wholesale cost is ${:.2f}'.format(wholesale))
    print('The shipping cost is ${:.2f}'.format(shipping_cost))
    print('The total cost is ${:.2f}'.format(total_cost))


main()
