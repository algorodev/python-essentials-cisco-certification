## The result of the input() function

We've said it already, but it must be unambiguously stated once again: **the result of the** ```input()``` **function is a string**.

A string containing all the characters the user enters from the keyboard. It is not an integer or a float.

This means that **you mustn't use it as an argument of any arithmetic operation**, e.g., you can't use this data to square it, divide it by anything, or divide anything by it.

### Prohibited operations

```
anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
```

We are trying to apply the ```**``` operator to ```str``` (string) accompanied with ```float```.

This is prohibited.

This should be obvious - can you predict the value of ```to be or not to be``` raised to the power of ```2```?

We can't. Python can't, either.
