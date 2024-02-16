## Conditions and conditional execution

You have to have a mechanism which will allow you to do something **if a condition is met, and not do it if it isn't**.

It's just like in real life: you do certain things or you don't when a specific condition is met or not, e.g., you go for a walk if the weather is good, or stay home if it's wet and cold.

To make such decisions, Python offers a special instruction. Due to its nature and its application, it's called a **conditional instruction** (or conditional statement).

This conditional statement consists of the following, strictly necessary, elements in this and this order only:

- the ```if``` keyword;
- one or more white spaces;
- an expression (a question or an answer) whose value will be interpreted solely in terms of ```True``` (when its value is non-zero) and ```False``` (when it is equal to zero);
- a ```colon``` followed by a newline;
- an ```indented``` instruction or set of instructions (at least one instruction is absolutely required); the ```indentation``` may be achieved in two ways – by inserting a particular number of spaces (the recommendation is to use ```four spaces of indentation```), or by using the _tab_ character; note: if there is more than one instruction in the indented part, the indentation should be the same in all lines; even though it may look the same if you use tabs mixed with spaces, it's important to make all indentations **exactly the same** – Python 3 **does not allow the mixing of spaces and tabs** for indentation.

How does that statement work?

- If the ```true_or_not``` expression **represents the truth** (i.e., its value is not equal to zero), **the indented statement(s) will be executed**;
- if the ```true_or_not``` expression **does not represent the truth** (i.e., its value is equal to zero), **the indented statement(s) will be omitted** (ignored), and the next executed instruction will be the one after the original indentation level.

### Conditional execution: the if statement

If a certain sleepless Python developer falls asleep when he or she counts 120 sheep, and the sleep-inducing procedure may be implemented as a special function named ```sleep_and_dream()```, the whole code takes the following shape:

```
if sheep_counter >= 120:
    sleep_and_dream()
```

You can read it as: if ```sheep_counter``` is greater than or equal to ```120```, then fall asleep and dream (i.e., execute the ```sleep_and_dream``` function.)

We've said that **conditionally executed statements have to be indented**. This creates a very legible structure, clearly demonstrating all possible execution paths in the code.

### Conditional execution: the if-else statement

We started out with a simple phrase which read: _If the weather is good, we will go for a walk_.

Note: there is not a word about what will happen if the weather is bad. We only know that we won't go outdoors, but what we could do instead is not known. We may want to plan something in case of bad weather, too.

We can say, for example: _If the weather is good, we will go for a walk, otherwise we will go to a theater_.

Thus, there is a new word: ```else``` – this is a keyword.

The part of the code which begins with ```else``` says what to do if the condition specified for the ``if`` is not met (note the ```colon``` after the word).

The _if-else_ execution goes as follows:

- if the condition evaluates to **True** (its value is not equal to zero), the ```perform_if_condition_true``` statement is executed, and the conditional statement comes to an end;
- if the condition evaluates to **False** (it is equal to zero), the ```perform_if_condition_false``` statement is executed, and the conditional statement comes to an end.

### Nested if-else statements

First, consider the case where the **instruction placed after the** ```if``` **is another** ```if```.

Read what we have planned for this Sunday. If the weather is fine, we'll go for a walk. If we find a nice restaurant, we'll have lunch there. Otherwise, we'll eat a sandwich. If the weather is poor, we'll go to the theater. If there are no tickets, we'll go shopping in the nearest mall.

Here are two important points:

- this use of the ```if``` statement is known as **nesting**; remember that every ```else``` refers to the ```if``` which lies **at the same indentation level**; you need to know this to determine how the _ifs_ and _elses_ pair up;
- consider how the **indentation improves readability**, and makes the code easier to understand and trace.

### The elif statement

The second special case introduces another new Python keyword: **elif**. As you probably suspect, it's a shorter form of **else if**.

```elif``` is used to **check more than just one condition**, and to **stop** when the first statement which is true is found.

Our next example resembles nesting, but the similarities are very slight. Again, we'll change our plans and express them as follows: If the weather is fine, we'll go for a walk, otherwise if we get tickets, we'll go to the theater, otherwise if there are free tables at the restaurant, we'll go for lunch; if all else fails, we'll stay home and play chess.

Have you noticed how many times we've used the word _otherwise_? This is the stage where the ```elif``` keyword plays its role.

The way to assemble subsequent _if-elif-else_ statements is sometimes called a **cascade**.

Notice again how the indentation improves the readability of the code.

Some additional attention has to be paid in this case:

- you **mustn't use** ```else``` **without a preceding** ```if```;
- ```else``` is always the **last branch of the cascade**, regardless of whether you've used ```elif``` or not;
- ```else``` is an **optional** part of the cascade, and may be omitted;
- if there is an ```else``` branch in the cascade, only one of all the branches is executed;
- if there is no ```else``` branch, it's possible that none of the available branches is executed.
