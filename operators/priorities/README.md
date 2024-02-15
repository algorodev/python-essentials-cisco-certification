## Operators and their priorities

So far, we've treated each operator as if it had no connection with the others. Obviously, such an ideal and simple
situation is a rarity in real programming.

Also, you will very often find more than one operator in one expression, and then things are no longer so simple.

Consider the following expression:

```
2 + 3 * 5
```

You probably remember from school that **multiplications** precede **additions**.

You surely remember that you should first multiply 3 by 5 and, keeping the 15 in your memory, then add it to 2, thus
getting the result of 17.

The phenomenon that causes some operators to act before others is known as **the hierarchy of priorities**.

Python precisely defines the priorities of all operators, and assumes that operators of a higher priority perform their
operations before the operators of a lower priority.

So, if you know that ```*``` has a higher priority than ```+```, the computation of the final result should be obvious.

### Operators and their bindings

The **binding** of the operator determines the order of computations performed by some operators with equal priority,
put side by side in one expression.

Most of Python's operators have left-sided binding, which means that the calculation of the expression is conducted from
left to right.

This simple example will show you how it works. Take a look:

```
print(9 % 6 % 2)
```

There are two possible ways of evaluating this expression:

from left to right: first ```9 % 6``` gives ```3```, and then ```3 % 2``` gives ```1```;
from right to left: first ```6 % 2``` gives ```0```, and then ```9 % 0``` causes **a fatal error**.

### List of priorities

Since you're new to Python operators, we don't want to present the complete list of operator priorities right now.

Instead, we'll show you a truncated form, and we'll expand it consistently as we introduce new operators.

Look at the table below:

| Priority |                                                   Operator                                                   |        |
|----------|:------------------------------------------------------------------------------------------------------------:|:------:|
| 1        |                                                   ```**```                                                   |        |
| 2        | ```*+```, ```-``` (note: unary operators located next to the right of the power operator bind more strongly) | unary  |
| 3        |                                     ```*```, ```/```, ```//```, ```%```                                      |        |
| 4        |                                               ```+```, ```-```                                               | binary |

Note: we've enumerated the operators in order **from the highest (1) to the lowest (4) priorities**.

### Operators and parentheses

Of course, you're always allowed to use **parentheses**, which can change the natural order of a calculation.

In accordance with the arithmetic rules, **subexpressions in parentheses are always calculated first**.

You can use as many parentheses as you need, and they're often used to **improve the readability** of an expression, even if they don't change the order of the operations.
