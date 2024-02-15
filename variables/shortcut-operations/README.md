## Shortcut operations

It's time for the next set of operators that make a developer's life easier. Very often, we want to use one and the same
variable both to the right and left sides of the ```=``` operator.

Let's try to present a general description for these operations. If ```op``` is a two-argument operator (this is a very
important condition) and the operator is used in the following context...:

```
variable = variable op expression
```

...then it can be simplified and shown as follows:

```
variable op= expression
```

Take a look at the examples below. Make sure you understand them all.

| Expression                    |     Shortcut operator      |
|-------------------------------|:--------------------------:|
| ```i = i + 2 * j```           |     ```*i += 2 * j```      |
| ```var = var / 2```           |       ```var /= 2```       |
| ```rem = rem % 10```          |      ```rem %= 10```       |
| ```j = j - (i + var + rem)``` | ```j -= (i + var + rem)``` |
| ```x = x ** 2```              |       ```x **= 2```        |
