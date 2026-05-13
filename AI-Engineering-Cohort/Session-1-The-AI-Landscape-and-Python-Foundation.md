# Session 1: The AI Landscape and Python Foundation

<a name="top"></a>

Mar 7 2026  

## Topics

* [#1 The Entire AI Family Tree](#1-the-entire-ai-family-tree)
* [#2 Traditional AI Vs Generative/Agentic AI](#2-traditional-ai-vs-generativeagentic-ai)
* [#3 AI Engineer Categories](#3-ai-engineer-categories)
* [#4 Study/Explore AI Engineer Job Posts](#4-studyexplore-ai-engineer-job-posts)
* [#5 The Mindset Shift](#5-the-mindset-shift)
* [#6 Why Python is Popular in AI World?](#6-why-python-is-popular-in-ai-world)
* [#7 Todos/Exercises](#7-todosexercises)
* [#8 Quizzes](#8-quizzes)

---

## #1 The Entire AI Family Tree

AI (Artificial Intelligence)  

ML (Machine Learning) is part of AI.

In ML (Machine Learning), there are two sub-domains:  

* Statistical ML
  Algorithms like:  
  - Linear Regression
  - Decision Tree
  - K-means
  Supervised dataset: it means labeled data
* Deep Learning
  - Neural Networks
  - CNN
  - RNN
  - Transformers

What is available outside ML (Machine Learning) if I want to do AI?

Regular Expressions  
Rule based programming  
Robotics  

Generative AI and Agentic AI are applications of Transformers.  

LLMs are based on transformer architecture.  

Transformer Architecture is the base of LLMs.

[⬆ Back to Top](#top)

---

## #2 Traditional AI Vs Generative/Agentic AI

Traditional AI  
It is not generative in nature.  

Examples:  

* Spam Classification
* Image Classification
* Home Price Prediction

Generative AI/Agentic AI

Examples:  

* LLMs like ChatGPT, Gemini
* Claude Code

[⬆ Back to Top](#top)

---

## #3 AI Engineer Categories

1. Integrator
    Software Engineer who can integrate AI into existing application.
    Good front-end + back-end or full-stack knowledge.
    Integrating AI into current application.

2. Builder
    Who can build LLM models
    AI Research Engineers
    Data Scientists
    Applied Scientists

3. All Rounder
    Combination of #1 and #2, who has overview of both #1 & #2
    Build Gen AI solution by calling LLM APIs
    Train a small statistical model
    etc.

[⬆ Back to Top](#top)

---

## #4 Study/Explore AI Engineer Job Posts

Study/Explore AI Engineer Job Posts to get idea about the company/employer expectations/job description.  

[⬆ Back to Top](#top)

---

## #5 The Mindset Shift

Today or tomorrow you have to accept that it is the end of the era for writing code by hand.  

Developer's job is evolved -  

* generate code with the help of Gen AI
* act as an orchestrator
* review generated code quality
* helping in architectural decisions
* output is aligned with business requirements
* take max benefit of vibe coding
* build products faster

Imagine working in a factory with assembly line.  
Just like that code is produced on assembly line using Gen AI tools and as a developer  
we need to keep an eye on quality, make sure it meets business requirements, orchestrating  
different parts of the application components etc.

Vibe Coding?  
Using Gen AI tools like Cursor, Claude Code, Antigravity etc. to write code.  

> Vibe coding is the new product management.  
> Training and tuning models is the new coding.  
Posted on X by @naval

> The hottest new programming language is English
Posted on X by @karpathy

[⬆ Back to Top](#top)

---

## #6 Why Python is Popular in AI World?

Python is more English like language.  

[Python Package Index](https://pypi.org/)

[⬆ Back to Top](#top)

---

## #7 Todos/Exercises

### Exercise #1 - Setup Python development environment

### Exercise #2 - Explore uv (Python package and project manager)

An extremely fast Python package and project manager, written in Rust.

* [Python UV: The Ultimate Guide to the Fastest Python Package Manager](https://www.datacamp.com/tutorial/python-uv)
* [uv](https://docs.astral.sh/uv/)

### Exercise #3 - Create a sample project using uv

### Exercise #4 - PEP 8 Style Guide for Python Code

### Exercise #5 - Processing data from CSV file
We have stock data file in CSV format.  
stock_data.csv  
columns = ticker/symbol, price/ltp, book_value, eps  

Calculate and add two new columns - pe_ratio, pb_ratio
pe_ratio = price / eps
pb_ratio = price / book_value

Generate a new file with all the columns.
Do vibe coding.

### Exercise #6 - Using `with` to read/write files

### Exercise #7 - Casting in Python

### Exercise #8 - Type hinting in Python

#9  
Create a simple program which calls a function to calculate market cap of a company.  
Display the output.  
Market cap = number of outstanding shares X current market price of a share

### Exercise #10 - Documenting functions in Python

### Exercise #11 - Commenting in Python

#12  
Convert the program written in task #5 to OOP style.  
Do vibe coding.  

Understand code at a higher level and become an orchestrator.  

* Class
* Constructor
* Object
* Static/Non-static Methods (behaviour)
* Static/Non-static Properties (state)

#13  
APIs and Decorators  

GitHub Profile Analyser  
Write code that can analyse a GitHub profile and return a response.

`uv add requests`

"requests" library/package to make API calls.

Decorators in Python  
Examples with and without decorator.  

```python
# Write a function to calculate sum of a series of numbers (e.g., 1 to 100_000)

# Function #1: Loop through 1 to 100_000 and do the sum. Calculate execution time.
# Function #2: Use a formula to do the sum of 1 to 100_000. Calculate execution time.

def sum_with_loop(n):
  start_time = perf_counter()
  sum = 0
  for i in range(100_000):
    sum += i
  end_time = perf_counter()

  print(f'Function #1: Loop through the range, execution time {end_time - start_time:.6f} seconds')
  return sum

def sum_with_formula(n):
  start_time = perf_counter()
  sum = n * (n - 1) / 2
  end_time = perf_counter()

  print(f'Function #2: With formula, execution time {end_time - start_time:.6f} seconds')
  return sum
```

Here the code which calculates execution time is getting repeated.  

How can decorators help here?

Decorator = Accessory

#14  
Groq LLM

Calling an LLM API

Create an account @ https://console.groq.com/home
It is free to use, get your API key.

Create .env file and set the following environment variables:

```
GROQ_API_KEY=<API-KEY>
GROQ_MODEL=<MODEL-NAME>
```

Install fastapi  
`uv add fastapi`

fastapi allows you to write back-end servers in Python.  
fastapi is like express in Node.js.  

`uv add uvicorn`
Also install uvicorn, which automatically reloads the server on file changes.  
uvicorn is like nodemon in Node.js.  

get_joke.py

```python
from fastapi import FastAPI
from random import choice

app = FastAPI()

JOKES = [
  "JOKE #1",
  "JOKE #2",
  "JOKE #3",
  "JOKE #4",
  "JOKE #5",
]

@app.get("/joke")
def get_joke():
  return {
    "joke": choice(JOKES)
  }
```

Run this server from the app directory.

Access the following end point from the Browser or Postman.  
GET /joke  
Returns a random joke.  

GET /docs  
Returns a documentation page.  

All this was done without LLM.

Now lets use LLM to generate a joke.  
We will LLM a topic to generate a joke.  

`uv add groq`

Complext tasks -> use Thinking model
Simple tasks -> use Simple model

#15  
Study/Explore AI Engineer Job Posts to get idea about the company/employer expectations/job description.  

[⬆ Back to Top](#top)

---

## #8 Quizzes

Quiz #1  
What is the purpose of the following line in a Python file?  

```python
if __name__ == '__main__':
  # some code block
```

Answer:  
It runs the code block only when the file is executed directly.

Quiz #2  
What is the output of the following code?  

```python
price = 10.0
shares = 100
print(f'Market Cap: ${price * shares}')
```

Answer:  
Market Cap: $1000

Quiz #3  
What actually runs when you call a function that has been decorated with `@my_decorator`?

Answer:  
The wrapper function returned by the decorator, which internally calls  
the original function (on which the decorator is applied).  

Quiz #4  
What does the annotation `def calculate_area(width: float, height: float) -> float:` tell us?  

Answer:  
It documents that the function expects two floats and returns a float,  
but Python does not enforce this at runtime.  

Quiz #5  
What is the purpose of the `__init__` method in a Python class?  

Answer:  
It initializes the object's attributes when a new instance is created.  

Quiz #6  
What does `response.json()` do in the requests library?  

Answer:  
Converts the response body from a JSON string into a Python dictionary (or list).  

Quiz #7  
When should you use `@staticmethod` inside a class?  

Answer:  
When the method is a utility that doesn't need self or cls.  

Quiz #8  
A REST API returns status code 200. What does this indicate?  

Answer:  
The request was successful.  

Quiz #9  
Why use `load_dotenv()` and `os.getenv('API_KEY')` instead of hardcoding secrets in source code?  

Answer:  
It seperates secrets from code, preventing accidental exposure.  

[⬆ Back to Top](#top)
