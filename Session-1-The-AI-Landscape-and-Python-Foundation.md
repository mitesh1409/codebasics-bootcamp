# Session 1: The AI Landscape and Python Foundation

Mar 7 2026  

## Entire AI family tree

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

---

## Traditional AI Vs Generative/Agentic AI

Traditional AI  
Not generative in nature.  

Examples:  
* Spam Classification
* Image Classification
* Home Price Prediction

Generative AI/Agentic AI

Examples:  
* LLMs like ChatGPT, Gemini
* Claude Code

---

## AI Engineer Categories

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

---

## Study/Explore AI Engineer Job Posts

Study/Explore AI Engineer Job Posts to get idea about the company/employer expectations/job description.  

---

## The Mindset Shift

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

---

## Why Python is popular in AI world?

Python is more English like language.  

Install the following:  
* Python
* VS Code
* uv

## Todos/Exercises

#1  
Setup Python development environment.

Install the following:  
* Python
* VS Code
* uv

#2  
* [Python UV: The Ultimate Guide to the Fastest Python Package Manager](https://www.datacamp.com/tutorial/python-uv)
* [uv](https://docs.astral.sh/uv/)

#3
Create a sample project using uv.  
Install some packages using uv, like "python-dotenv", "ruff" etc.

When we setup a project using `uv init project-name`, directory structure looks like:  

|-- .gitignore
|-- .python-version
|-- README.md
|-- hello.py
|-- pyproject.toml <-- similar to package.json
|-- .venv (directory/folder) <-- similar to node_modules folder
|-- uv.lock <-- similar to package-lock.json

Activate virtual environment by running `.venv\Scripts\activate` from the project directory.  

#4  
PEP8 coding convention.

#5  
We have stock data file in CSV format.  
stock_data.csv  
columns = ticker/symbol, price/ltp, book_value, eps  

Calculate and add two new columns - pe_ratio, pb_ratio
pe_ratio = price / eps
pb_ratio = price / book_value

Generate a new file with all the columns.
Do vibe coding.

#6  
Using with to read/write files.  

#7  
Casting operations - for example string value to number.  

#8  
Type hinting in Python.  
Useful in static analysis of the code.  

#9  
Create a simple program which calls a function to calculate market cap of a company.  
Display the output.  
Market cap = number of outstanding shares X current market price of a share

#10  
Convert the program written in task #5 to OOP style.  
Do vibe coding.  

Understand code at a higher level and become an orchestrator.  

* Class
* Constructor
* Object
* Static/Non-static Methods (behaviour)
* Static/Non-static Properties (state)

#11  
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

#12  
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

## Quiz

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
