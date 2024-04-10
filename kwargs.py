
def order_pizza(name, address, **toppings):
    print(f'Order is for {name}')
    print(f'Ship it to {address}')
    price = 18
    for key in toppings.items():
        price +=2
    print(f'The price is {price}')
    return price

order_pizza('Arik', 'Israel', Bulgarit = True, extra_cheese=True, mashrooms = True)