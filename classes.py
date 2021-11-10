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


print(Pizza)
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
        self.cipher = {self.letters[i]: self.letters[(i + self.shift) % len(self.letters)] for i in
                       range(len(self.letters))}
        self.decoder = {self.letters[i]: self.letters[(i - self.shift) % len(self.letters)] for i in
                        range(len(self.letters))}

    def transform_message(self, message, cipher):
        """
        Transforms a message using the specified cipher.  Is not called by users directly,
        and can be called with either the cipher (to encrypt) or the decoder (to decode).
        """
        tmsg = ''
        for c in message:
            tmsg = tmsg + cipher.get(c, c)
        return tmsg

    def encrypt(self, message):
        """
        Transforms a message using the cipher, by calling self.transform_message
        """
        return self.transform_message(message,self.cipher)

    def decode(self, message):
        """
        Transforms a message using the decoder, by calling self.transform_message
        """
        return self.transform_message(message,self.decoder)


test = "I come to bury Caesar, not to praise him."
move3 = ShiftCipher(-3)
#  Shift -3 Cipher
print(move3.encrypt(test))
# Shift 13 Cipher
print(move3.decode(move3.encrypt(test)))
move13 = ShiftCipher(13)
print(move13.encrypt(test))

c0 = ShiftCipher(0)
# print(c0.cipher)
m3 = ShiftCipher(-3)
# print(m3.cipher)
p13 = ShiftCipher(13)
# print(p13.cipher)


