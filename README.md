# Savetest

## Description:
*Savetest* helps you save small test cases and run them on your command line application! Simple and easy! Easy and Simple!

You provide the steps of your test cases by simply writing the user input to *Savetest* (like you would normally for your app)

## Expected Result:
Savetest will run the test suite on your application, display the results and return running times. Savetest decides quickly!

If an algorithm is not efficient it will return *Time Limit Exceeded* (TLE)
*i.e.* Your algorithm is not an algorithm (goes in an infinite loop) or worse, if your app runs at ![eq0](http://latex.codecogs.com/gif.latex?O(n^7)) where ![eq1](http://latex.codecogs.com/gif.latex?%281%5Cleq%20n%20%5Cleq%2010%5E9%29)

Give it a try, it can improve your development speed!

## Instructions:
1. Within the cli change to an empty directory in your Mac or Linux machine
2. Run `git clone https://github.com/jonadiazz/Savetest.git`
3. Now follow usage example

**Tip:**
- Create alias `alias savetest="python Savetest/main.py"`

## Usage (with example):
### a. Write a simple script to use for testing Savetest

Write or copy this code into a modular_exp.py (file also included in *sample script* folder)

```python
n = int(raw_input().strip())
m = int(raw_input().strip())

print m % (2**n)
```

This script takes 2 user inputs, and returns the inverse of a modular exponentiation ![eq2](http://latex.codecogs.com/gif.latex?m%20%5Cmod%202%5En)

Run: `pypy modular_exp.py`

Input:
```
4
42
```
It should return `10`.

### b. Actual *Savetest* usage

Now, we want to test the script with different values of *`n`* and *`m`*

**Note:**
- Every test case needs to be separated by an empty line. Just press enter twice to delimit each test case
    - Savetest will then prompt you to enter a *new* test
- Save all tests and quit by typing *`save()`* anytime

#### Example:
```
~$ savetest add modular_exp.py

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

	save()
~$
```

#### Now, to run these tests

```
~$ savetest run modular_exp.py`
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


Now, add really big numbers to see how **Savetest** handles it with your application
