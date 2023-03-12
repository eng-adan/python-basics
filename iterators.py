# for loop with array

print('for Loop on array/list')
for iterator in [1,2,3,4,5]:
    print(iterator)

# for loop with sting
print('for Loop on string')
for iterator in 'string':
    print(iterator)

# for loop with integer
print('Loop on range of integers')
for iterator in range(3,5):
    print(iterator)

# for loop with dictionary
print('Loop on dict')
dict = {'a': 1, 'b': 2}
for iterator in dict:
    print(dict[iterator])


# there is also a method for iteration of array
# that keyword is know as iter() and to get value
# we need to use next() method to call it
print('Iter method')
arr = [1,2,4,6,2]
my_iter = iter(arr)

print(next(my_iter)) # print first element i.e., 1
print(next(my_iter)) # print second element i.e., 2 and so on...


# the best way to use iter mehtod is while loop
print('Iter method with while loop')
arr = [1,2,4,6,2]
my_iter = iter(arr)
while True:
    try:
        print(next(my_iter))
    except StopIteration:
        break
