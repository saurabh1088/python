"""
A simple Flask web application.

This module initializes a basic Flask app, defines a single route for the
home page, and runs the development server.
"""

# -------------------------------- Imports -------------------------------- #
# Import the Flask class from the flask module.
# This class is the core of your web application.
from flask import Flask
# Import the render_template function from the flask module.
# This function is used to render HTML templates stored in the 'templates' directory.
from flask import render_template


# ---------------------------- Application Setup --------------------------- #
# Create an instance of the Flask class.
# The `__name__` argument tells Flask where to look for resources like templates.
app = Flask(__name__)


# ------------------------------ Route Definitions ------------------------- #
# The `@app.route('/')` decorator associates the `index` function with the URL '/'.
# This means when a user visits the root of your website, this function will run.
@app.route('/')
def index():
    """
    Handles the root URL route.

    Returns:
        Renders and returns the 'index.html' template to be displayed in the user's browser.
    """
    # Render the 'index.html' template and pass a variable to it.
    # app_name is a variable that can be used within the HTML template.
    # It can be any string one want to display on the page, just one has to use same name in the template.
    # Here, we set it to "Hello Flask App!!!".
    # The render_template function looks for the template in the 'templates' folder.
    return render_template("index.html", app_name="Hello Flask App!!!")


# The `@app.route('/form')` decorator associates the `form` function with the URL '/form'.
@app.route('/form', methods=['GET'])
def form():
    """
    Handles the /form URL route.

    Returns:
        Renders and returns the 'form.html' template to be displayed in the user's browser.
    """
    return render_template("form.html", form_name="Who's your Hero!")


# ------------------------------ Run the App ------------------------------- #
# This block ensures the web server only starts when you run the script directly.
# It is a standard Python practice. `debug=True` provides helpful error messages
# and automatically reloads the server on code changes.
if __name__ == '__main__':
    app.run(debug=True)



