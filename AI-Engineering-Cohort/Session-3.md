<a name="top"></a>

# Session 3: RAG Fundamentals & Building a RAG Pipeline

Mar 14, 2026

## Topics

* [#1 RAG](#1-rag)
* [#N Todos/Exercises](#11-todosexercises)
* [#N Quizzes](#12-quizzes)

---

## #1 RAG

**RAG** stands for **Retrieval-Augmented Generation**. The core idea: instead of relying only on what an LLM memorized during training, you first *fetch* relevant context from an external source, then *generate* a response using that context.

**The problem it solves**: LLMs have a knowledge cutoff and no access to your private data. RAG bridges that gap.

**The flow in simple terms:**

1. User asks a question
2. System searches a knowledge base for relevant chunks
3. Those chunks are injected into the LLM prompt
4. LLM answers *using that fresh context*---

**Real-life examples:**

**Customer support bots** — A company uploads its product manuals, FAQs, and policies to a vector DB. When a customer asks "How do I reset my device?", the bot retrieves the exact manual section and answers accurately — without hallucinating.

**Legal & compliance tools** — Law firms use RAG to let lawyers query thousands of case files. "Show me past rulings on IP infringement in software" → retrieves relevant case summaries → LLM drafts an analysis.

**Internal enterprise search** — Companies like Notion, Confluence, or Slack-integrated tools use RAG so employees can ask "What was decided in last quarter's product review?" and get answers pulled from actual meeting notes.

**Medical assistants** — Clinical decision support tools retrieve from medical literature or patient records before answering "What's the recommended dosage for X in a diabetic patient?"

**Code assistants** — GitHub Copilot Chat retrieves from your own codebase before answering "How is authentication implemented here?"

---

**How it's used in industry:**

| Layer | What's used |
|---|---|
| Chunking | Split docs into ~512 token chunks |
| Embedding | OpenAI `text-embedding-3`, `all-MiniLM-L6-v2`, etc. |
| Vector store | Qdrant, Pinecone, Weaviate, pgvector |
| Retrieval | ANN search (HNSW) → top-k most similar chunks |
| Generation | GPT-4, Claude, Llama → reads chunks + answers |

The key insight: **the LLM stays frozen — only what you feed it changes.** That's what makes RAG cheaper and more controllable than fine-tuning.

### RAG Pipeline (Retrieval-Augmented Generation)

```
① Query → ② Retrieve → ③ Generate → ④ Answer
```

### Simple example - What problem RAG solves?

https://economictimes.indiatimes.com/industry/renewables/fueling-demand-inside-indias-ethanol-mobility-revolution-in-reverse/articleshow/131650947.cms

This article is posted on: Jun 11, 2026, 02:05:00 PM IST

Ask Gemini to summarize this article and highlight key pointers at the end.

Even though it is a latest article, Gemini is able to do this job because we provided the knowledge base.

Knowledge Base = external or internal, private or public, text, images, pdf, excel, audio, video etc.

Here in this simple example the knowledge base was small, a URL, but it can be very huge/big such that it cannot be fit into the context window.

Every LLM has a context window limit.
Beyond that limit it won't be able to answer the question or do its job.

Vector Databases have the ability to do "Semantic Search".
Semantic Search = Searching by meaning, not by matching exact text/keywords

### Benefits of RAG

- Reduced token cost due to small context
- Helps maintain data privacy
- Less chance of hallucination. Ground the answers with legit sources.
- Helps to provides up-to-date knowledge

### Architecture of RAG Based Gen AI Application

## RAG Based Gen AI Application

### Architecture

```

[Data Sources]
+-------------+            +-----------+             +-------+            [User]
| Excel files |            |           |             |       |   <-----   Question
| PDF files   |   ----->   | Vector DB |   <----->   |  LLM  |
| SQL DB      |            |           |             |       |   ----->   Answer
+-------------+            +-----------+             +-------+

```

### How it Works

1. **Ingest** — Documents (Excel, PDF, SQL) are converted to vectors and stored in Vector DB
2. **Query** — User asks a question → LLM searches Vector DB for relevant context
3. **Retrieve** — Vector DB returns the most similar/relevant chunks back to LLM
4. **Answer** — LLM uses retrieved context to generate a precise answer

### Why RAG?

Without RAG, an LLM only knows what it was trained on. RAG lets you **plug in your own private data** (company docs, PDFs, databases) so the LLM can answer questions about it — without retraining the model.

### How LLMs Produce Results in Case of RAG

To produce results LLMs can use:

* Context + LLM's own knowledge
* Context only

**Both options are partially correct** — it depends on how you design the prompt.

---

### What actually happens in RAG:

The retrieved context from Vector DB is **injected into the prompt** sent to the LLM:

```
Prompt to LLM:
"Answer the question using the context below.

Context:
{retrieved chunks from Vector DB}

Question: {user's question}
Answer:"
```

So the LLM **always uses its trained knowledge** (grammar, reasoning, language understanding) — but what controls the *answer content* is how you write the prompt.

---

### It's your choice as a developer:

| Approach | How | When to Use |
|---|---|---|
| **Only use provided context** | Add `"Answer only from the context. If not found, say I don't know."` | Private/sensitive data, factual accuracy critical |
| **Use both** | Don't restrict — let LLM blend context + its own knowledge | General assistants, broader Q&A |

---

### Simple Rule of Thumb

```
RAG without restriction  →  Context + LLM's own knowledge
RAG with restriction     →  Context only
```

> 💡 In most **enterprise/private data** RAG apps (e.g. "chat with your PDF"), you'd restrict to context only — otherwise the LLM might hallucinate answers from its training data that contradict your documents.

---

### Flow

```
[User]          [Retriever]          [LLM]           [Answer]
asks a    →    converts query   →   reads context  →  grounded
question       to embedding,        + generates
               searches             answer
                    ↑
               [Knowledge Base]
               Docs, PDFs, DBs
               (top-k chunks)
```

---

### Steps

| Step | Component | What happens |
|------|-----------|--------------|
| ① | User | Asks a question |
| ② | Retriever | Converts query to embedding, searches knowledge base, returns top-k chunks |
| ③ | LLM | Reads retrieved context + generates a grounded answer |
| ④ | Answer | Returned to the user, grounded in real data |

---

### Industry Stack

| Layer | Tools / Examples |
|-------|-----------------|
| Chunking | Split docs into ~512 token chunks |
| Embedding | OpenAI `text-embedding-3`, `all-MiniLM-L6-v2` |
| Vector store | Qdrant, Pinecone, Weaviate, pgvector |
| Retrieval | ANN search (HNSW) → top-k most similar chunks |
| Generation | GPT-4, Claude, Llama → reads chunks + answers |

---

## #N Todos/Exercises

@todo
Transformers lets you capture the contextual meaning of a word.
It uses "attention mechanism".

---

@todo
Static Embedding
Contextual Embedding
Dense numeric presentation/Dense Vectors/Dense Embeddings
Sparse numeric presentation

Word Embedding
Sentence Embedding
Doc Embedding

---

@todo

Explore
https://colab.research.google.com

https://excalidraw.com

---

@todo

Download and load the Embedding Model.

What is an Embedding Model?
It is a model that coverts text (or any other data) to fixed length numerical vectors (1D arrays) that capture the semantic meaning of the input text (or data).

We are going to use the Sentence Transformer library by HuggingFace which allows us to download and use opensource embedding models from HuggingFace.

HuggingFace is like the GitHub of AI, where the AI community collaborates on models, datasets, and applications.

`pip install -q qdrant-client sentence-transformers`

```python
from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = "all-MiniLM-L6-V2"
embedder = SentenceTransformer(EMBEDDING_MODEL)

# Example Documents
docs = [
    "Dogs are loyal and friendly domestic animals.",         # text_1
    "Cats are independent and curious creatures.",           # text_2
    "The Milky Way galaxy contains over 200 billion stars.", # text_3
]

# Creating Embedding
embedding = embedder.encode(docs)
embedding.shape
# Output: (3, 384)

# Creating Embedding of the "Query" text.
query = "What animals make good pets?"
query_embedding = embedder.encode(query)

# Calculate "Similarity" between text_1 & query
score_1 = embedder.similarity(query_embedding, embedding[0])
score_1
# Output: tensor([[0.5665]])

# Calculate "Similarity" between text_2 & query
score_2 = embedder.similarity(query_embedding, embedding[1])
score_2
# Output: tensor([[0.3954]])

# Calculate "Similarity" between text_3 & query
score_3 = embedder.similarity(query_embedding, embedding[2])
score_3
# Output: tensor([[0.0029]])
```

---

@todo

0 Dimension -> 3.14 -> Scaler
A single value

1 Dimension -> [1.1, 2.1, 3.1, ...] -> Vector
A list of values

2 Dimention -> [[1, 2, 3], -> Matrix
                [4, 5, 6],
                [7, 8, 9]]
A two-dimension array OR an array of arrays

More than 2 Dimension -> Tensor

Above is almost correct, but there's one inaccuracy: **Tensor** is actually the overarching term that covers *all* of the above.

Here's the corrected picture:

| Name | Dimensions | Example |
|---|---|---|
| Scalar | 0D | `5` |
| Vector | 1D | `[1, 2, 3]` |
| Matrix | 2D | `[[1,2], [3,4]]` |
| Tensor | **any** (0D, 1D, 2D, 3D+) | all of the above |

So a scalar *is* a tensor, a vector *is* a tensor, a matrix *is* a tensor. "Tensor" is the general term — it doesn't start at 3D.

In practice though (especially in ML/NumPy conversations), people often use "tensor" colloquially to mean *specifically* 3D or higher, just to distinguish it from the named types. That's where the confusion comes from. But technically, the definition is **any n-dimensional array**.

In NumPy, everything is an `ndarray` — a scalar is `ndim=0`, a vector is `ndim=1`, a matrix is `ndim=2`, and so on. PyTorch and TensorFlow call them all `Tensor` regardless of rank, which reflects the correct definition.

---

@todo

Traditional Databases - MySQL, PostgreSQL etc.

Lets take a simple example - we have a "books" table.

books table with following fields:
- id
- title
- category
- content

Now if we want to search books by a category then we can write a query like:

```sql
SELECT id, title
FROM books
WHERE category = 'Health';
```

But what if we want to search books that talk about "travelling to other planets".

Here we want to query database using natural language, not by exact category or title or words.

We may try the following query:

```sql
SELECT id, title
FROM books
WHERE content LIKE "%travelling to other planets%";
```

But the problem is it will do exact text search, it cannot search by meaning or semantic search.
Because of this we may not get the desired output.

This is the problem with traditional databases - they cannot perform semantic search because they are not developed that way. They don't have that feature.

Solution is to use Vector Databases like Qdrant that stores books data into the form of vectors and then we can perform semantic search on it.

So we will have books table:

- id <-- id of the point
- vector <-- contains embedded data (word/sentence/doc embeddings)
- payload <-- contains raw actual data

---

@todo

Hands-on: Vector DB

### What is a Vector Database?

A vector database is a specialized storage system designed to **manage, index, and query high-dimensional vector embeddings**.

### What is Qdrant?

Qdrant is an **OpenSource, high performance vector database**. It specializes in storing, and searching high-dimensional vectors, like those generated by AI models, along with associated metadata (payloads).

### Key Qdrant Concepts

| Concept | Description |
|---|---|
| **Collections** | Groups of points — like a table in SQL |
| **Points** | Each entry consisting of `idx + vector + payload` |
| **Payload** | Metadata stored alongside the vector (e.g. species, URL, color) |
| **Distance Metrics** | Euclidean Distance, Dot Product (and Cosine from earlier) |

### Supported Client SDKs

Qdrant can be accessed programmatically via:

- Python
- Rust
- Go
- TypeScript

### What is a Collection?

In Qdrant, a collection is a **named, logical container** that stores a set of related data points, which consist of:
- **Vectors**
- **Optional metadata (payloads)**

It serves a similar purpose to a **table in a traditional MySQL database**.

### Quick Analogy

| MySQL | Qdrant |
|---|---|
| Database | Qdrant instance |
| Table | Collection |
| Row | Point |
| Columns | Payload fields |
| Primary Key | Point ID |

### What is a Point?

Qdrant stores data in an entity called `point`. A point is a record consisting of a **vector** and an **optional payload** (similar to a row in MySQL).

---

### Structure of a Point

```
Point = id + [vector dimensions...] + payload
```

| Field | Type | Description |
|---|---|---|
| `id` | integer/uuid | Unique identifier for the point |
| `vector` | list of floats | The embedding — many numbers representing meaning |
| `payload` | dict | Optional metadata stored alongside the vector |

---

### Real Example — Books Collection

| book_id (id) | title (payload) | category (payload) | book_text (payload) | vector |
|---|---|---|---|---|
| 1 | Space Journey | science fiction | A crew travels across galaxies to discover new planets | [0.12, -0.44, 0.88, ...] |
| 2 | The Silent Forest | mystery | A detective investigates strange disappearances in a... | [-0.33, 0.91, 0.04, ...] |

---

### Key Takeaway

```python
models.PointStruct(
    id      = 1,                          # → book_id
    vector  = [0.12, -0.44, 0.88, ...],   # → embedding of book_text
    payload = {                           # → all other columns
        "title"    : "Space Journey",
        "category" : "science fiction",
        "book_text": "A crew travels across galaxies..."
    }
)
```

### Code Example

```python
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance, VectorParams, PointStruct,
    Filter, FieldCondition, MatchValue
)

EMBEDDING_MODEL = "all-MiniLM-L6-V2"
embedder = SentenceTransformer(EMBEDDING_MODEL)

# "path" = no server needed for development
# Production use: QdrantClient(url="http://localhost:6333")

# Connecting to a local instance
client = QdrantClient(path="/tmp/my_qdrant")

# Creating a Collection
COLLECTION_NAME = "docs"
DIM = embedder.get_sentence_embedding_dimension()

client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(
        size=DIM,
        distance=Distance.COSINE,
    ),
)

print("Collection created.")
# Output: Collection created.

# Example Documents
docs = [
    "Dogs are loyal and friendly domestic animals.",         # text_1
    "Cats are independent and curious creatures.",           # text_2
    "The Milky Way galaxy contains over 200 billion stars.", # text_3
]

# Creating points to store in the vector db
points = [
    PointStruct(
        id=idx,
        vector=embedding[idx].tolist(),
        payload={
            "text": docs[idx]
        },
    )
    for idx, doc in enumerate(docs)
]

# bulk inserting the points
response = client.upsert(
    collection_name=COLLECTION_NAME,
    points=points,
    wait=True,
)

response.status
# Output: <UpdateStatus.COMPLETED: 'completed'>
```

### What `wait=True` means in the `client.upsert() method`:
```python
wait=True   # ✅ Synchronous — confirms all points are written before moving on
wait=False  # ⚡ Asynchronous — faster but doesn't guarantee write is complete
```

> 💡 Always use `wait=True` in learning/dev environments so you can be sure data is ready before querying it.

### Querying Demo

```python
# Querying Demo
query     = "What animals make good pets?"
query_vec = embedder.encode(query).tolist()

results = client.query_points(
    collection_name=COLLECTION_NAME,
    query=query_vec,
    limit=3,
    #score_threshold=0.30  # You can limit the relevant results by their score
)

for r in results.points:
    print(f"Score: {r.score:.4f} | {r.payload['text']}")

# Output:
# Score: 0.5665 | Dogs are loyal and friendly domestic animals.
# Score: 0.3954 | Cats are independent and curious creatures.
# Score: 0.0029 | The Milky Way galaxy contains over 200 billion stars.
```

### What this code does:

**Step 1 — Encode the query:**
```python
query_vec = embedder.encode(query).tolist()
# Converts the question into a 384-dim vector
```

**Step 2 — Search Qdrant:**

| Parameter | Value | Purpose |
|---|---|---|
| `collection_name` | `COLLECTION_NAME` | Which collection to search |
| `query` | `query_vec` | The vector to find similar points for |
| `limit` | `3` | Return top 3 most similar results |
| `score_threshold` | `0.30` (commented out) | Only return results above this similarity score |

**Step 3 — Print results:**
```python
r.score          # similarity score (0 to 1)
r.payload['text'] # original text stored in payload
```

### Output Explained:

| Score | Text | Meaning |
|---|---|---|
| **0.5665** | Dogs are loyal... | Most similar — dogs are pets ✅ |
| **0.3954** | Cats are independent... | Related — cats are pets ✅ |
| **0.0029** | The Milky Way... | Almost 0 — completely unrelated ❌ |

> 💡 The commented `score_threshold=0.30` would filter out the Milky Way result automatically since `0.0029 < 0.30` — useful in production to avoid returning irrelevant results.

---

@todo

Benchmark of Embedding Models.

https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

HuggingFace > Embedding Leaderboard
https://huggingface.co/spaces/mteb/leaderboard

Which model to use for your project/app?
It depends on different factors, cost, the problem you are trying to solve etc.
We can ask ChatGPT, Claude, Gemini in selecting the right model.

OpenAI > Vector embeddings
https://developers.openai.com/api/docs/guides/embeddings

---

@todo

## #1 RAG

This comes here.

---

@todo

RAG Hands-on.

**What is RAG?**
RAG is the technique of grounding model's responses by letting them retrieve real time data from knowledge bases. It is used to make AI more personalized and reliable.

**Why do we need RAG?**
> LLMs are frozen in time, since they have a specific knowledge cut-off date.

They know nothing about your private documents/data or anything past their training/knowledge cut-off date.
RAG (Retrieval Augmented Generation) solves this by giving the model a reference knowledge to consult before answering.
