def make_pizza(size, *toppings):
    """
    Create a function called make_pizza that takes two arguments: size and toppings.
    The function should return a string that describes a pizza with the given size and toppings.
    """
    print(f'\nMaking a {size} pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')
