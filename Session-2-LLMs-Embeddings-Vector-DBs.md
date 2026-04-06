# Session 2: LLMs, Embeddings & Vector DBs

Mar 8 2026  

## Generative AI

Generative AI is a type of artificial intelligence that creates new content -  
such as text, images or audio - based on patterns learned from existing data.  

ChatGPT -> Application that uses LLM GPT-5
GPT-5 -> LLM

Claude -> Application that uses LLM Sonnet 4.6
Sonnet 4.6 -> LLM

LLM is the brain.  
Application is the body which needs a brain.  

So as an AI engineer we will build applications that will use LLM as their brain.  

## AI Agent

AI Agent is a program that takes input, thinks and acts to complete a task using  
tools, memory and knowledge.  

AI Agent = LLM + Tools + Knowledge + Memory

AI Agents are autonomous but narrow, task specific and does not span multiple or evolving goals.  

Agentic AI is a system where one or more AI agents work autonomously,  
often over long tasks, making decisions, using tools and even other agents to reach a goal.

## LLM

Language Modeling  
A language model is a probability distribution over a sequence of tokens (words/sub-words).

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
