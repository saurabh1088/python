The project setup for **ST-01** is performed by establishing a decoupled architecture. This ensures that the Python logic, HTML templates, and static assets remain separate, following professional development patterns.

### 📂 Step 1: Directory Structure Creation

The following commands are executed in the terminal to generate the necessary project folders and empty files:

```bash
mkdir the_digital_passport
cd the_digital_passport
mkdir -p static/css static/js templates
touch app.py requirements.txt static/css/style.css static/js/script.js templates/dashboard.html

```

The resulting project tree appears as follows:

```text
digital_passport/
├── app.py              # Main Flask server & Cookie logic
├── requirements.txt    # Project dependencies
├── static/
│   ├── css/
│   │   └── style.css   # UI styling & Theme variables
│   └── js/
│       └── script.js   # Client-side cookie manipulation
└── templates/
    └── dashboard.html  # The "Passport" interface

```

---

### 📦 Step 2: Dependency Definition

The `requirements.txt` file is updated to include the Flask framework. Specifying the version ensures environment stability.

**`requirements.txt`**

```text
Flask==3.1.1

```

---

### 🐍 Step 3: Virtual Environment Initialization

The project dependencies are isolated by initializing a virtual environment to prevent version conflicts.

1. **Environment creation**:
```bash
python -m venv venv

```


2. **Activation**:
* **macOS/Linux**: `source venv/bin/activate`
* **Windows**: `venv\Scripts\activate`


3. **Installation**:
```bash
pip install -r requirements.txt

```



---

### 🛠️ Step 4: Backend Skeleton Construction (`app.py`)

A basic scaffold is written for `app.py`. A `secret_key` is defined at this stage, as it serves as a mechanical necessity for the signed sessions required in later tasks.

**`app.py`**

```python
from flask import Flask, render_template, request, make_response, session

app = Flask(__name__)

# This key is used to cryptographically sign the session cookie.
# It prevents unauthorized tampering with session-stored data.
app.secret_key = "passport_secret_dev_key" 

@app.route('/')
def dashboard():
    """
    Main entry point. It eventually reads cookies 
    to determine the user's displayed state.
    """
    return render_template('dashboard.html')

if __name__ == '__main__':
    # debug=True enables auto-reloading and helpful error messages.
    app.run(debug=True, port=5001) 

```

---

### ✅ ST-01 Completion Checklist

* [x] Project folders and files created.
* [x] `requirements.txt` configured and dependencies installed.
* [x] Virtual environment successfully activated.
* [x] `app.py` skeleton prepared for Phase 1 logic.

**ST-01 is concluded.** The next objective is **ST-02: Phase 1 (The Entry Stamp)**, which involves implementing the persistent "Check-in" cookie.
