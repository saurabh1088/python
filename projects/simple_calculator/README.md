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

To run a Flask project effectively, there are two primary methods depending on whether the user executes the internal script logic or utilizes the official Flask Command Line Interface (CLI). 


The application can be started using either the Python interpreter or the Flask CLI. Before starting, it is necessary to ensure the virtual environment is active and the templates are organized. 

#### **Option 1: Using the Flask CLI (Recommended for Development)**

The `flask` command is the modern standard for running applications as it automatically handles the application context and provides clear status updates. 

1. **Navigate to the project directory**:
```bash
cd /path/to/your/simple_calculator

```


2. **Activate the Virtual Environment**:
* 
**macOS/Linux**: `source venv/bin/activate` 


* 
**Windows**: `venv\Scripts\activate` 




3. **Run the Application**:
The `--app` flag is used to point to the main script (e.g., `app.py`). 


```bash
flask --app app run

```


*Note: Adding `--debug` to this command enables the interactive debugger and auto-reloader.*

---

#### **Option 2: Running the Script Directly**

This method relies on the `if __name__ == '__main__':` block defined at the bottom of the `app.py` file. 

1. **Prepare the Templates**:
A folder named `templates` must exist in the root directory containing `index.html`, as `render_template` expects this specific structure. 


2. **Start the Server**:
The script is executed directly using the Python interpreter: 


```bash
python app.py

```


This triggers `app.run(debug=True)`, which provides helpful error messages and reloads the server automatically when code changes are saved. 



---

### 🔍 Architectural Note: Execution Choice

* 
**Option 1** is preferred when following the official Flask workflow or when additional CLI commands (such as database migrations) are required. 


* 
**Option 2** is suitable for quick testing or when the execution logic should remain entirely within the Python script itself. 



Would the user like a demonstration of how to configure environment variables to allow for the use of `flask run` without the `--app` flag?

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
