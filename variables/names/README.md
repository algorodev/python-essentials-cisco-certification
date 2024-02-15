## Variable names

It seems fairly obvious that Python should allow you to encode literals carrying number and text values.

You already know that you can do some arithmetic operations with these numbers: add, subtract, etc. You'll be doing that many times.

But it's quite a normal question to ask how to **store the results** of these operations, in order to use them in other operations, and so on.

Python will help you with that. It offers special "boxes" (or "containers" as we may call them) for that purpose, and these boxes are called **variables** ‒ the name itself suggests that the content of these containers can be varied in (almost) any way.

What does every Python variable have?

- a name;
- a value (the content of the container)

If you want to **give a name to a variable**, you must follow some strict rules:

- the name of the variable must be composed of upper-case or lower-case letters, digits, and the character ```_``` (underscore)
- the name of the variable must begin with a letter;
- the underscore character is a letter;
- upper- and lower-case letters are treated as different (a little differently than in the real world – _Alice_ and _ALICE_ are the same first names, but in Python they are two different variable names, and consequently, two different variables);
- the name of the variable must not be any of Python's reserved words (the keywords – we'll explain more about this soon).

Note that the same restrictions apply to function names.

Python does not impose restrictions on the length of variable names, but that doesn't mean that a long variable name is always better than a short one.

Here are some correct, but not always convenient variable names:
- ```MyVariable```
- ```i```
- ```l```
- ```t34```
- ```Exchange_Rate```
- ```counter```
- ```days_to_christmas```
- ```TheNameIsTooLongAndHardlyReadable```
- ```_```
- ```Adiós_Señora```
- ```sûr_la_mer```
- ```Einbahnstraße```
- ```переменная.```

And now for some incorrect names:
- ```10t``` (does not begin with a letter)
- ```!important``` (does not begin with a letter)
- ```exchange rate``` (contains a space).

### Keywords

Take a look at the list of words that play a very special role in every Python program.

- ```False```
- ```None```
- ```True```
- ```and```
- ```as```
- ```assert```
- ```break```
- ```class```
- ```continue```
- ```def```
- ```del```
- ```elif```
- ```else```
- ```except```
- ```finally```
- ```for```
- ```from```
- ```global```
- ```if```
- ```import```
- ```in```
- ```is```
- ```lambda```
- ```nonlocal```
- ```not```
- ```or```
- ```pass```
- ```raise```
- ```return```
- ```try```
- ```while```
- ```with```
- ```yield```

They are called **keywords** or (more precisely) **reserved keywords**. They are reserved because **you mustn't use them as names**: neither for your variables, nor functions, nor any other named entities you want to create.

The meaning of the reserved word is **predefined**, and mustn't be changed in any way.

Fortunately, due to the fact that Python is case-sensitive, you can modify any of these words by changing the case of any letter, thus creating a new word, which is not reserved anymore.
