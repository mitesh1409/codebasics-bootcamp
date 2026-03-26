# Quiz-5: NumPy

## #1 What does `np.arange(10)` produce?

array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

## #2 Why is a NumPy array faster compared to a Python list?

NumPy uses fixed types and contiguous memory locations which allows for more efficient data processing

Compared to Python Lists NumPy

* requires less memory
* does faster execution

## #3 What will be the output of the following code?

```python
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(arr[:2, 1:])
```

Output:

[[20 30]
 [50 60]]

## #4 What is the shape of an array created using `np.zeros((3, 4))`?

(3, 4)

## #5 What does the `np.linspace` function do?

Creates an array with linearly spaced values
