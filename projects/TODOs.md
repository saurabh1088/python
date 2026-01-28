# Project - TODOs

---

# 🧠 Phase 0: Mental shift (Swift → Python)

Before projects, two mindset notes:

| Swift                | Python                          |
| -------------------- | ------------------------------- |
| Strong typing        | Dynamic typing                  |
| Struct / Class heavy | Functions + objects             |
| Protocols            | Duck typing                     |
| Optionals            | `None`                          |
| Extensions           | Monkey patching                 |

Python rewards **clarity and iteration speed**, not compiler strictness.

---

# 🟢 Phase 1: Python fundamentals (with purpose)

## 🧩 Project 1: Command-line Personal Expense Tracker

### Why this project?

* Teaches data types, control flow, collections
* Mirrors real-world data handling
* ML later = *data first*

### Features

* Add an expense (amount, category, note)
* List all expenses
* Show total per category
* Save/load from file (JSON)

### Concepts learned

* `list`, `dict`
* Loops, conditionals
* Functions
* File I/O
* JSON serialization

### Swift mapping

| Swift       | Python             |
| ----------- | ------------------ |
| `[Expense]` | `list[dict]`       |
| Codable     | `json.dump / load` |
| `switch`    | `if / elif`        |

---

## 🧩 Project 2: Text Analyzer (very ML-relevant)

### What it does

Given a text file:

* Count words
* Find most common words
* Ignore stop words
* Case normalization

### Concepts learned

* Strings
* Dictionaries as frequency maps
* Functions returning values
* Basic algorithmic thinking

### ML relevance

This is **NLP 101** (tokenization + frequency).

---

# 🟡 Phase 2: Pythonic thinking (important shift)

## 🧩 Project 3: Log File Analyzer

### Example input

```
INFO User logged in
ERROR Database timeout
WARNING Disk space low
ERROR Invalid token
```

### Tasks

* Count each log level
* Extract error messages
* Save summary report

### Concepts learned

* File iteration
* `defaultdict`
* List comprehensions
* `with` context manager

### Swift comparison

| Swift          | Python              |
| -------------- | ------------------- |
| `map / filter` | List comprehensions |
| `do {}`        | `with`              |

---

## 🧩 Project 4: Mini REST Client (API consumer)

### What it does

* Call a public API (weather / quotes)
* Parse JSON response
* Display formatted output

### Concepts learned

* `requests` library
* HTTP basics
* JSON parsing
* Error handling (`try/except`)

### ML relevance

Most ML pipelines **consume APIs or datasets**.

---

# 🔵 Phase 3: Data + math (bridge to ML)

## 🧩 Project 5: CSV Data Analyzer (ML starter)

### Input

CSV file:

```
age,salary
25,50000
30,70000
```

### Tasks

* Load CSV
* Calculate mean, min, max
* Plot simple graph

### Concepts learned

* `csv` module
* `pandas` (intro)
* `matplotlib`
* Vectorized thinking

### This is **mandatory** before ML.

---

## 🧩 Project 6: Simple Recommendation Engine (logic only)

### Example

Users rate movies:

```python
{
  "Alice": {"Inception": 5, "Titanic": 3},
  "Bob": {"Inception": 4, "Avatar": 5}
}
```

### Tasks

* Find similar users
* Recommend unseen movies

### Concepts learned

* Nested dictionaries
* Similarity logic
* Functions returning structured data

### ML relevance

This becomes **collaborative filtering** later.

---

# 🔴 Phase 4: ML-adjacent Python thinking

## 🧩 Project 7: Dataset Cleaner

### Tasks

* Handle missing values
* Normalize numbers
* Remove outliers

### Concepts learned

* `numpy`
* Vector math
* Data preprocessing (huge in ML)

---

# 🧠 Phase 5: AI mindset projects (no ML yet)

## 🧩 Project 8: Rule-based Chatbot

### Features

* Keyword detection
* Context memory
* Simple intent matching

### Concepts learned

* State
* Functions as behavior
* Decision trees

### ML bridge

Later replace rules with **models**.

---

# 🧭 Suggested learning pace (30 min/day)

| Week | Focus                   |
| ---- | ----------------------- |
| 1    | Projects 1–2            |
| 2    | Projects 3–4            |
| 3    | Projects 5–6            |
| 4    | Projects 7–8            |
| 5    | Intro to NumPy + Pandas |
| 6    | First ML model          |

---
