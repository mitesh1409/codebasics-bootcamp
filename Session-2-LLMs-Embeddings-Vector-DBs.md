# Session 2: LLMs, Embeddings & Vector DBs

Mar 8 2026  

Topics

1. Generative AI
2. AI Agent
3. Software 1.0 Software 2.0 Software 3.0
4. Follow Andrej Karpathy
5. Gen AI (LLM only) Vs AI Agent Vs Agentic AI
6. What exactly are LLMs?
7. Transformers
8. Key Parameters
9. What Exactly is a Token?
10. Vector Databases

7. Todos/Exercises
8. Quizzes

---

## #1 Generative AI

Generative AI is a type of artificial intelligence that creates new content -  
such as text, images or audio - based on patterns learned from existing data.  

ChatGPT -> Application that uses LLM GPT-5
GPT-5 -> LLM

Claude -> Application that uses LLM Sonnet 4.6
Sonnet 4.6 -> LLM

LLM is the brain.  
Application is the body which needs a brain.  

LLMs are trained on vast amount of data (source: internet or other?),  
then they do a reinforcement learning with human feedback RLHF.

So as an AI engineer we will build applications that will use LLM as their brain.  

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

---

## #3 Software 1.0 Software 2.0 Software 3.0

[Karpathy's 3 Software Paradigms Expanded](https://kanaka.github.io/blog/karpathy-software-paradigms-expanded/)

---

## #4 Follow Andrej Karpathy

* [Andrej Karpathy | YouTube](https://www.youtube.com/@AndrejKarpathy)
* [Andrej Karpathy | X](https://x.com/karpathy)

---

## #5 Gen AI (LLM only) Vs AI Agent Vs Agentic AI

Here's the markdown table extracted from the screenshot:

| System Type | Gen AI (LLM-only) | AI Agent | Agentic AI |
|---|---|---|---|
| **Task Capability** | Answers based on pre-trained knowledge only | Takes input, decides, and completes a task | Handles multi-step goals with planning and coordination |
| **Tool Usage** | ❌ No external tools | Uses tools to complete a task | Uses multiple tools, may call other agents |
| **Autonomous Decisions** | ❌ No decision-making | ✅ Makes decisions to complete the task | ✅ Plans, decides, and adapts over time |

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


---

## Quizzes

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

Answer:  

Quiz #8  

Answer:  

Quiz #9  

Answer:  

---

**inference**  
An inference is a logical conclusion or "educated guess" made by combining evidence, observations, or clues with your own background knowledge. It is the process of figuring out something that is not directly stated, acting as a bridge between known facts and new understanding.
