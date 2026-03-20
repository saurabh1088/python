from flask import Flask, render_template, request, make_response, redirect, url_for

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

    # Read the persistent cookies
    # If the cookie doesn't exist, it defaults to None
    visitor_name = request.cookies.get('visitor_name')
    home_airport = request.cookies.get('home_airport')
    
    return render_template('dashboard.html', name=visitor_name, airport=home_airport)

@app.route('/check-in', methods=['POST'])
def check_in():
    # Extract data from the form
    name = request.form.get('name')
    airport = request.form.get('airport')
    
    # Create a response object to redirect back to the dashboard
    response = make_response(redirect(url_for('dashboard')))
    
    # Set Persistent Cookies (Valid for 30 days)
    # 60 seconds * 60 minutes * 24 hours * 30 days
    max_age = 60 * 60 * 24 * 30
    
    response.set_cookie('visitor_name', name, max_age=max_age)
    response.set_cookie('home_airport', airport, max_age=max_age)
    
    return response


if __name__ == '__main__':
    # debug=True enables auto-reloading and helpful error messages.
    app.run(debug=True, port=5001) 
