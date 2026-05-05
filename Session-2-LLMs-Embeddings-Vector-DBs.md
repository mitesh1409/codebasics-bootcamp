# Session 2: LLMs, Embeddings & Vector DBs

Mar 8 2026  

Topics

1. Generative AI
2. AI Agent
3. Software 1.0 Software 2.0 Software 3.0
4. Follow Andrej Karpathy
5. Gen AI (LLM only) Vs AI Agent Vs Agentic AI
6. What exactly are LLMs?

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

For example

Input:  
Roses are red...  
Output:  
Violets are blue... (higher probability of getting this)

Input:  
I am feeling hungry, I need...  
Output:  
foo  
OR  
something to eat  
etc. (higher probability of getting this)


Google's Word2Vec


Transformer Explainer  

https://github.com/poloclub/transformer-explainer

https://poloclub.github.io/transformer-explainer/


## Key Parameters

Key Parameters

* Context Window
* Temperature
* Top-p & Top-k
* Output Length

Context Window  
Maximum number of tokens that can be passed at a time for inference.  

Prompt:  
teach me a philosophy of non-attachment  

Total number of tokens = 7  
Context utilized = 7  



## Quiz

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
