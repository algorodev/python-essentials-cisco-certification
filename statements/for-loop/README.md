## Looping your code with for

```
for item in range:
    do something with the item
```

Another kind of loop available in Python comes from the observation that sometimes it's more important to **count the "turns" of the loop** than to check the conditions.

Actually, the ```for``` loop is designed to do more complicated tasks – **it can "browse" large collections of data item by item**. We'll show you how to do that soon, but right now we're going to present a simpler variant of its application.

There are some new elements. Let us tell you about them:

- the _for_ keyword opens the ```for``` loop; note – there's no condition after it; you don't have to think about conditions, as they're checked internally, without any intervention;
- any variable after the _for_ keyword is the **control variable** of the loop; it counts the loop's turns, and does it automatically;
- the _in_ keyword introduces a syntax element describing the range of possible values being assigned to the control variable;
- the ```range()``` function (this is a very special function) is responsible for generating all the desired values of the control variable; in our example, the function will create (we can even say that it will feed the loop with) subsequent values from the following set: 0, 1, 2 .. 97, 98, 99; note: in this case, the ```range()``` function starts its job from 0 and finishes it one step (one integer number) before the value of its argument;
- note the _pass_ keyword inside the loop body – it does nothing at all; it's an **empty instruction** – we put it here because the ```for``` loop's syntax demands at least one instruction inside the body (by the way – ```if```, ```elif```, ```else``` and ```while``` express the same thing)


### The for loop and the else branch

```for``` loops behave a bit differently. The ```i``` variable retains its last value.

When the loop's body isn't executed, the control variable retains the value it had before the loop.

Note: **if the control variable doesn't exist before the loop starts, it won't exist when the execution reaches the** ```else``` **branch**.

```
for item in range:
    do something with the item
else:
    do it
```
