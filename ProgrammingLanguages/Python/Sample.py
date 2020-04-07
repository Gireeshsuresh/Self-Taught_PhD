# /**
#  * @author  [Gireesh Suresh]
#  * @email   [gireesh.star@gmail.com]
#  * @create  date 2020-04-06 18:51:33
#  * @modify  date 2020-04-06 18:51:33
#  * @desc    [Rough work]
#  */

testSting = "Hello World"
print(testSting)

spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

type(19.95)  # float

print(min(1, 2, 3))
print(max(1, 2, 3))

print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)

print(5//2)     # Returns the Quotient

print(5 % 2)    # Returns the Remainder


def least_difference(a, b, c):
    """Return the smallest difference between any two numbers       # Docstrings
    among a, b and c.

    >>> least_difference(1, 5, -5)
    4
    """
    return min(abs(a - b), abs(b-c), abs(a - c))

print("Least Difference = %.3f"  %least_difference(1,10,100))       # Python - 2
print("Least Difference = {}"  .format(least_difference(1,10,100))) # Python - 2

print("Least Difference = ", least_difference(1,10,100))            # Python - 3

# help(least_difference)
# least_difference(a, b, c)
#     Return the smallest difference between any two numbers
#     among a, b and c.
    
#     >>> least_difference(1, 5, -5)
#     4

print(1, 2, 3, sep=' < ')                                            # Python - 3
