## Looping your code with while

```
while there is something to do:
    do it
```

If you notice some similarities to the _if_ instruction, that's quite all right. Indeed, the syntactic difference is only one: you use the word ```while``` instead of the word ```if```.

The semantic difference is more important: when the condition is met, _if_ performs its statements **only once**; _while_ **repeats the execution as long as the condition evaluates to** ```True```.

Note: all the rules regarding **indentation** are applicable here, too.

It is now important to remember that:

- if you want to execute **more than one statement inside one** ```while``` **loop**, you must (as with ```if```) **indent** all the instructions in the same way;
- an instruction or set of instructions executed inside the ```while``` loop is called the **loop's body**;
- if the condition is ```False``` (equal to zero) as early as when it is tested for the first time, the body is not executed even once (note the analogy of not having to do anything if there is nothing to do);
- the body should be able to change the condition's value, because if the condition is ```True``` at the beginning, the body might run continuously to infinity – notice that doing a thing usually decreases the number of things to do).

### An infinite loop

An infinite loop, also called an **endless loop**, is a sequence of instructions in a program which repeat indefinitely (loop endlessly.)

```
while True:
    print("I'm stuck inside a loop.")
```

This loop will infinitely print "I'm stuck inside a loop." on the screen.

### The while loop and the else branch

Both loops, ```while``` and ```for```, have one interesting (and rarely used) feature.

As you may have suspected, **loops may have the** ```else``` **branch too, like** ```if```**s**.

The loop's ```else``` branch is **always executed once, regardless of whether the loop has entered its body or not**.

```
while there is something to do:
    do it
else:
    do it
```
