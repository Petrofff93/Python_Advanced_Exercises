from collections import deque


def shopping_cart(*args):
    meals = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }

    meals_length = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
    }
    args = deque(args)

    while args:
        current_couple = args.popleft()
        if current_couple == 'Stop':
            if len(meals["Soup"]) == 0 and len(meals["Pizza"]) == 0 and len(meals["Dessert"]) == 0:
                return 'No products in the cart!'
            result = ''
            meals = dict(sorted(meals.items(), key=lambda x: (-len(x[1]), x[0])))
            for key, value in meals.items():
                result += f"{key}:\n"
                for item in sorted(value):
                    result += f" - {item}\n"
            return result.strip()

        meal, product = current_couple

        if product not in meals[meal] and len(meals[meal]) < meals_length[meal]:
            meals[meal].append(product)


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

