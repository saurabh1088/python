# 🚀 Simple Flask Project

A minimal Flask project to get started with web development in Python.

---

## 📂 Step 1: Create Project Folder

```bash
mkdir simple_flask
cd simple_flask
```

---

## 🐍 Step 2: Set Up Virtual Environment

A **virtual environment** keeps project dependencies isolated from the global Python installation.

From inside `simple_flask` run:

```bash
python3 -m venv venv
source venv/bin/activate
```

* After activation, terminal will show `(venv)` at the beginning → meaning the environment is active.
* A new folder `venv/` will also appear in the project directory. (⚠️ Do **not** commit this folder to GitHub; add it to `.gitignore`.)

---

## 📦 Step 3: Install Flask

```bash
pip install flask
```

---

## 📄 Step 4 (Optional but Recommended): Freeze Dependencies

```bash
pip freeze > requirements.txt
```

* This generates a `requirements.txt` file listing all dependencies.
* Another developer (or future you) can install them using:

  ```bash
  pip install -r requirements.txt
  ```

---

## 📝 Step 5: Create Starter Flask App

Create a file **`app.py`** with the following code:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

---

## ▶️ Step 6: Run the App

Activate the virtual environment (if not already active):

```bash
source venv/bin/activate
```

Run the app:

```bash
python app.py
```

By default, Flask runs on **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**.
Open it in browser to see app running 🎉.

---

