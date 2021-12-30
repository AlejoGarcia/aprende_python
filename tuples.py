# List example
#prime_numbers = [2, 3, 5, 7, 11, 13, 17]

# Tuple example
#perfect_squares = (1, 4, 9, 16, 25, 36)

#print("List methods")
#print(dir(prime_numbers))
#print(80*"-")
#print("Tuple methods")
#print(dir(perfect_squares))
#
import sys

list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)

print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))

