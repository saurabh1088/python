"""
A simple Flask web application.

This module initializes a basic Flask app, defines a single route for the
home page, and runs the development server.
"""

# Import the Flask class from the flask module.
# This class is the core of your web application.
from flask import Flask

# Create an instance of the Flask class.
# The `__name__` argument tells Flask where to look for resources like templates.
app = Flask(__name__)

# The `@app.route('/')` decorator associates the `index` function with the URL '/'.
# This means when a user visits the root of your website, this function will run.
@app.route('/')
def index():
    """
    Handles the root URL route.

    Returns:
        A simple string "Hello, Flask!" to be displayed in the user's browser.
    """
    return "Hello, Flask!"

# This block ensures the web server only starts when you run the script directly.
# It is a standard Python practice. `debug=True` provides helpful error messages
# and automatically reloads the server on code changes.
if __name__ == '__main__':
    app.run(debug=True)



