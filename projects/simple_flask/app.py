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


# The `@app.route('/html')` decorator associates the `html` function with the URL '/html'.
# This means when a user visits the /html endpoint, this function will run.
@app.route('/html')
def html():
    """
    Handles the /html URL route.

    Returns:
        A rich HTML string to be rendered in the user's browser.
        Flask's default content type is HTML, so it automatically renders the string as a web page.
    """
    return """
    <p style="font-family: 'Georgia', serif; font-size: 1.5em; color: #333; text-shadow: 2px 2px 4px #aaa; text-align: center;"><strong>🎉 Hello, Flask! This is a rich HTML string. Served by Flask ✨</strong></p>
    """


# The `@app.route('/user/<username>')` decorator defines a dynamic route.
# The <username> part captures a value from the URL and passes it to the function.
@app.route('/user/<username>')
def user(username):
    """
    Handles the dynamic /user/<username> URL route.

    Args:
        username (str): The username captured from the URL.

    Returns:
        A personalized greeting that includes the username in an H1 heading.
    """
    return f"<h1>Hello, {username}!</h1>"


# This block ensures the web server only starts when you run the script directly.
# It is a standard Python practice. `debug=True` provides helpful error messages
# and automatically reloads the server on code changes.
if __name__ == '__main__':
    app.run(debug=True)



