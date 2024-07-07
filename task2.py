import random


def get_numbers_ticket(min: int, max: int, quantity: int):
    try:
        if min < 1:
            raise ValueError(f"Minimum number '{min}' is less than 1.")
        if max >= 1000:
            raise ValueError(f"Maximum number '{max}' is greater than 1000.")
        if min > max:
            raise ValueError(f"Minimum number '{min}' is greater than maximum number '{max}'.")
        if quantity <= 0:
            raise ValueError(f"Quantity '{quantity}' is less than or equal to zero.")
        if quantity > (max - min + 1):
            raise ValueError(f"Quantity '{quantity}' is greater than the range of numbers between {min} and {max}.")

        # Generate random numbers:
        random_numbers = random.sample(range(min, max + 1), quantity)
        random_numbers.sort()

        return print(f"Randomly generated numbers between {min} and {max} are: {random_numbers}")
    except ValueError as e:
        print(e)
        # Retry block:
        try_again = input("Do you want to try again? (Y/N): ")
        if try_again.lower() == 'y':
            new_min = int(input("Enter a minimum number: "))
            new_max = int(input("Enter a maximum number: "))
            new_quantity = int(input("Enter a quantity of numbers to generate: "))
            return get_numbers_ticket(new_min, new_max, new_quantity)
        else:
            return "Goodbye!"


min = int(input("Enter a minimum number: "))
max = int(input("Enter a maximum number: "))
quantity = int(input("Enter a quantity of numbers to generate: "))

get_numbers_ticket(min, max, quantity)
