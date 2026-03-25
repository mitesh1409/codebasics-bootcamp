# Quiz-4: Classes and Exception Handling

## #1 What is the purpose of the finally block?

To execute code, whether an exception occurs or not

## #2 What will be the output for the following code?

```python
try:
    print(1/0)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("Error occurred:", e)
```

Output:
Cannot divide by zero.

Division by zero raises/throws "ZeroDivisionError" exception which is one of the built-in Python exceptions.

## #3 What happens if an exception is raised but not handled?

The program terminates/crashes and an error message is displayed

## #4 What is the role of the except block?

To handle the error/exception raised in the try block

## #5 What is instantiation in the context of object-oriented programming?

Creating an object of a class

## #6 What is the purpose of the super() function in Python?

It is used to call methods from the parent class

## #7 Which of the following is true about the __init__ method in Python classes?

(A) It is used to initialize new objects
(B) It is called automatically whenever an object is created
(C) Both options (A) and (B)
(D) It makes sure the class is well-behaved during instantiation

Answer:
(C) Both options (A) and (B)

## #8 Given the following Python class, what will be the output when you create an instance and call my_pet.speak()?

```python
class Pet:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(self.sound)

my_pet = Pet("Buster", "Woof")
my_pet.speak()
```

Output:
Woof
