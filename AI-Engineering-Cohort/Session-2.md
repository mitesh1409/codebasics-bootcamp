<a name="top"></a>

# Session 2: LLMs, Embeddings & Vector DBs

Mar 8 2026  

## Topics

* [#1 Generative AI](#1-generative-ai)
* [#2 AI Agent](#2-ai-agent)
* [#3 Software 1.0 Software 2.0 Software 3.0](#3-software-10-software-20-software-30)
* [#4 Follow Andrej Karpathy](#4-follow-andrej-karpathy)
* [#5 Gen AI (LLM only) Vs AI Agent Vs Agentic AI](#5-gen-ai-llm-only-vs-ai-agent-vs-agentic-ai)
* [#6 What exactly are LLMs?](#6-what-exactly-are-llms)
* [#7 Transformers](#7-transformers)
* [#8 Key Parameters](#8-key-parameters)
* [#9 What Exactly is a Token?](#9-what-exactly-is-a-token)
* [#10 Vector Databases](#10-vector-databases)
* [#11 Todos/Exercises](#11-todosexercises)
* [#12 Quizzes](#12-quizzes)

---

## #1 Generative AI

Generative AI is a type of artificial intelligence that creates new content -  
such as text, images, audio/video - based on patterns learned from existing data.  

ChatGPT -> It is an application that uses LLM GPT-5  
GPT-5 -> LLM  

Claude -> It is an application that uses LLM Sonnet 4.6
Sonnet 4.6 -> LLM  

LLM is the brain.  
Application is the body which needs a brain.  

LLMs are trained on vast amount of data (source: internet or other?),  
then they do a reinforcement learning with human feedback RLHF.

So as an AI engineer we will build applications that will use LLM as their brain.  

[⬆ Back to Top](#top)

---

## #2 AI Agent

**AI Agent**  

AI Agent is a program that takes input, thinks and acts to complete a task  
using tools, memory and knowledge.  

AI Agent = LLM + Tools + Knowledge + Memory

AI Agents are autonomous but narrow, task specific and does not span multiple or evolving goals.  

**Agentic AI**  

Agentic AI is a system where one or more AI agents work autonomously,  
often over long tasks, making decisions, using tools and even other agents to reach a goal.

Agentic AI is a system with one or more AI agents, these agents interact with each other  
and they try to accomplish a complex goal by doing a multi-step reasoning and multi-step planning.

Examples:  

* Flight booking AI agent
    Tools = AccuWeather API, Expedia platform  
    Knowledge = Database  
    Example Usage:  
    Book a flight for my 7 day trip from New York to New Delhi in May 2026.  
    The weather should be sunny all day.  
    My budget is up to 1600$.  
    And no layovers.  
* Immigration AI agent
    Knowledge = Passport, ID documents, Database etc.  
    Example Usage:  
    Process my VISA.

LLM has a reasoning power, traditional program does not have that capability.  
And it makes the real difference.  

When a user gives instructions like this:  
> Book a flight for my 7 day trip from New York to New Delhi in May 2026.  
> The weather should be sunny all day.  
> My budget is up to 1600$.  
> And no layovers.  

The traditional program won't be able to process this but LLM can extract key information  
from this and can complete the task.  

> An LLM is like a human brain.

[⬆ Back to Top](#top)

---

## #3 Software 1.0 Software 2.0 Software 3.0

[Karpathy's 3 Software Paradigms Expanded](https://kanaka.github.io/blog/karpathy-software-paradigms-expanded/)

[⬆ Back to Top](#top)

---

## #4 Follow Andrej Karpathy

* [Andrej Karpathy | YouTube](https://www.youtube.com/@AndrejKarpathy)
* [Andrej Karpathy | X](https://x.com/karpathy)

[⬆ Back to Top](#top)

---

## #5 Gen AI (LLM only) Vs AI Agent Vs Agentic AI

Here's the markdown table extracted from the screenshot:

| System Type | Gen AI (LLM-only) | AI Agent | Agentic AI |
|---|---|---|---|
| **Task Capability** | Answers based on pre-trained knowledge only | Takes input, decides, and completes a task | Handles multi-step goals with planning and coordination |
| **Tool Usage** | ❌ No external tools | Uses tools to complete a task | Uses multiple tools, may call other agents |
| **Autonomous Decisions** | ❌ No decision-making | ✅ Makes decisions to complete the task | ✅ Plans, decides, and adapts over time |

[⬆ Back to Top](#top)

---

## #6 What exactly are LLMs?

LLMs = Large Language Models

Language Modeling  
A language model is a probability distribution over a sequence of tokens (words/sub-words).

A language model is a probability distribution that tells you that  
given a certain sequence of tokens, what could be the probability that  
the next token is X or Y.

For example, try giving this input - "Roses are red..." to a Gen AI (ChatGPT, Claude, Gemini etc.) and observe the output.  

LLMs are trained on vast amount of data (source: internet or other?),  
then they do a reinforcement learning with human feedback RLHF.

So when you give a sequence of text to an LLM it can predict the next tokens and  
will ultimately able to complete the sentence meaningfully.  

LLM can process text, image, audio etc. type of data.  

Internally LLM uses conditional probability for that.  

Probability is measured on a scale of 0(lowest) to 1(highest).  
P("food" | "I am hungry, I need...") = 0.9 (most likely)  
P("camera" | "I am hungry, I need...") = 0.01 (highly unlikely)  

Example #1  
Input:  
Roses are red...  
Output:  
Violets are blue... (higher probability of getting this)

Example #2  
Input:  
I am feeling hungry, I need...  
Output:  
foo  
OR  
something to eat  
etc. (higher probability of getting this)

> LLM is a kind of a neural network.
> Neural Networks → Deep Learning → Transformers → LLMs
> LLMs are based on Transformers architecture.

[⬆ Back to Top](#top)

---

## #7 Transformers

Reference:  
[How Transformers Work: A Detailed Exploration of Transformer Architecture](https://www.datacamp.com/tutorial/how-transformers-work)

**Word Embeddings**  
Word Embedding is a way to represent text in numeric format such that  
it can capture its meaning.  

**Google's Word2Vec**  
[Google Word2Vec](https://www.kaggle.com/datasets/sugataghosh/google-word2vec)

**Transformer Explainer**  
https://github.com/poloclub/transformer-explainer

https://poloclub.github.io/transformer-explainer/

[⬆ Back to Top](#top)

---

## #8 Key Parameters

Key Parameters

* Context Window
* Temperature
* Top-p & Top-k
* Output Length

**Context Window**  
Maximum number of tokens that can be passed at a time for inference.  
This will be your working memory.  

Thinking tokens are also a part of the Context Window.

Input, output and thinking tokens of a current chat are part of the Context Window.  
They all are counted in the Context Window.  

The LLM will use the attention mechanism to make sense out of that context.  
It will create the contextual embedding and do the next token prediction based on it.  

There is a saying in the AI Engineering:  
> Context is the king.
> Always maintain a clean context.

Example Prompt:  
teach me a philosophy of non-attachment  

Total number of tokens = 7  
Context utilized = 7  

**Temperature**  
Temperature controls how "random" or "creative" the model's output will be.  

The concept of temperature in Physics  
When the temperature of a matter increases it expands,  
and when it decreases it shrinks.  
For example, water gets boiled and converted into vapour (expands) when its temperature  
reaches to 100 celcius or more, and it is converted into ice (shrinks) when its temperature  
reaches to 0 celcius or below.  

AI/ML researchers are mostly from Maths/Physics background, so they borrowed  
a lot of concepts from Maths/Physics.

LLM models are focused at a lower temperature,  
they become creative at a higher temperature, sometimes even gibberish.

LLM Temperature Parameter is a parameter that controls the randomness/creativity of an LLM's output, ranging from **0 to 2**.

| Temperature | Behavior | Probability Distribution | Example Output |
|---|---|---|---|
| **Low (→ 0)** | Deterministic & predictable | Sharp curve — high-probability words dominate | "A cup of **coffee**." |
| **Mid (~1)** | More creative, considers lower-probability words | Moderate spread across options | "A cup of **courage**." |
| **High (→ 2)** | Unpredictable, chaotic | Uniform/flat distribution → confusion & unexpected outputs | "A cup of **stars**." |

Key Takeaways  

- At **low temperature**, the model almost always picks the most probable next word — great for factual, consistent tasks.
- At **mid temperature**, the model balances creativity and coherence — good for general use.
- At **high temperature**, probability gets spread nearly equally across all words, leading to surprising or even nonsensical outputs.

When to Use What  

- Use **low temperature** for: code generation, data extraction, Q&A
- Use **mid temperature** for: chatbots, summarization
- Use **high temperature** for: brainstorming, creative writing (with caution)

**Top-p (nucleus sampling)**  

Top-P is another parameter that controls the **randomness of the model's output**, but it works differently from temperature.

How it Works  

Instead of scaling probabilities (like temperature), Top-P **limits the pool of words** the model can choose from.

- The model ranks all possible next words by probability
- It then picks the **smallest group of top words** whose combined probability adds up to **P**
- It only samples from that group

Example  

Say the next word probabilities are:

| Word | Probability |
|---|---|
| coffee | 40% |
| courage | 25% |
| dreams | 20% |
| stars | 10% |
| chaos | 5% |

- At **Top-P = 0.85** → model considers {coffee, courage, dreams} (40+25+20 = 85%) and ignores the rest
- At **Top-P = 1.0** → model considers **all words** (no filtering)
- At **Top-P = 0.4** → model only considers {coffee} (very deterministic)

Top-p vs Temperature  

| | Temperature | Top-p |
|---|---|---|
| **Controls** | How sharp/flat the probability curve is | How many words are in the candidate pool |
| **Low value** | More deterministic | Fewer word choices |
| **High value** | More creative/random | More word choices |

On Claude's API  

```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    top_p=0.9,  # 👈 Set it here (0.0 to 1.0)
    messages=[
        {"role": "user", "content": "Your prompt here"}
    ]
)
```

> **💡 Tip:** Anthropic generally recommends using **either** temperature **or** Top-P, not both together, as combining them can produce unpredictable behavior.

**Top-k**  

Top-k is similar to Top-p but even simpler — it limits the word pool to a **fixed number of top candidates**, regardless of their probabilities.

How it Works  

- The model ranks all possible next words by probability
- It only considers the **top K words** and samples from those
- Everything outside the top K is ignored completely

Example  

Using the same word probabilities:

| Word | Probability |
|---|---|
| coffee | 40% |
| courage | 25% |
| dreams | 20% |
| stars | 10% |
| chaos | 5% |

- At **K = 3** → model only considers {coffee, courage, dreams} — always exactly 3 words
- At **K = 1** → model always picks {coffee} — completely deterministic (like greedy decoding)
- At **K = 5** → model considers all 5 words

Top-k vs Top-p vs Temperature  

| | Temperature | Top-p | Top-k |
|---|---|---|---|
| **Controls** | Sharpness of probability curve | Cumulative probability threshold | Fixed number of candidates |
| **Low value** | Deterministic | Fewer words | Fewer words |
| **High value** | Creative/random | More words | More words |
| **Pool size** | All words (scaled) | Varies dynamically | Always fixed |

The key difference from Top-p is that **Top-k is rigid** — it always picks exactly K words, even if the probability gap between word K and K+1 is huge.

On Claude's API  

```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    top_k=40,  # 👈 Set it here
    messages=[
        {"role": "user", "content": "Your prompt here"}
    ]
)
```

> **💡 Note:** Anthropic recommends using only **one** sampling parameter at a time — pick whichever suits your use case and leave the others at default.

Top-p  
For creative, diverse tasks  
Examples - Chatbots, Storytelling  

Top-k  
For predictable, structured tasks  
Examples - Writing Code, Summarization  

**Output Length**  

Output Length is a parameter, commonly called **`max_tokens`**.

What is a Token?  

Before diving in, it helps to understand tokens:

- A token ≈ **~¾ of a word** on average
- "A cup of coffee" ≈ **4 tokens**
- 1000 tokens ≈ **750 words**

How `max_tokens` Works  

It simply sets a **hard cap** on how many tokens the model can generate in its response. The model stops generating once it hits this limit — even mid-sentence.

On Claude's API  

```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,  # 👈 This one — you've already been setting it!
    messages=[
        {"role": "user", "content": "Your prompt here"}
    ]
)
```

Practical Guidelines  

| Use Case | Recommended `max_tokens` |
|---|---|
| Short Q&A / classification | 100–300 |
| Summarization | 300–600 |
| Chatbot responses | 500–1000 |
| Long-form writing / reports | 2000–4000 |
| Complex reasoning / agents | 4000+ |

Important Notes  

- It is a **maximum**, not a target — the model can stop earlier if it finishes naturally
- Setting it **too low** can cut off responses abruptly
- Claude's maximum allowed `max_tokens` depends on the model — for Claude Sonnet 4 it is **8192 tokens**
- More tokens = **higher API cost**, so set it appropriately for your use case

[⬆ Back to Top](#top)

---

## #9 What Exactly is a Token?

Tokenization is based on **subword units**, not whole words. Here's how it actually works:

| Text | Tokens | Count |
|---|---|---|
| "cat" | ["cat"] | 1 token |
| "coffee" | ["coff", "ee"] | 2 tokens |
| "unbelievable" | ["un", "belie", "vable"] | 3 tokens |
| "internationalization" | ["int", "ern", "ation", "al", "ization"] | 5 tokens |
| "A cup of coffee" | ["A", "cup", "of", "coff", "ee"] | 5 tokens |

So yes — **long words get split into multiple tokens**, and a token is roughly **3–4 characters** as you suspected.

Simple Rules of Thumb  

- Short common words → usually **1 token** ("the", "cat", "run")
- Long or rare words → **split into multiple tokens**
- Punctuation & spaces → often their **own token**
- Numbers like "12345" → can be **split digit by digit**

Why does this matter?  

```python
# This prompt might look short but could use many tokens
# if it contains long/technical/rare words
max_tokens=100  # might cut off sooner than you expect
```

Best Way to Check  

Anthropic has an official tokenizer tool you can use to see exactly how any text gets tokenized:

👉 [https://claude-tokenizer.vercel.app/](https://claude-tokenizer.vercel.app/)

Paste any text there and it will show you the exact token breakdown visually.

[⬆ Back to Top](#top)

---

## #10 Vector Databases

When you search  
"Calories in apple"  
"Revenue of apple"  

apple word is common but search results are different and relevant.  

> Embeddings are used for semantic search

Word Embedding  
Sentence Embedding  
Document Embedding  

Embeddings group together similar things.  

Embeddings are stored as vectors in Vector Database.  

OLTP Databases  
OLTP = Online Transaction Processing
Examples are - MySQL, PostgreSQL, MongoDB  
How data is stored?  
rows, columns

OLAP Databases  
OLAP = Online Analytical Processing  
Examples are - ClickHouse, Snowflake, Databricks, Apache Druid  
How data is stored?  
rows, columns

Vector Databases  
A vector database is a specialized system for storing, managing, and searching high-dimensional vector embeddings, allowing for semantic similarity search rather than exact keyword matches. By utilizing algorithms like Approximate Nearest Neighbor (ANN) (e.g., HNSW), they enable fast retrieval of unstructured data (text, images, audio) based on meaning.  
Examples are - Pinecone, Milvus, Chroma, Qdrant
How data is stored?  
id, vector and payload

References:  
* [What is a Vector Database?](https://qdrant.tech/articles/what-is-a-vector-database/)

[⬆ Back to Top](#top)

---

## #11 Todos/Exercises

#1  
Qdrant Hands-on

Install Qdrant using Docker

Initialise a demo app using `uv init`.

Install Qdrant Python Client.  

`uv init`  
`uv venv`  
`.\.venv\Scripts\activate`  
Install Python Dotenv package.  
Install Qdrant Python Client package.  
Install Sentence Transformer package.

What we are doing?  
Setup a local vector database.  
Then this vector database will store the embeddings.  
For embeddings we can use different models - like BERT, Da Vinci from OpenAI etc.  
And then we can do semantic search on this vector database.  

Create a collection in the vector database.

```python
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

qdrant_client = QdrantClient(host="localhost", port=6333)
model = SentenceTransformer("all-MiniLM-L6-v2")

DIMENSION = model.get_sentence_embedding_dimension()

print(DIMENSION)

def create_collection(name: str, distance: models.Distance):
    if client.collection_exists(collection_name=name):
        print(f'Collection {name} already exists.')
        return

    client.create_collection(
        collection_name=name,
        vectors_config=models.VectorParams(
            size=DIMENSION,
            distance=distance
        )
    )
    print(f'Collection {name} created successfully.')
```

Create collection in a very idempotent way,  
that means if a collection already exists then don't  
try to create it. It should not change the existing state.  

Perform CRUD operations.

Create and read a vector.

```python
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

client = QdrantClient(host="localhost", port=6333)
model = SentenceTransformer("all-MiniLM-L6-v2")

new_text   = "Elephants are the largest land animals on Earth."
new_vector = model.encode(new_text).tolist()

print(new_vector)

#CREATE
client.upsert(
    collection_name="my_collection",
    points=[
        models.PointStruct(
            id      = 0,
            vector  = new_vector,
            payload = {"text": new_text, "category": "animal", "role": "public"}
        )
    ]
)

print("Point 0 inserted.")

#READ
point = client.retrieve(
    collection_name="my_collection",
    ids=[0],
    with_payload=True,
    with_vectors=True
)
print(point)
```

Storing multiple points/vectors into the vector database.
Then perform semantic search.
Then filtering by exact match.

```python
# Sample Documents
documents = [
    {"id": 1, "text": "Dogs are loyal and friendly domestic animals.",
     "category": "animal", "role": "public"},

    {"id": 2, "text": "Cats are independent and curious creatures.",
     "category": "animal", "role": "public"},

    {"id": 3, "text": "Quantum computing uses qubits to perform complex calculations.",
     "category": "technology", "role": "admin"},

    {"id": 4, "text": "Machine learning enables computers to learn from data.",
     "category": "technology", "role": "public"},

    {"id": 5, "text": "The Milky Way galaxy contains over 200 billion stars.",
     "category": "science", "role": "public"},

    {"id": 6, "text": "Nuclear fusion is the process powering the sun.",
     "category": "science", "role": "public"},
]

texts = [doc['text'] for doc in documents]
vectors = model.encode(texts)

# Creating Points with Payload (Qdrant's Datastructure)
points = [
    models.PointStruct(
        id      = doc["id"],
        vector  = vectors[i].tolist(),
        payload = {
            "text"    : doc["text"],
            "category": doc["category"],
            "role"    : doc["role"],
        }
    )
    for i, doc in enumerate(documents)
]

operation_info = client.upsert(
    collection_name="my_collection",
    wait=True,
    points=points
)

print(f'Status: {operation_info.status}')

# Performing Semantic Search
query = "What animals make good pets?"
query_vector = model.encode(query).tolist()

results = client.query_points(
    collection_name="my_collection",
    query=query_vector,
    limit=3,
    #score_threshold=0.35
)

if not len(results.points):
    print('No results found')

for r in results.points:
    print(f"Score: {r.score:.4f} | {r.payload['text']}")

# Filtering by exact match
results = client.query_points(
    collection_name="my_collection",
    query=model.encode("computers and learning").tolist(),
    query_filter=Filter(
        must=[
            FieldCondition(
                key="category",
                match=MatchValue(value="technology")
            ),
        ]
    )
    limit=3
)

if not len(results.points):
    print('No results found')

for r in results.points:
    print(f"Score: {r.score:.4f} | {r.payload['text'][:60]}")

# Filtering with multiple conditions
# must = AND, should = OR, must_not = NOT
results = client.query_points(
    collection_name="my_collection",
    query=model.encode("astronomy and stars").tolist(),
    query_filter=Filter(
        must=[
            FieldCondition(
                key="category",
                match=MatchValue(value="science")
            ),
            FieldCondition(
                key="category",
                match=MatchValue(value="science")
            ),
        ]
    )
    limit=3
)

# Filtering points without query
# we can use scroll() to iterate through points without the need of a query

results, next_page_offset = client.scroll(
    collection_name="my_collection",
    scroll_filter=Filter(
        must=[FieldCondition(key="category", match=MatchValue(value="animal"))]
    ),
    limit=10,
    with_payload=True,
    with_vectors=False
)

print(f"Found {len(results)} animal points:")

for r in results:
    print(f"ID: {r.id}: {r.payload['text'][:50]}")
```

[⬆ Back to Top](#top)

---

## #12 Quizzes

Quiz #1  
What is the core mechanism that makes transformer models so effective for language tasks?  

Answer:  
Self-attention, which lets each token attend to every other token in the sequence.  

Quiz #2  
In LLM terminology, what is a "token"?  

Answer:  
A sub-word unit that the model uses to represent text.  

Quiz #3  
What is the core loop that defines Agentic AI behaviour?

Answer:  
Perceive, Reason, Act, Observe

Quiz #4  
In language modeling, the probability of a sequence of tokens t1, t2, ..., tn is computed as:  

Answer:  
The product of conditional probabilities of each token given the previous tokens.

Quiz #5  
What do "parameters" refer to in a 7-billion parameter LLM?

Answer:  
The learnable weights in the neural network that store the model's knowledge.

Quiz #6  
The original Transformer architecture mainly consists of which two components?

Answer:  
Encoder and Decoder

Quiz #7  
Word2Vec generates static embeddings. Which type of models generate contextual embeddings?

Answer:  
Transformer based models (e.g., BERT, GPT)

Quiz #8  
You want your LLM to produce deterministic, consistent output every time.  
What "temperature" value should you set?

Answer:  
A low value close to 0

Quiz #9  
What is a model's "context window"?

Answer:  
The maximum number of tokens the model can process in a single input + output

Quiz #10  
Why are traditional relational databases unsuitable for vector similarity search  
at scale?

Answer:  
They lack specialized indexing algorithms (like HNSW) for efficient nearest  
neighbour search

Quiz #11  
Why do we "chunk" large documents before embedding them?

Answer:  
Because embedding models have a maximum input token limit,  
and smaller chunks capture more focused meaning.

[⬆ Back to Top](#top)
