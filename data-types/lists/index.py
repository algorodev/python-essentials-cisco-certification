numbers = [1, 2, 3, 4, 5]
print("Original list contents:", numbers)

numbers[0] = 111
print("New list contents: ", numbers)

numbers[1] = numbers[4]
print("New list contents:", numbers)

print("First element on the list:", numbers[0])

print("List length:", len(numbers))

del numbers[1]
print("New list's length:", len(numbers))
print("New list content:", numbers)

print("Last element on the list:", numbers[-1])

value = 6
numbers.append(value)
print("New list contents:", numbers)
print("New list's length:", len(numbers))

value = 4
location = 3
numbers.insert(location, value)
print("New list contents:", numbers)
print("New list's length:", len(numbers))

numbers.sort()
print("List sorted by ASC", numbers)

numbers.sort(reverse=True)
print("List sorted by DESC", numbers)

numbers.reverse()
print("List reversed", numbers)

numbers2 = numbers[:]
print("New list created of numbers list", numbers2)

numbers3 = numbers[2:4]
print("New list created of a part of our initial numbers list", numbers3)

numbers4 = numbers[1:-1]
print("New list created using negative index on slice", numbers4)

del numbers4[2:3]
print("New 4 list contents:", numbers4)

del numbers3[:]
print("New 3 list contents:", numbers3)

print("Is there a 5 in my list?", 5 in numbers)
print("Is there not a 5 in my list?", 5 not in numbers)
