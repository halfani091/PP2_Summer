"""
Function Arguments Examples
Demonstrates positional arguments, keyword arguments, and default values.
"""


# Example 1: Positional arguments - order matters
def introduce(first_name, last_name):
    """Introduces a person using positional arguments."""
    print(f"This is {first_name} {last_name}.")


introduce("John", "Smith")  # first_name="John", last_name="Smith"


# Example 2: Keyword arguments - order does not matter
def order_food(item, quantity):
    """Places a food order using keyword arguments."""
    print(f"Order: {quantity} x {item}")


order_food(quantity=3, item="Burger")  # works fine, order doesn't matter here


# Example 3: Default argument values
def make_coffee(size="medium", sugar=True):
    """Makes coffee with optional size and sugar parameters."""
    sugar_text = "with sugar" if sugar else "without sugar"
    print(f"Making a {size} coffee {sugar_text}.")


make_coffee()                  # uses both defaults
make_coffee("large")           # overrides size only
make_coffee(sugar=False)       # overrides sugar only


# Example 4: Mixing required and default arguments together
def book_ticket(destination, passengers=1, seat_class="economy"):
    """Books a ticket with one required and two optional arguments."""
    print(f"Booking {passengers} ticket(s) to {destination} in {seat_class} class.")


book_ticket("Almaty")
book_ticket("Astana", 2)
book_ticket("Paris", 4, "business")
