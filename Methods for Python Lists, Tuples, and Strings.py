my_list = [3,1,7,-3,2,-4,5,1,2,2,3,3,2,9,0,2,2,2,3,3,3,3]
# print(my_list.count(3))

a = [1,2,3]
b = [4,5,6]
a.append(b)
# print(a)

c = [1,2,3]
d = [4,5,6]
c.extend(d)
# print(d)
#
# print(my_list.index(2))
# print(my_list.index(2,5))

# Methods for dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# print(dict1.keys())
dict2 = {'c': 10, 'd': 20, 'e': 30, 'f': 40, 'g': 50}
# print(dict2.keys())
dict1 = set(dict1)
dict2 = set(dict2)


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dict1.get('e', None))


def sum_and_difference(x,y):
    return x+y,x-y


xysum, xydiff = sum_and_difference(200,10)
# print(xysum)
# print(xydiff)
dict2 = {'a': 1, 'b': 2, 'c': 2}

for k, v in dict2.items():
    # print(k,v)

# coauthors = {}
#
# coauthors[['Author1','Authur2']] = 2
# # immutable
# coauthors[('Author1','Authur2')] = 2

    date = (2019, 4, 7)
# print(date[2])


def product_and_ratio(x, y):
    return x*y,x/y


# print(product_and_ratio(10,20))


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

cipher = {letters[i]: letters[(i-3) % len(letters)] for i in range(len(letters))}
decoder = {letters[i]: letters[(i+3) % len(letters)] for i in range(len(letters))}


def transform_message(message, decoder):
    tmsg = ''
    for c in message:
        tmsg = tmsg + decoder.get(c,c)
    return tmsg


test = "A Journey of a 1000 miles begins with one foot step."
# print(str(test))
# print(test)
# print(cipher)
ttest = transform_message(test,cipher)
print(ttest)
print(transform_message(ttest,decoder))


