## Lists

### Why do we need lists?

It may happen that you have to read, store, process, and finally, print dozens, maybe hundreds, perhaps even thousands of numbers. What then? Do you need to create a separate variable for each value? Will you have to spend long hours writing statements like the one below?

```
var1 = int(input())
var2 = int(input())
var3 = int(input())
var4 = int(input())
var5 = int(input())
var6 = int(input())
:
:
```

So far, you've learned how to declare variables that are able to store exactly one given value at a time. Such variables are sometimes called **scalars** by analogy with mathematics. All the variables you've used so far are actually scalars.

Think of how convenient it would be to declare a variable that could store more than one value. For example, a hundred, or a thousand or even ten thousand. It would still be one and the same variable, but very wide and capacious. Sounds appealing? Perhaps, but how would it handle such a container full of different values? How would it choose just the one you need?

What if you could just number them? And then say: _give me the value number 2; assign the value number 15; increase the value number 10000._

We'll show you how to declare such **multi-value variables**. We'll do this with the example we just suggested. We'll write a **program that sorts a sequence of numbers**. We won't be particularly ambitious ‒ we'll assume that there are exactly five numbers.

Let's create a variable called `numbers`; it's assigned with not just one number, but is filled with a list consisting of five values (note: the **list starts with an open square bracket and ends with a closed square bracket**; the space between the brackets is filled with five numbers separated by commas).

```
numbers = [1, 2, 3, 4, 5]
```

Let's say the same thing using adequate terminology: numbers **is a list consisting of five values**, all of them numbers. We can also say that this statement creates a list of length equal to five (as in there are five elements inside it).

The elements inside a list **may have different types**. Some of them may be integers, others floats, and yet others may be lists.

Python has adopted a convention stating that the elements in a list are **always numbered starting from zero**. This means that the item stored at the beginning of the list will have the number zero. Since there are five elements in our list, the last of them is assigned the number four. Don't forget this.

### Indexing lists

How do you change the value of a chosen element in the list?

Let's **assign a new value of** `111` **to the first element** in the list.

```
numbers[0] = 111
```

And now we want **the value of the fifth element to be copied to the second element**.

```
numbers[1] = numbers[4]
```

The value inside the brackets which selects one element of the list is called an **index**, while the operation of selecting an element from the list is known as **indexing**.

Note: all the indices used so far are literals. Their values are fixed at runtime, but **any expression can be the index**, too. This opens up lots of possibilities.

### Accessing list content

Each of the list's elements may be accessed separately. Or the list may also be printed as a whole.

```
print(numbers[0])
print(numbers)
```

### The _len()_ function

The **length of a list** may vary during execution. New elements may be added to the list, while others may be removed from it. This means that the list is a very dynamic entity.

If you want to check the list's current length, you can use a function named `len()` (its name comes from _length_).

The function takes the **list's name as an argument, and returns the number of elements currently stored** inside the list (in other words ‒ the list's length).

```
print(len(numbers))
```

### Removing elements from a list

Any of the list's elements may be **removed** at any time ‒ this is done with an instruction named `del` (delete). Note: it's an **instruction**, not a function.

You have to point to the element to be removed ‒ it'll vanish from the list, and the list's length will be reduced by one.

**You can't access an element which doesn't exist** ‒ you can neither get its value nor assign it a value.

```
del numbers[1]
print(len(numbers))
print(numbers)
```

### Negative indices are legal

It may look strange, but negative indices are legal, and can be very useful.

An element with an index equal to `-1` is **the last one in the list**.

```
print(numbers[-1])
```

Similarly, the element with an index equal to `-2` is **the one before last in the list**.

```
print(numbers[-2])
```

### Adding elements to a list: append() and insert()

Such an operation is performed by a method named `append()`. It takes its argument's value and puts it **at the end of the list** which owns the method.

The list's length then increases by one.

```
value = 6
numbers.append(value)
```

The `insert()` method is a bit smarter ‒ it can add a new element **at any place in the list**, not only at the end.

```
value = 6
location = 3
numbers.insert(location, value)
```

It takes two arguments:

- the first shows the required location of the element to be inserted; note: all the existing elements that occupy locations to the right of the new element (including the one at the indicated position) are shifted to the right, in order to make space for the new element;
- the second is the element to be inserted.

You can **start a list's life by making it empty** (this is done with an empty pair of square brackets) and then adding new elements to it as needed.

### Sorting a list

Now that you can effectively juggle the elements of lists, it's time to learn how to **sort** them. Many sorting algorithms have been invented so far, which differ a lot in speed, as well as in complexity. We are going to show you a very simple algorithm, easy to understand, but unfortunately not too efficient, either. It's used very rarely, and certainly not for large and extensive lists.

Let's say that a list can be sorted in two ways:

- increasing (or more precisely ‒ non-decreasing) ‒ if in every pair of adjacent elements, the former element is not greater than the latter;
- decreasing (or more precisely ‒ non-increasing) ‒ if in every pair of adjacent elements, the former element is not less than the latter.

Python lists have a method called `sort()` that **modifies the list in-place**.

```
# ASC Sort
numbers.sort()
print(numbers)
```

```
# DESC Sort
numbers.sort(reverse=True)
print(numbers)
```

There is also a list method called `reverse()`, which you can use to **reverse the list**.

```
numbers.reverse()
print(numbers)
```

### The _slice_ operator

A **slice** is an element of Python syntax that allows you to **make a brand-new copy of a list, or parts of a list**.

It actually copies the list's contents, not the list's name.

```
numbers2 = numbers[:]
print(numbers2)
```

This inconspicuous part of the code described as `[:]` is able to produce a brand new list.

A slice of this form **makes a new (target) list, taking elements from the source list ‒ the elements of the indices from** `start` **to** `end - 1`.

```
list_name[start:end]
```

- `start` is the index of the first element **included in the slice**;
- `end` is the index of the first element **not included in the slice**.

Note: not to `end` but to `end - 1`. An element with an index equal to `end` is the first element which **does not take part in the slicing**.

Using negative values for both start and end is possible (just like in indexing).

```
numbers3 = numbers[2:4]
print(numbers3)
```

This is how negative indices work with the slice:

```
numbers4 = numbers[1:-1]
print(numbers4)
```

If the `start` specifies an element lying further than the one described by the `end` (from the list's beginning), the slice will be **empty**.

If you omit the `start` in your slice, it is assumed that you want to get a slice beginning at the element with index `0`.

Similarly, if you omit the `end` in your slice, it is assumed that you want the slice to end at the element with the index `len`.

As we've said before, omitting both `start` and `end` makes a **copy of the whole list**.

The previously described `del` instruction is able to **delete more than just a list's elements at once ‒ it can delete slices too**.

Note: in this case, the slice **doesn't produce any new list**!

```
del numbers4[2:3]
print(numbers4)
```

Deleting **all the elements** at once is possible too.

```
del numbers3[:]
print(numbers3)
```

### The _in_ and _not_ in operators

Python offers two very powerful operators, able to **look through the list in order to check whether a specific value is stored inside the list or not**.

These operators are:

```
element in list_name
element not in list_name
```

The first of them (`in`) checks if a given element (its left argument) is currently stored somewhere inside the list (the right argument) ‒ the operator returns `True` in this case.

```
print(5 in numbers)
```

The second (`not in`) checks if a given element (its left argument) is absent in a list ‒ the operator returns `True` in this case.
```
print(5 not in numbers)
```
