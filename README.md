# Savetest

## Description:
Savetest helps you save small test cases and run them on your command line application! Simple and easy! Easy and Simple!

You provide the steps of your test case by simply providing the user input to Savetest

## Expected Result:
Savetest will run the test suite on your application, display the results and return running times. Savetest decides quickly! 

If an algorithm is not efficient it will return Time Limit Exceeded (TLE)
i.e. your algorithm is not an algorithm (meaning it goes in an infinite loop) or worth, if your app runs at ![eq](http://latex.codecogs.com/gif.latex?O(n^7)) and ![equation](http://latex.codecogs.com/gif.latex?%281%5Cleq%20n%20%5Cleq%2010%5E9%29)

Give it a try, it can improve your development speed!

## Intructions

1. Go to an empty folder within the CLI in your Mac or Linux
2. Run
```git clone https://github.com/jonadiazz/Savetest.git```
3. Follow usage

## Usage (with example)
### a. Script for testing

Write or copy this code into a modular_exp.py
```python
n = int(raw_input().strip())
m = int(raw_input().strip())

print m % (2**n)
```

This script takes 2 user inputs, applies the inverse of a modular exponentiation on those numbers and `print`s the value.

To run it do `python modular_exp.py`
e.g. 
```
4
42
```
It should return `10`.

### b. Actual Savetest usage

Now, we want to test the script with several values for `n` and `m`, so we need to input this information everytime we need to test `modular_exp.py`.
However, everytime we make a change to our code we might need to re-run all the tests again, so it becomes tedious to repeat this task over and over.

- Every test case needs to be separated by an empty line. So, just press enter 2 times after writing each test case.
    - Savetest will prompt you to enter a new TEST case
- To save all the tests and quit type `save()` anytime

#### Example:

```
~$ python savetestinput.py for modular_exp.py

╰─○	Enter test cases separated by an empty line.
	Save and exit by writing command "save()" (without quotes)

╭─○	User input for TEST 0

    4
    42

╭─○	User input for TEST 1

	1
	58

╭─○	User input for TEST 2

	98765432
	23456789

╭─○	User input for TEST 3

	save()
~$
```

#### Now, to run this tests
```
~$ pypy savetest.py for a.py`
```
It will produce the following output:
```
┲  running modular_exp.py with test case 0

    4
    42
    10

    48 ms

┲  running modular_exp.py with test case 1

    1
    58
    0

    49 ms

┲  running modular_exp.py with test case 2

    98765432
    23456789
    23456789

    59 ms

```
