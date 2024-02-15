## Basic operators

An operator is a symbol of the programming language, which is able to operate on the values.

For example, just as in arithmetic, the ```+``` (plus) sign is the operator which is able to **add** two numbers, giving the result of the addition.

Not all Python operators are as obvious as the plus sign, though, so let's go through some of the operators available in Python, and we'll explain which rules govern their use, and how to interpret the operations they perform.

We'll begin with the operators which are associated with the most widely recognizable arithmetic operations:

```
+
-
*
/
//
%
**
```
The order of their appearance is not accidental. We'll talk more about it once we've gone through them all.

**Remember**: Data and operators when connected together form **expressions**. The simplest expression is a literal itself.

### Exponentiation

Note: we've surrounded the double asterisks with spaces in our examples. It's not compulsory, but it improves the **readability** of the code.

The examples show a very important feature of virtually all Python **numerical operators**.

Run the code and look carefully at the results it produces. Can you see any regularity here?

**Remember**: It's possible to formulate the following rules based on this result:

- when **both** ```**``` arguments are integers, the result is an integer, too;
- when **at least one** ```**``` argument is a float, the result is a float, too.

### Multiplication

An ```*``` (asterisk) sign is a **multiplication** operator.

### Division

A ```/``` (slash) sign is a **division** operator.

The value in front of the slash is a **dividend**, the value behind the slash, a **divisor**.

You should see that there is an exception to the rule.

**The result produced by the division operator is always a float**, regardless of whether or not the result seems to be a float at first glance: ```1 / 2```, or if it looks like a pure integer: ```2 / 1```.

Is this a problem? Yes, it is. It happens sometimes that you really need a division that provides an integer value, not a float.

Fortunately, Python can help you with that.

### Integer division (floor division)

A ```//``` (double slash) sign is an **integer division** operator. It differs from the standard ```/``` operator in two details:

- its result lacks the fractional part ‒ it's absent (for integers), or is always equal to zero (for floats); this means that **the results are always rounded**;
- it conforms to the _integer vs. float rule_.

The result of integer division is always rounded to the nearest integer value that is less than the real (not rounded) result.

This is very important: **rounding always goes to the lesser integer**.

### Remainder (modulo)

The next operator is quite a peculiar one, because it has no equivalent among traditional arithmetic operators.

Its graphical representation in Python is the ```%``` (percent) sign, which may look a bit confusing.

Try to think of it as a slash (division operator) accompanied by two funny little circles.

The result of the operator is a **remainder left after the integer division**.

In other words, it's the value left over after dividing one value by another to produce an integer quotient.

Note: the operator is sometimes called **modulo** in other programming languages.

### How not to divide

As you probably know, **division by zero doesn't work**.

Do **not** try to:

- perform a division by zero;
- perform an integer division by zero;
- find a remainder of a division by zero.

### Addition

The **addition** operator is the ```+``` (plus) sign, which is fully in line with mathematical standards.

### The subtraction operator, unary and binary operators

The **subtraction** operator is obviously the ```-``` (minus) sign, although you should note that this operator also has another meaning ‒ **it can change the sign of a number**.

This is a great opportunity to present a very important distinction between **unary** and **binary** operators.

In subtracting applications, the **minus operator expects two arguments**: the left (a **minuend** in arithmetical terms) and right (a **subtrahend**).

For this reason, the subtraction operator is considered to be one of the binary operators, just like the addition, multiplication and division operators.

But the minus operator may be used in a different (unary) way.

By the way: there is also a unary ```+``` operator.

The operator preserves the sign of its only argument – the right one.

Although such a construction is syntactically correct, using it doesn't make much sense, and it would be hard to find a good rationale for doing so.
