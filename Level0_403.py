# Print exercise
print("V")
print("i")
print("v")
print("i")
print("a")
print("n")

# Operation exercises 
print(int(5/2))
print(5.0 / 2.0)
print(10 % 3)
print(5 ** 2)
print (5 // 2)
print(10 - 3 + (1 * 9))


# Boolean exercises 
print(1 == 1.0)
print("1" == "1.0")
print (5 == (3 + 2))
print(1 == 1.0 and not "1" == "1.0" and 5 == (3+2))
print(1 == 1.0 or "1" == "1.0" and 5 == (3+2))
print(1 == 1.0 and "1" == "1.0" or 5 == (3+2))
print(1 == 1.0 or "1" == "1.0" or 5 == (3+2))
print(1 == 1.0 and not "1" == "1.0" or 5 == (3+2))

# List exercises
oddlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(oddlist)
print(len(oddlist))
print(type(oddlist))
intlist = list(range(101))
print(intlist)

# Dictionary exercises
import pprint
about_me = {
'name': 'Vivian',
'age': 22.0,
'year': 2022,
'favourite foods': ['sourdough, pasta, chicken shwarma'],
}
print(about_me)
pprint.pprint(about_me)
print(type(about_me))
print(len(about_me))

# Array excercises
import numpy as np

mixnums = np.array([1, 2, 3, 4.0, 5.0, 6.0])
print(mixnums)
mixtypes = np.array([7, 8, 9.0, 10.0, '11', '12'])
print(mixtypes)
oddarray = np.arange(1, 100, 2)
print(oddarray)
logarray = np.logspace(1,5, 16)
print(logarray)