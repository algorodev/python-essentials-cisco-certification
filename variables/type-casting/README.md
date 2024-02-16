## Type casting (type conversion)

Python offers two simple functions to specify a type of data and solve this problem ‒ here they are: ```int()``` and ```float()```.

Their names are self-commenting:

- the ```int()``` function **takes one argument** (e.g., a string: ```int(string)```) and tries to convert it into an integer; if it fails, the whole program will fail too (there is a workaround for this situation, but we'll show you this a little later);
- the ```float()``` function takes one argument (e.g., a string: ```float(string)```) and tries to convert it into a float (the rest is the same).

This is very simple and very effective. Moreover, you can invoke any of the functions by passing the ```input()``` results directly to them. There's no need to use any variable as an intermediate storage.
