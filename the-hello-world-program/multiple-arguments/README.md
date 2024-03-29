## Using multiple arguments

So far we have tested the ```print()``` function behavior with no arguments, and with one argument. It's also worth trying to feed the ```print()``` function with more than one argument.

There is one ```print()``` function invocation, but it contains **three arguments**. All of them are strings.

The arguments are **separated by commas**. We've surrounded them with spaces to make them more visible, but it's not really necessary, and we won't be doing it anymore.

In this case, the commas separating the arguments play a completely different role than the comma inside the string. The former is a part of Python's syntax, while the latter is intended to be shown in the console.

If you look at the code again, you'll see that there are no spaces inside the strings.

The spaces, removed from the strings, have appeared again. Can you explain why?

Two conclusions emerge from this example:

- a ```print()``` function invoked with more than one argument **outputs them all on one line**;
- the ```print()``` function **puts a space between the outputted arguments** on its own initiative.
