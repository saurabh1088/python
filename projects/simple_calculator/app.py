"""
A simple Flask web application.

This module initializes a basic Flask app, defines a single route for the
home page, and runs the development server.
"""

# Import the Flask class from the flask module.
# This class is the core of the web application.
from flask import Flask, render_template, request

# Creates an instance of the Flask class.
# The `__name__` argument tells Flask where to look for resources like templates.
app = Flask(__name__)

# The `@app.route('/')` decorator associates the `index` function with the URL '/'.
# This means when a user visits the root of this website, this function will run.
@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None
    
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    error = "Cannot divide by zero!"
                else:
                    result = num1 / num2
        except ValueError:
            error = "Please enter valid numbers!"
    
    return render_template('index.html', result=result, error=error)

# This block ensures the web server only starts when one runs the script directly.
# It is a standard Python practice. `debug=True` provides helpful error messages
# and automatically reloads the server on code changes.
if __name__ == '__main__':
    app.run(debug=True)


