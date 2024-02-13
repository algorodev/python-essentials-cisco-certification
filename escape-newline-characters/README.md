## Python escape and newline characters

Interestingly, while **you can see two characters, Python sees one**.

The backslash (``` \ ```) has a very special meaning when used inside strings ‒ this is called **the escape character**.

The word _escape_ should be understood specifically ‒ it means that the series of characters in the string escapes for the moment (a very short moment) to introduce a special inclusion.

In other words, the backslash doesn't mean anything in itself, but is only a kind of announcement, that the next character after the backslash has a different meaning too.

The letter ```n``` placed after the backslash comes from the word newline.

Both the backslash and the _n_ form a special symbol named **a newline character**, which urges the console to start a **new output line**.

This convention has two important consequences:

1. If you want to put just one backslash inside a string, don't forget its escaping nature ‒ you have to double it. For example, an invocation like this will cause an error:

```
print("\")
```

while this one won't:

```
print("\\")
```

2. Not all escape pairs (the backslash coupled with another character) mean something.
