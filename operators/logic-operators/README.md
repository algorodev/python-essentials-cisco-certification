## Logic operators

### The _and_ operator

One logical conjunction operator is `and`. It's a **binary operator with a priority that is lower than the one expressed
by the comparison operators**.

```
counter > 0 and value === 100
```

The result provided by the `and` operator can be determined on the basis of the **truth table**.

| Argument `A` | Argument `B` | `A and B` |
|--------------|:------------:|:---------:|
| `False`      |   `False`    |  `False`  |
| `False`      |    `True`    |  `False`  |
| `True`       |   `False`    |  `False`  |
| `True`       |    `True`    |  `True`   |

### The _or_ operator

A disjunction operator is the word `or`. It's a **binary operator with a lower priority than** `and` (just like `+`
compared to `*`).

| Argument `A` | Argument `B` | `A and B` |
|--------------|:------------:|:---------:|
| `False`      |   `False`    |  `False`  |
| `False`      |    `True`    |  `True`   |
| `True`       |   `False`    |  `True`   |
| `True`       |    `True`    |  `True`   |

### The _not_ operator

Another logical conjunction operator is `not`. It's a **unary operator performing a logical negation**. This operator is
written as the word `not`, and its **priority is very high: the same as the unary** `+` **and** `-`.

| Argument | `not` Argument |
|:--------:|:--------------:|
| `False`  |     `True`     |
|  `True`  |    `False`     |

### Logical values vs. single bits

Logical operators take their arguments as a whole regardless of how many bits they contain. The operators are aware only
of the value: zero (when all the bits are reset) means `False`; not zero (when at least one bit is set) means `True`.

The result of their operations is one of these values: `False` or `True`. This means that this snippet will assign the
value `True` to the `j` variable if `i` is not zero; otherwise, it will be `False`.

```
i = 1
j = not not i
```

### Bitwise operators

There are four operators that allow you to **manipulate single bits of data**. They are called **bitwise operators**.

They cover all the operations we mentioned before in the logical context, and one additional operator. This is
the `xor` (as in **exclusive or**) operator, and is denoted as `^` (caret).

Here are all of them:

- `&` (ampersand) ‒ bitwise conjunction;
- `|` (bar) ‒ bitwise disjunction;
- `~` (tilde) ‒ bitwise negation;
- `^` (caret) ‒ bitwise exclusive or (xor).

Bitwise operations (`&`, `|` and `^`)

| Argument `A` | Argument `B` | `A ampersand B` | `A bar B` | `A caret B` |
|--------------|:------------:|:---------------:|:---------:|-------------|
| `0`          |     `0`      |       `0`       |    `0`    | `0`         |
| `0`          |     `1`      |       `0`       |    `1`    | `1`         |
| `1`          |     `0`      |       `0`       |    `1`    | `1`         |
| `1`          |     `1`      |       `1`       |    `1`    | `0`         |

Bitwise operations (`~`)

| Argument | `tilde` Argument |
|----------|:----------------:|
| `0`      |       `1`        |
| `1`      |       `0`        |

Let's make it easier:

- `&` requires exactly two `1`s to provide `1` as the result;
- `|` requires at least one `1` to provide `1` as the result;
- `^` requires exactly one `1` to provide `1` as the result.

Let us add an important remark: the arguments of these operators **must be integers**; we must not use floats here.

The difference in the operation of the logical and bit operators is important: **the logical operators do not penetrate into the bit level of its argument**. They're only interested in the final integer value.

Bitwise operators are stricter: they deal with **every bit separately**.

### Binary left shift and binary right shift

Python offers yet another operation relating to single bits: **shifting**. This is applied only to **integer** values, and you mustn't use floats as arguments for it.

```
12345 × 10 = 123450
```

As you can see, **multiplying by ten is in fact a shift** of all the digits to the left and filling the resulting gap with zero.

```
12340 ÷ 10 = 1234
```

Dividing by ten is nothing but shifting the digits to the right.

The same kind of operation is performed by the computer, but with one difference: as two is the base for binary numbers (not 10), **shifting a value one bit to the left thus corresponds to multiplying it by two**; respectively, **shifting one bit to the right is like dividing by two** (notice that the rightmost bit is lost).

The shift operators in Python are a pair of digraphs: `<<` and `>>`, clearly suggesting in which direction the shift will act.

```
value << bits
value >> bits
```

**The left argument of these operators is an integer value whose bits are shifted. The right argument determines the size of the shift.**

The priority of these operators is very high.
