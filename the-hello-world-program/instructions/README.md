## Instructions

You have already seen a computer program that contains one function invocation. A function invocation is one of many possible kinds of Python **instruction**.

Of course, any complex program usually contains many more instructions than one. The question is: how do you couple more than one instruction into the Python code?

Python's syntax is quite specific in this area. Unlike most programming languages, Python requires that **there cannot be more than one instruction in a line**.

A line can be empty (i.e., it may contain no instruction at all) but it must not contain two, three or more instructions. This is strictly prohibited.

Note: Python makes one exception to this rule ‒ it allows one instruction to spread across more than one line (which may be helpful when your code contains complex constructions).

This is a good opportunity to make some observations:

- the program invokes the ```print()``` **function twice**, and you can see two separate lines in the console ‒ this means that ```print()``` begins its output from a new line each time it starts its execution; you can change this behavior, but you can also use it to your advantage;
- each ```print()``` invocation contains a different string, as its argument, and the console content reflects it ‒ this means that **the instructions in the code are executed in the same order** in which they have been placed in the source file; no subsequent instruction is executed until the previous one is completed (there are some exceptions to this rule, but you can ignore them for now.)
