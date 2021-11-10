import pandas
import random

my_list = [1, 2, 3]

my_list.insert(1, 4)

dict1 = {'car': 1, 'trucks': 2, 'suv': 2}


# print(dict1.values())


def exceed_threshold(value, threshold=0.):
    if value > threshold:
        return True
    else:
        return False


# print(exceed_threshold(2, 10))
# sum
# print(sum([1,2,3]))

# print(exceed_threshold(value=3, threshold=20))


# help(pandas.read_excel)


def add_two_strings_with_separator(first, separator, second):
    """
    Returns the concatenation of the first string and the second string,
    separated by the separator.
    """
    return first + separator + second


yourname = add_two_strings_with_separator('Your', 'Name', ' ')


# print(yourname)


def add_two_strings(first, second, separator=' '):
    """
    Returns the concatenation of the first string and the second string,
    separated by the separator (default=' ').
    """
    return first + separator + second


hername = add_two_strings('Her', 'Name')
# print(hername)
her_name = add_two_strings('her', 'Name', '_')
# print(her_name)

result1 = add_two_strings(first='My', second='Name')
result2 = add_two_strings(second='My', first='Name')
# print(result2)
# print(result1)

apples = 2.69
coffee = 8.99
bread = 2.99
lettuce = 3.19
cheese = 6.89
nontaxable = apples + coffee + bread + lettuce + cheese
# print(nontaxable)

pencils = 3.49
toothpaste = 3.89
shoelaces = 4.99
flowers = 7.99
soap = 1.29
taxable = pencils + toothpaste + shoelaces + flowers + soap
# print(taxable)

tax_rate = .08
new_tax_rate = .09
total_cost = nontaxable + (taxable * new_tax_rate) + taxable
# print(total_cost)


my_list = [1, 3, 5, 7, 9]

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}


def multiply_list_by(alist, multiplier):
    """
    Returns a new list that multiplies each element of alist by the multiplier, so that the new list is the same length as alist, and the n'th element of new_list is equal to multiplier times the n'th element of alist
    """
    new_list = []
    for elem in alist:
        print(elem)
        new_list.append(multiplier * elem)
    return new_list


# print(multiply_list_by(my_list, 10))


def print_keys_and_values(adict):
    """
    Returns a list of strings, where each key and value is converted to a string, and each key-value pair is concatenated.
    NOTE: we use the builtin str() function to convert adict's keys and values to strings.
    """

    new_list = []
    for key, value in adict.items():
        pair = str(key) + str(value)
        new_list.append(pair)
    return new_list


# print(print_keys_and_values(my_dict))

def get_N_random_elements_from_list(alist, N):
    """
    Returns a new list that chooses N elements randomly from alist,
    using the random.choice function, which can choose the same element more than once.
    The resulting list that is returned should have N elements in it.
    """
    counter = 0
    new_list = []
    while counter < N:
        random_element = random.choice(alist)
        new_list.append(random_element)
        counter = counter + random_element
    return new_list


# print(get_N_random_elements_from_list(my_list, 20))

# for elem in [9,2,3,1,2]:
# print(elem)

# for elem in sorted([9,2,3,1,2]):
# print(elem)

# for elem in [9,2,3,1,2]:
#     print(elem)

# counter = 0
# while counter < 10:
#    counter = counter + 2
#    print(counter)

# n = 12
# while n > 0:
#     n = n-1
#     print(n)
#
# my_list = [1,2,3,4]

# def sum_list1(alist):
# total = 0
# for elem in alist:
#     print(elem)
#     total = total + elem
# return total
my_list = [1, 2, 3, 4]


def sum_list2(alist):
    total = 0
    for elem in alist:
        print(elem)
        total = total + elem
    return total


# print(sum_list2(my_list),'2')


def sum_list3(alist):
    total = 0
    for elem in alist:
        print(elem)
    total = total + elem
    return total


# print(sum_list3(my_list),'3')


def sum_list4(alist):
    total = 0
    for elem in alist:
        print(elem)
        total = total + elem
    return total


# print(sum_list4(my_list),'4')

def find_min(a, b):
    """
    Returns the lesser of two inputs a and b
    """
    if a < b:
        return a
    else:
        return b


# print(find_min(1,3))


def test_for_equality(a, b):
    """
    Returns True if a and b are equal, or False otherwise
    """
    if a == b:
        return True
    else:
        return False


# print(test_for_equality(2,3))


def test_for_3or4(a):
    """
    Returns the string "input is equal to 3" if the input a is equal to 3,
    "input is equal to 4" if a is equal to 4, and
    "input is not equal to 3 or 4" if neither case is true
    """

    if a == 3:
        return "input is equal to 3"
    elif a == 4:
        return "input is equal to 4"
    else:
        return "input is not equal to 3 or 4"


# print(test_for_3or4(40))

def add2(x, y):
    """
    Returns the sum of inputs x and y if they can be added,
    and otherwise returns None and prints the statement:
    "Those two inputs cannot be added to each other."
    """
    try:
        result = x + y
        return result
    except TypeError:
        print("Those two inputs cannot be added together")
        return TypeError


#
# print(add2(2,3))
# print(add2('abc','def'))
# print(add2(2,'abc'))

# Examples of iteration
squares = [n ** 2 for n in range(100)]

# The long hand-way
squares = []
for n in range(100):
    squares.append(n ** 2)

squares_even = [n ** 2 for n in range(100) if n % 2 == 0]

squares_and_cubes = [(n ** 2, n ** 3) for n in range(100)]

# for  a dict mapping keys to lists, get lengths of lists
# adict_lengths = [len(v) for v in adict.values()]

#  for a set s1 get intersection with other sets
# s1_isecs = [s1.intersection(s) for s in [s2,s3,s4]]

# inverter keys and values ,assuming values are unique and valid as keys
# invertered_adict = [v:k fro k,v in adict.items()]

# make a Cesar cipher for coded messages
letters = 'abcdefghijklmnopqrstuvwxyz'

cesar_cipher = {letters[i]: letters[i-3] % len(letters) for i in range(len(letters))}



my_evens2 = [n for n in my_list if n % 2 == 0]
# print(my_evens2)
s = '1,abc,33'
a = s.replace('1,abc,33', 'Listo')
print(a)
str_digits2 = [s for s in s if s.isdigit()]
print(str_digits2)

# s = list(cars)


def convert(set):
    return sorted(set)

cars = {'bmw', 'ferrari', 'maserati'}
s = set(cars)
# print(convert(s))


def make_dict_of_squares(n):
    """
    Returns a dictionary that maps from integers to their squares,
    starting with 0 and ending at one less than the input n
    """
    result = {}
    for i in range(n):
        result[i] = i*i
    return result

squares = make_dict_of_squares(10)
# print(squares)

squares2 ={key for key in range(n)}
# print(squares2)

apple = {n: n-1 for n in range(0,10)}
print(apple)

juice = [i for i in range(10) if True]
print(juice)


dog = [j for j in range(1,51,2) if j%2==0]
print(dog)