## Simple Flask Calculator

This project is a lightweight web-based calculator built using the **Flask** framework. It provides a clean interface for performing fundamental arithmetic operations directly in a web browser.

---

### 🚀 Project Overview

The application demonstrates a classic **Model-View-Controller (MVC)** inspired flow in Python:

* **Backend (`app.py`)**: Handles the server logic, processes incoming `POST` requests from the user, performs calculations, and manages error handling (such as division by zero or invalid numeric inputs).
* **Frontend (`index.html`)**: (Implicitly required) Serves as the user interface where users input numbers and select operations.
* 
**Dependencies**: Managed via a standard `requirements.txt` file, ensuring the environment is consistent across different setups.



---

### 🛠️ Prerequisites

Before running the project, ensure you have the following installed:

* **Python 3.8+**
* **pip** (Python package manager)

---

### 📦 Installation and Setup

Follow these steps to get your development environment ready:

1. **Clone or Download the Project**:
Ensure all files (`app.py` and `requirements.txt`) are in your project directory.
2. **Create a Virtual Environment (Recommended)**:
It is best practice to isolate your project dependencies.
```bash
python -m venv venv

```


3. **Activate the Virtual Environment**:
* **Windows**: `venv\Scripts\activate`
* **macOS/Linux**: `source venv/bin/activate`


4. **Install Dependencies**:
Install the required packages, including Flask 3.1.1 and its supporting libraries.


```bash
pip install -r requirements.txt

```



---

### 🏃 How to Run the Project

1. **Prepare the Templates**:
Ensure you have a folder named `templates` in your root directory containing your `index.html` file, as the application uses `render_template` to serve the UI.
2. **Start the Flask Server**:
Run the application script directly from your terminal:
```bash
python app.py

```


3. **Access the Application**:
Once the server starts, you will see an output indicating the local address (usually `http://127.0.0.1:5000`). Open this URL in your web browser.
4. **Debug Mode**:
The project is configured with `debug=True`, which means the server will automatically reload whenever you save changes to your code.

---

### 🧮 Supported Operations

* **Addition (+)**
* **Subtraction (-)**
* **Multiplication (*)**
* **Division (/)**: Includes safety validation to prevent crashes when dividing by zero.
