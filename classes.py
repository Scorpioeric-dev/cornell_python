class Pizza:
    """Class to Construct pizza pies"""
    def __init__(self, size, toppings=None):
        """Build a pizza of a certain size and toppings"""
        self.size = size
        self.toppings = set()
        if toppings is not None:
            for toppings in toppings:
                self.toppings.add(toppings)

    def price(self):
        """Calculate the price base on size and toppings"""
        base_prize = {'small': 10.0, 'medium': 12.0, 'large': 14.0}
        p = base_prize[self.size]
        for topping in self.toppings:
            p += 0.50
        return p


my_pizza = Pizza('large', {'Garlic', 'Pepperoni'})
your_pizza = Pizza('small', {'Pineapple', 'Pepperoni'})
# print(your_pizza.price())

# Cornell exercise


class ShiftCipher:
    """
    ShiftCipher objects that can encrypt and decode text messages based on a specific shift length.
    """

    def __init__(self, shift):
        """
        Constructs a ShiftCipher for the specified degree of shift (positive or negative),
        by building a cipher (dictionary mapping from letters to other letters), and
        a decoder (the inverse of the cipher)
        """
        self.shift = shift
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        self.cipher = {self.letters[i]: self.letters[self.shift % len(self.letters)] for i in range(len(self.letters))}
        self.decoder = {self.letters[i]: self.letters[self.shift % len(self.letters)] for i in range(len(self.letters))}


c0 = ShiftCipher(0)
print(c0.cipher)
m3 = ShiftCipher(-3)
print(m3.cipher)
p13 = ShiftCipher(13)
print(p13.cipher)

