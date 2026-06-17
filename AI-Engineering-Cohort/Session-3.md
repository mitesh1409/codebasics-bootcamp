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

**Steps in RAG**

1. Ingestion: Preparing, embedding and storing the data
2. Retrieval: Finding relevant document to put in context
3. Generation: Prompting the LLM with retrieved context to generate grounded response

**What we are going to build?**

An HR Policies Chatbot, that can answer about Atliq AI's HR Policies using RAG.

Lets assume we have a company's HR policies document - "Atliq AI HR Policies Document".

---

### Step #1: Ingestion

Ingestion itself involves multiple steps:

1. **Loading** — the documents into a readable format
2. **Chunking** — splitting them into smaller chunks
3. **Embedding** — creating their embeddings using the embedding models
4. **Indexing** — storing the embeddings and payloads on the vector DB

### 1. Ingestion -> Loading

The first step is loading the document so that we can process it.

```python
# Loading the Document
import os
import requests

GITHUB_RAW_URL = "https://raw.githubusercontent.com/tnahddisttud/sample-doc/refs/heads/main/atliqai_hr_policies.txt"

def load_document(url: str) -> str:
    """Fetch a plain-text file from a raw GitHub URL."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

raw_text = load_document(GITHUB_RAW_URL)
print(f"Loaded {len(raw_text):,} characters")
print(raw_text[:400])  # Sanity check
```

### What this code does:

| Step | Code | Purpose |
|---|---|---|
| 1 | `requests.get(url, timeout=10)` | Fetches the raw file content from GitHub, times out after 10s |
| 2 | `response.raise_for_status()` | Throws an error if request failed (404, 500, etc.) |
| 3 | `return response.text` | Returns the file content as a plain string |
| 4 | `raw_text[:400]` | Prints first 400 characters as a quick sanity check |

> 💡 `raise_for_status()` is a good practice — without it, a failed request (like a typo'd URL) would silently return an error page as text instead of raising an exception.

### 2. Ingestion -> Chunking

It's an essential preprocessing step where we break down large documents into smaller, manageable, and semantically meaningful text segments.

It optimizes RAG by ensuring retrieval accuracy, fitting content into LLM context windows, and reducing retrieval time.

### Flow Summary

| Step | Input | Output |
|---|---|---|
| 1. Split | Document | Chunk 1, Chunk 2, Chunk 3 |
| 2. Embed | Each chunk | Chunk embeddings (vectors) |
| 3. Store | Chunks (as payload) + embeddings | Vector DB |

Chunking Techniques

* Recursive Text Splitting
* Hierarchical Chunking
* Semantic Chunking

Recursive Text Splitting Example

```python
CHUNK_SIZE = 50

def parse_word_chunks(text: str, chunk_size: int = CHUNK_SIZE) -> list[dict]:
    # Strip markdown heading symbols and blank lines
    clean_lines = []
    for line in text.splitlines():
        line = line.strip().lstrip("#").strip()
        if line:
            clean_lines.append(line)

    # Join everything into one word list and slice
    words = " ".join(clean_lines).split()

    chunks = []
    for i in range(0, len(words), chunk_size):
        content = " ".join(words[i : i + chunk_size])
        chunks.append({
            "chunk_index": len(chunks),
            "content": content,
        })

    return chunks

chunks = parse_word_chunks(raw_text)
print(f'Total chunks = {len(chunks)}')
```

### What this code does:

**Step 1 — Clean the text:**
```python
line.strip().lstrip("#").strip()
```
- Removes leading/trailing whitespace
- Strips markdown `#` heading symbols (e.g. `"# Introduction"` → `"Introduction"`)
- Skips blank lines entirely

**Step 2 — Flatten into words:**
```python
words = " ".join(clean_lines).split()
```
- Joins all cleaned lines into one string, then splits into a flat list of words

**Step 3 — Chunk by word count:**
```python
for i in range(0, len(words), chunk_size):
    words[i : i + chunk_size]
```
- Slides a window of `chunk_size` words (default 50) across the word list
- Each chunk becomes a dict with `chunk_index` and `content`

### Example Output:
```python
[
    {"chunk_index": 0, "content": "first 50 words..."},
    {"chunk_index": 1, "content": "next 50 words..."},
    ...
]
```

> 💡 This is **word-count based chunking** — simple and fast, but doesn't respect sentence/paragraph boundaries. More advanced chunking strategies (e.g. semantic chunking, recursive splitting) try to avoid cutting mid-sentence.

> Chunking is also called Text Segmentation

> 50-250 is considered a good chunk size

```python
def build_chunk_text(chunk: dict) -> str:
    return chunk["content"]
```

### Ingestion -> Embedding

```python
from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
embedder = SentenceTransformer(EMBEDDING_MODEL)

# Extract Chunk Texts
chunk_texts = [build_chunk_text(c) for c in chunks]

print(f"Embedding {len(chunk_texts)} chunks ...")
embeddings = embedder.encode(chunk_texts, show_progress_bar=True)

print(f"Shape: {embeddings.shape}")
```

### Ingestion -> Indexing

Connect to Qdrant cluster and create a collection.

```python
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance, VectorParams, PointStruct,
    Filter, FieldCondition, MatchValue,
)

# "path" = no server needed for demos
# Production use: QdrantClient(url="http://localhost:6333")
client = QdrantClient(path="/tmp/langchain_qdrant")

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
```

Saving embeddings into the collection.

```python
# Creating Points
points = [
    PointStruct(
        id=idx,
        vector=embedding.tolist(),
        payload={
            "content": chunk["content"],
        },
    )
    for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings))
]

result = client.upsert(
    collection_name=COLLECTION_NAME,
    points=points,
    wait=True,  # Block until indexing completes before returning
)
print(f"Indexed {len(points)} points — status: {result.status}")

info = client.get_collection(COLLECTION_NAME)
print(f"Points     : {info.points_count}")
print(f"Dimensions : {info.config.params.vectors.size}")
```

---

### Step #2: Retrieval

We will retrieve the relevant chunks.

Retrieval is same as a semantic search.

Retrieval has the following steps:

1. Get user query/question
2. Generate embedding of it
3. Search into Vector DB using this embedding
4. Get relative chunks/vectors

```python
def retrieve(
    query: str,
    top_k: int = 5
) -> list[dict]:
    """
    Embed the query and return the top-k most similar chunks.

    Args:
        query         : User's question.
        top_k         : Number of chunks to return.
        section_filter: Optional H2 heading to restrict the search scope.
    """

    query_vector = embedder.encode(query).tolist()

    hits = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k,
        with_payload=True,
    )

    return [{**hit.payload, "score": round(hit.score, 4)} for hit in hits.points]

results = retrieve("What is the leave policy", top_k=3)
for r in results:
    print(f"[score={r['score']}]")
    print(f"  {r['content'][:200]}...\n")
```

The purpose of the Retrieval step is to retrieve relevant chunks/data from the knowledge base.  
Where knowledge base might have one or multiple databases of different kinds, documents, files etc.  

---

### Step #3: Generation


---

Ingestion step is the most important and the longest step in RAG pipeline.
Quality of embedding depends on - chunk size, embedding model etc. factors.

Retrieval step is simple.

---

### RAG Pipeline

1. Ingestion: Preparing, embedding and storing the data
2. Retrieval: Finding relevant document to put in context
3. Generation: Prompting the LLM with retrieved context to generate grounded response

Step #1 Ingestion

Ingestion -> reading data, chunking, embedding and storing into the Vector DB.

Prepares knowledge base into Vector DB. So that we can perform semantic search on it.

1. **Loading** — loading data from the data source - Excel, PDF, SQL Database etc.
2. **Chunking** — splitting them into smaller chunks
3. **Embedding** — creating their embeddings using the embedding model
4. **Indexing** — storing the embeddings and payloads on the vector DB

Step #2 Retrieval

Retrieval -> user query, embedding, searching Vector DB using this embedding and getting relative chunks/vectors.

Semantic search on knowledge base or Vector DB. This context is then passed to LLM to get final response.

1. Get user query/question
2. Generate embedding of it
3. Search into Vector DB using this embedding
4. Get relative chunks/vectors

Step #3 Generation

We pass the following prompt to LLM:

```
{
    System Prompt
        +
    Question/Query
        +
    Context retrieved from the knowledge base (Retrieval step)
}
```

```
SYSTEM_PROMPT = """You are a helpful HR assistant.
Answer the user's question using ONLY the context provided below.
If the context does not contain enough information, say so — do not make things up.
Always cite the section name when referencing specific information."""
```

```python
def build_context(retrieved_chunks: list[dict]) -> str:
    parts = []
    for i, chunk in enumerate(retrieved_chunks, 1):
        parts.append(f"[Source {i}]\n{chunk['content']}")
    return "\n\n---\n\n".join(parts)
```

```python
from groq import Groq

groq_client = Groq()  # Reads GROQ_API_KEY from environment automatically
GROQ_MODEL  = "openai/gpt-oss-safeguard-20b"

def rag(query: str, top_k: int = 5):
    """
    End-to-end RAG pipeline:
      1. Retrieve relevant chunks from Qdrant
      2. Format them as a context block
      3. Send context + query to Groq and return the answer
    """

    # Step 1 — Retrieve
    chunks = retrieve(query, top_k=top_k)
    if not chunks:
        return "No relevant content found in the document."

    # Step 2 — Build context
    context = build_context(chunks)

    # Step 3 — Generate
    user_message = f"Context:\n{context}\n\nQuestion: {query}"

    response = groq_client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_message},
        ],
        temperature=0.2,   # Low = factual; High = creative
    )

    return response.choices[0].message.content, context

answer, context = rag("What are the main topics covered in this document?")
print(answer)
print(f"{250*'='}")
print(f"\n\nSOURCES:\n {context}")
```

---

## #N Quizzes

Quiz #1  
Traditional DB vs Vector DB  

What is the key difference between a Traditional Database (e.g. MySQL) and a Vector Database (e.g. Qdrant)?  

Answer:  
Traditional DBs match exact values; Vector DBs match by semantic similarity  

Key Takeaway  
The fundamental difference isn't speed — it's the **matching mechanism**:
- **Traditional DBs (MySQL)** → exact value matching (`WHERE id = 5`)
- **Vector DBs (Qdrant)** → semantic similarity matching (finds conceptually similar items, even with different exact wording)

---

Quiz #2  
RAG Acronym  

Which of the following is the correct definition of the acronym RAG?  

Answer:  
- Randomly Asking Google
- Recursive Attention Gateway
- Response-Aligned Grounding
- **Retrieval-Augmented Generation** ✅

Key Takeaway  
**RAG = Retrieval-Augmented Generation** — the LLM's generation is "augmented" with content retrieved from an external knowledge source (like a vector database) before producing an answer.

---

Quiz #3  
Dense Numerical Representation in RAG  

In a RAG pipeline, what do we call the dense numerical representation that captures a text's meaning relative to its surrounding context?

Answer:  
- **A contextual embedding** ✅
- A semantic hash
- A digital horoscope for words
- A token index

Right Answer: A contextual embedding - why?  
A **contextual embedding** is a dense vector representation of text where the meaning is captured **relative to the surrounding context** — this is exactly what we've covered earlier (e.g. `model.encode()` converting text into a vector that captures semantic meaning).

---

Quiz #4  
Primary Problem RAG Solves  

What is the primary problem that RAG aims to solve in Large Language Models?  

Answer:  
RAG primarily solves the problem of LLMs being limited to their **static, pre-trained knowledge** — they can't access up-to-date, private, or domain-specific information, and tend to **hallucinate** when asked about things outside their training data. RAG fixes this by retrieving relevant external context at query time and grounding the LLM's answer in that real data.

---

Quiz #5  
Why Chunk Large Documents for RAG  

Why do we typically "chunk" large documents (like a 100-page PDF) before storing them for RAG?  

Answer:  
Chunking large documents serves multiple purposes:  
- **Fits content into LLM context windows** — a 100-page PDF as one block would exceed the model's input limit
- **Improves retrieval accuracy** — smaller, semantically focused chunks let the vector search return precisely relevant sections instead of vague whole-document matches
- **Reduces retrieval time** — searching/embedding smaller units is faster and more efficient

---

Quiz #6  
Role of Vector Database in RAG  

What role does the Vector Database (like Qdrant) play in RAG?  

Answer:  
The Vector Database stores the **embeddings (vectors) and payloads** of document chunks, and enables **fast semantic similarity search** — when a user asks a question, the query is embedded and the Vector DB retrieves the most relevant chunks to pass to the LLM as context.

---

Quiz #7  
How Vector DB Determines Relevant Chunks  

In a RAG system, how does the vector database determine which stored chunks are most relevant to a user's query?  

Answer:  
The query is converted into an embedding (vector), and the vector database compares this query vector against all stored chunk vectors using a **similarity metric** (commonly **cosine similarity**). The chunks with the highest similarity scores are returned as the most relevant results.

---

Quiz #8  
What Happens After Retriever Finds Chunks  

What happens immediately after the Retriever finds the most relevant document chunks?  

Answer:  
Immediately after retrieval, the chunks are **formatted into a context block** and then **combined with the user's query** to form the prompt — this combined prompt (System Prompt + User's Query/Question + Context retrieved from the knowledge base) is sent to the LLM to generate the final answer.

```
Retrieve chunks → Build context → Send (system prompt + query + context) to LLM → Generate answer
```

---

Quiz #9  
Role of an Embedding Model in RAG  

In a RAG application, what is the role of an Embedding Model?  

Answer:  
The Embedding Model converts text (documents, chunks, or the user's query) into **dense numerical vectors** that capture semantic meaning. This allows the system to compare text mathematically — measuring similarity between the query and stored chunks — rather than relying on exact keyword matching.

```
Text  →  Embedding Model  →  Vector (e.g. [0.2, -0.5, 0.8, ...])
```

---

Quiz #10  
Well-Prompted RAG Agent with No Answer in Context  

If a user asks a question, but the retrieved documents do not contain the answer, what should a well-prompted RAG agent do?  

Answer:  
A well-prompted RAG agent should **honestly state that the context does not contain enough information to answer the question**, rather than guessing or making something up. This directly matches the instruction from earlier: *"If the context does not contain enough information, say so — do not make things up."*

This is the core defense against **hallucination** in RAG systems.

---

## #N How does search work in Vector DB?

Suppose there are 1-10 million vectors in the Vector DB.  

Now performing search operation on it - consine similarity search.  

How do they do it efficiently?  

HNSW - Highly Navigable Small World  
This algorithm is used for efficient search and retrieval.  

---

## #N How to handle updates in the knowledge base?

Initially we started with v1 of the document, chunked, embedded and stored in Vector DB.  

Later on we got v2 of the document with some updates.  
How do we handle it?  

We can filter the chunks that needs to be updated using meta-data filtering.  
That way we can identify and update the required chunks.  

---

## #N RAG and the security of the data

Scenario: We have a confidential IP protected data, passing it to LLM as part of RAG pipeline,  
would LLM retrain and use it for other work?  

Cloud providers will provide you this protected private environment.  
So your data will be protected.  

Some clients don't trust this cloud providers - Microsoft Azure, AWS etc.  

It is possible to host LLM on your own server.  
We can host LLM on a server which is located in the same country.  
So data won't leave outside the country.  
Also since LLM is hosted on a server, it has no connection to the outside world, it cannot be retrained.  

---

## #N What size is good for chunking? Which is better big chunks or small chunks?

Smaller chunks are better as they:  
- retrieval accuracy -> we get better results from LLM
- cost effective as they consume less number of tokens
