## Integers

You may already know a little about how computers perform calculations on numbers. Perhaps you've heard of the **binary system**, and know that it's the system computers use for storing numbers, and that those computers can perform any operation upon them.

We won't explore the intricacies of positional numeric systems here, but we will say that the numbers handled by modern computers are of two types:

- **integers**, that is, those which are devoid of the fractional part;
- and **floating-point** numbers (or simply **floats**), that contain (or are able to contain) the fractional part.

This definition is not entirely accurate, but quite sufficient for now. The distinction is very important, and the boundary between these two types of numbers is very strict. Both of these kinds of numbers differ significantly in how they're stored in a computer memory and in the range of acceptable values.

The characteristic of the numeric value which determines its kind, range, and application, is called the **type**.

If you encode a literal and place it inside Python code, the form of the literal determines the representation (type) Python will use to **store it in the memory**.

Consider the question of how Python recognizes integers.

The process is almost like how you would write them with a pencil on paper - it's simply a string of digits that make up the number. But there's a reservation ‒ you must not interject any characters that are not digits inside the number.

Take, for example, the number _eleven million one hundred eleven thousand one hundred eleven_. If you took a pencil in your hand right now, you would write the number like this: ```11,111,111```, or like this: ```11.111.111```, or even like this: ```11 111 111```.

It's clear that this provision makes it easier to read, especially when the number consists of many digits. However, Python doesn't accept things like these. It's **prohibited**. What Python does allow, though, is the use of **underscores** in numeric literals.*

Therefore, you can write this number either like this: ```11111111```, or like this: ```11_111_111```.

And how do we code negative numbers in Python? As usual ‒ by adding a **minus**. You can write: ```-11111111```, or ```-11_111_111```.

Positive numbers do not need to be preceded by the plus sign, but it's permissible, if you wish to do it. The following lines describe the same number: ```+11111111``` and ```11111111```.

### Octal and hexadecimal numbers

There are two additional conventions in Python that are unknown to the world of mathematics. The first allows us to use numbers in an **octal** representation.

If an integer number is preceded by an ```0O``` or ```0o``` prefix (zero-o), it will be treated as an octal value. This means that the number must contain digits taken from the [0..7] range only.

```0o123``` is an octal number with a (decimal) value equal to ```83```.

The second convention allows us to use **hexadecimal** numbers. Such numbers should be preceded by the prefix ```0x``` or ```0X``` (zero-x).

```0x123``` is a hexadecimal number with a (decimal) value equal to ```291```.
