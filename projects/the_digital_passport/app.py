from flask import Flask, render_template, request, make_response, session

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
    return render_template('dashboard.html')

if __name__ == '__main__':
    # debug=True enables auto-reloading and helpful error messages.
    app.run(debug=True, port=5001) 
