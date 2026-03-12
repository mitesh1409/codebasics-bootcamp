# Quiz-2: Lists, if condition & for loop

## #1 How does the continue statement affect a for loop in Python?

It skips the current iteration and proceeds to the next iteration

## #2 What happens when you try to remove an element that is not present in the list using remove()?

```python
animals = ["cat", "dog", "rabbit", "wolf"]
animals.remove("lion")
```

It raises a ValueError  
ValueError: list.remove(x): x not in list

## #3 What will the output be when you run the following for loop?

```python
for i in range(4):
    print(i)
```

0
1
2
3

## #4 What will be the output of the following code?

```python
n = -5
message = "Negative" if n >= 0 else "Positive"
print(message)
```

Positive

## #5 What is the result of the following code?

```python
prices = [300, 50, 1200, 10]
sorted(prices)
print(prices[2])
```

`sorted(prices)`  
`sorted()` does not modify the original list,  
but it sorts and returns a new list.

`prices.sort()`  
Whereas `sort()` method when called on list object  
modifies the original list object.

## #6 What will the following code output?

```python
age = 17
if age >= 30:
    print("Adult")
elif age > 18 and age < 30:
    print("Young adult")
else:
    print("Minor")
```

Minor

## #7 What will be the output of the following code?

```python
lst = [1, [2, 3], 4, [5, [6, 7]]]
print(lst[3][1][0])
```

6

## #8 What will the output be when you run the following for loop?

```python
for i in range(2,10):
    if i % 5 == 0:
        break
    print(i)
```

2
3
4

## #9 Which of the following will add "orange" to the fruits list?

```python
fruits = ["apple", "banana", "cherry", "date"]
```

```python
fruits.append("orange")
```

## #10 What is the result of the following code?

```python
office_supplies = ["pen", "paper", "stapler"]
kitchen_supplies = ["fork", "knife", "spoon"]
combined_list =  kitchen_supplies + office_supplies
print(combined_list[2: 4])
```

['spoon', 'pen']
