# Program to count the number of bits that are set to 1 in a positive integer.

def count_bits(x):
  num_bits = 0
  while x:
    num_bits += x & 1 # Checks the least significant bit is 1.
    x >>= 2 # In some ways this pushes the least significant bit out of the number and is equivalent to x mod 2
  return num_bits


x = count_bits(9)
print(f'\nThe Total Num of Bits = {x}')