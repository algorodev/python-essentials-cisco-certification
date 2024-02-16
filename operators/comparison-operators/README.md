## Comparison

### Equality operator

Question: **are two values equal**?

To ask this question, you use the ```==``` (equal equal) operator.

Don't forget this important distinction:

- ```=``` is an assignment operator, e.g., ```a = b ```assigns ```a``` with the value of ```b```;
- ```==``` is the question are these values equal? so ```a == b``` compares ```a``` and ```b```.

It is a **binary operator with left-sided binding**. It needs two arguments and **checks if they are equal**.

### Inequality: the _not equal to_ operator (!=)

The ```!=``` (not equal to) operator compares the values of two operands, too. Here is the difference: if they are equal, the result of the comparison is ```False```. If they are not equal, the result of the comparison is ```True```.

### Comparison operators: greater than

The _greater than_ operator has another special, **non-strict** variant, but it's denoted differently than in classical arithmetic notation: ```>=``` (greater than or equal to).

There are two subsequent signs, not one.

Both of these operators (strict and non-strict), as well as the two others discussed in the next section, are **binary operators with left-sided binding**, and their **priority is greater than that shown by** ```==``` **and** ```!=```.

### Comparison operators: less than/less than or equal to

As you've probably already guessed, the operators used in this case are: the ```<``` (less than) operator and its non-strict sibling: ```<=``` (less than or equal to).
