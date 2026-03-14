# Quiz-3: Functions, Dictionaries, Tuples and File Handling

## #1 What is the output of the following Python function?

```python
def check(x):
    return x + 7
print(check(3))
```

10

## #2 What is a better way to properly close the file after reading or writing?

Use the "with" statement

```python
# Use with statement as it will automatically close the file.

# Reading a file
with open('sample-data.txt', 'r') as file_stream:
    for line in file_stream:
        print(line)

# Writing/appending to a file
with open('test.txt', 'a') as file_stream:
    file_stream.write('I love Python\n')
    file_stream.write('I love meditation\n')
```

## #3 The following dictionary contains salaries based on skill and experience level. Which statement can retrieve a senior, php engineer's salary?

```python
salaries = {
    'python': { 'junior': '100k', 'senior': '600k' },
    'php': { 'junior': '70k', 'senior': '400k' },
    'java': { 'junior': '80k', 'senior': '500k' },
}
```

Following will retrieve a senior PHP engineer's salary:
```python
salaries['php']['senior']
```

## #4 How do you write a list of lines to a file in Python?

Use the "writelines" function

```python
with open('dummy.txt', 'w') as file_stream:
    file_stream.writelines([
        'Line One\n',
        'Line Two\n',
        'Line Three\n'
    ])
```

## #5 What does the return statement do in a function?

It exits the function & returns the value to the calling function

## #6 What is the purpose of items() function in a Python dictionary?

To iterate through every item of a dictionary and get key, value pair from that item

## #7 Which of the following pip commands correctly installs version 1.5.3 of pandas?

`pip install pandas==1.5.3`

## #8 Which of the following commands is used to open a file in append mode in Python?

```python
with open('test.txt', 'a') as file_stream:
    file_stream.write('I love Python\n')
    file_stream.write('I love meditation\n')
```
