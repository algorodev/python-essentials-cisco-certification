## Floats

Now it's time to talk about another type, which is designed to represent and to store the numbers that (as a mathematician would say) have a **non-empty decimal fraction**.

They are the numbers that have (or may have) a fractional part after the decimal point, and although such a definition is very poor, it's certainly sufficient for what we wish to discuss.

Whenever we use a term like _two and a half or minus zero point four_, we think of numbers which the computer considers **floating-point** numbers.

Note: _two and a half_ looks normal when you write it in a program, although if your native language prefers to use a comma instead of a point in the number, you should ensure that your **number doesn't contain any commas** at all.

As you can probably imagine, the value of zero point four could be written in Python as ```0.4``` or ```.4```

### Ints vs. floats

The decimal point is essential for recognizing floating-point numbers in Python.

Look at these two numbers:

```
4
4.0
```

You may think that they are exactly the same, but Python sees them in a completely different way.

```4``` is an **integer** number, whereas ```4.0``` is a **floating-point** number.

On the other hand, it's not only points that make a float. You can also use the letter ```e```.

When you want to use any numbers that are very large or very small, you can use **scientific notation**.

Take, for example, the speed of light, expressed in _meters per second_. Written directly it would look like this: ```300000000```.

To avoid writing out so many zeros, physics textbooks use an abbreviated form, which you have probably already seen: ```3 x 10^8```.

It reads: three times ten to the power of eight.

In Python, the same effect is achieved in a slightly different way ```3E8```.

The letter ```E``` (you can also use the lower-case letter ```e``` ‒ it comes from the word **exponent**) is a concise record of the phrase _times ten to the power of_.

Note:

- the **exponent** (the value after the _E_) has to be an integer;
- the **base** (the value in front of the _E_) may be either an integer or a float.

### Coding floats

Let's see how this convention is used to record numbers that are very small (in the sense of their absolute value, which is close to zero).

A physical constant called _Planck's constant_ (and denoted as _h_), according to the textbooks, has the value of: ```6.62607 x 10^-34```.

If you would like to use it in a program, you should write it this way ```6.62607E-34```.

Note: the fact that you've chosen one of the possible forms of coding float values doesn't mean that Python will present it the same way.

Python may sometimes choose **different notation** than you.

Python always chooses **the more economical form of the number's presentation**, and you should take this into consideration when creating literals.
