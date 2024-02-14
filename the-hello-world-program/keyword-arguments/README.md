## Keyword arguments

Python offers another mechanism for the passing of arguments, which can be helpful when you want to convince the ```print()``` function to change its behavior a bit.

We aren't going to explain it in depth right now. We plan to do this when we talk about functions. For now, we simply want to show you how it works. Feel free to use it in your own programs.

The mechanism is called **keyword arguments**. The name stems from the fact that the meaning of these arguments is taken not from its location (position) but from the special word (keyword) used to identify them.

The ```print()``` function has two keyword arguments that you can use for your purposes. The first is called ```end```.

In order to use it, it is necessary to know some rules:

- a keyword argument consists of three elements: a **keyword** identifying the argument (```end``` here); an **equal sign** (```=```); and a value assigned to that argument;
- any keyword arguments have to be put **after the last positional argument** (this is very important)

In our example, we have made use of the ```end``` keyword argument, and set it to a string containing one space.

```
My name is Python. Monty Python.
```

As you can see, the ```end``` keyword argument determines the characters the ```print()``` function sends to the output once it reaches the end of its positional arguments.

The default behavior reflects the situation where the ```end``` keyword argument is implicitly used in the following way: ```end="\n"```.

We said previously that the ```print()``` function separates its outputted arguments with spaces. This behavior can be changed, too.

The **keyword argument** that can do this is named ```sep``` (as in separator).

```
My-name-is-Monty-Python.
```

The ```print()``` function now uses a dash, instead of a space, to separate the outputted arguments.

Note: both keyword arguments may be **mixed in one invocation**.
