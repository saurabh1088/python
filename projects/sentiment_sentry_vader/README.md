## Sentiment Sentry (VADER)

Sentiment Sentry is a small command‑line tool that uses the VADER sentiment analysis library to classify text as **positive**, **negative**, or **neutral**.

### 1. Prerequisites

- **Python 3.11** (or compatible Python 3.x)
- **git** and a terminal (macOS: Terminal or iTerm)

### 2. Clone or download the project

If you haven’t already:

```bash
git clone <your-repo-url>
cd sentiment_sentry_vader
```

Or, if you have the folder already, just `cd` into it:

```bash
cd /Users/saurabhverma/DevBox/python/projects/sentiment_sentry_vader
```

### 3. Create and activate a virtual environment (recommended)

If the `venv` folder already exists (as in this project), you can skip creation and just activate it.

#### macOS / Linux

```bash
python3 -m venv venv        # only if venv doesn't exist yet
source venv/bin/activate
```

You should now see something like `(venv)` at the start of your shell prompt.

### 4. Install dependencies

With the virtual environment activated:

```bash
pip install vaderSentiment
```

If you add more dependencies later, consider adding a `requirements.txt` file and installing via:

```bash
pip install -r requirements.txt
```

### 5. Run the program

From the project root (with the virtual environment activated):

```bash
python sentry.py
```

You should see:

```text
--- 🤖 Sentiment Sentry Active ---
Type 'exit' to quit.
```

Now you can type any sentence and press Enter to analyze its sentiment.

### 6. Exit the program

You can stop the program in two ways:

- **Graceful exit (recommended)**: type `exit` (any case: `exit`, `EXIT`, `Exit`, etc.) and press Enter.
- **Force quit**: press `Ctrl + C` in the terminal to interrupt the program.

### 7. Deactivate the virtual environment

When you’re done working with the project:

```bash
deactivate
```

Your shell will return to its normal state (without the `(venv)` prefix).

