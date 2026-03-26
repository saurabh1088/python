from flask import Flask, render_template, request, make_response, redirect, url_for, session

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

    # Retrieve the suitcase list from the session. 
    # Default to an empty list if it doesn't exist.
    suitcase = session.get('suitcase', [])

    # ST-05: Read the theme cookie set by JavaScript
    # We default to 'light' if the cookie doesn't exist
    current_theme = request.cookies.get('theme', 'light')
    
    # Create a helper variable for the CSS class
    theme_class = 'dark-mode' if current_theme == 'dark' else ''
    
    return render_template('dashboard.html', 
                           name=visitor_name, 
                           airport=home_airport, 
                           suitcase=suitcase,
                           theme_class=theme_class)

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

@app.route('/add-item', methods=['POST'])
def add_item():
    item = request.form.get('item')
    
    # Initialize the suitcase in the session if not present
    if 'suitcase' not in session:
        session['suitcase'] = []
    
    # Logic: To update a list in a session, it must be re-assigned
    # so Flask notices the change.
    current_suitcase = session['suitcase']
    if item:
        current_suitcase.append(item)
        session['suitcase'] = current_suitcase
    
    return redirect(url_for('dashboard'))

@app.route('/get-vault-key')
def get_vault_key():
    response = make_response(redirect(url_for('dashboard')))
    
    # Setting a High-Security Cookie
    # HttpOnly=True: Prevents JavaScript from accessing the cookie
    # SameSite='Lax': Prevents the cookie from being sent on cross-site subrequests (CSRF protection)
    response.set_cookie('vault_key', 'SECRET-PASS-789', 
                        max_age=60*60, 
                        httponly=True, 
                        samesite='Lax')
    
    return response

if __name__ == '__main__':
    # debug=True enables auto-reloading and helpful error messages.
    app.run(debug=True, port=5001) 
