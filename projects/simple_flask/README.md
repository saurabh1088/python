# Simple Flask Project

## Steps

### Create folder
mkdir simple_flask
cd simple_flask

### Set up virtual environment
A virtual environment keeps project's dependencies isolated.

From folder simple_flask execute
python3 -m venv venv
source venv/bin/activate

Source command will now start terminal with (venv), showing the environment is active.
Also one will observe a new created folder venv in the directory.

### Install Flask
pip install flask

### (Optional Step)Freeze dependencies into a requirements.txt
pip freeze > requirements.txt

This will create requirements.txt file in directory.

### Create starter Flask App
Create a file named app.py with below minimum code to start.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
    
### Run the app
python app.py
