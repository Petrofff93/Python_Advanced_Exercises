def shopping_list(leva, **kwargs):
    budget = int(leva)

    if budget < 100:
        return 'You do not have enough budget.'

    result = ''
    basket = 0

    while True:
        for key, value in kwargs.items():
            price, qty = float(value[0]), int(value[1])
            if basket == 5:
                break

            current_price = price * qty

            if budget >= current_price:
                basket += 1
                budget -= current_price
                result += f"You bought {key} for {current_price:.2f} leva.\n"
        break
    return result


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
