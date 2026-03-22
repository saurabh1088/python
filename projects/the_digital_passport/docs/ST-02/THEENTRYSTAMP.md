In **ST-02**, the focus shifts to implementing **Persistent Cookies**. Unlike session cookies that disappear when a browser is closed, persistent cookies remain on the user's device for a specified duration.

The goal of this task is to create a "Check-in" feature that captures the traveler's name and home airport, storing them so the application recognizes the user upon return.

### 1. Update the Backend Logic (`app.py`)

The `make_response` function is used to wrap the rendered template. This allows the attachment of a cookie to the outgoing HTTP header before it is sent to the browser.

```python
from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)
app.secret_key = "passport_secret_dev_key"

@app.route('/')
def dashboard():
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

```

---

### 2. Create the Interface (`templates/dashboard.html`)

The HTML is structured to conditionally show a "Check-in" form if the user is unknown, or a "Passport" greeting if the cookies are found.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Digital Passport</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <h1>🌍 Digital Passport</h1>

        {% if not name %}
            <section class="check-in">
                <h2>Border Control: Please Check In</h2>
                <form action="/check-in" method="POST">
                    <input type="text" name="name" placeholder="Full Name" required>
                    <input type="text" name="airport" placeholder="Home Airport (e.g. LHR)" required>
                    <button type="submit">Stamp Passport</button>
                </form>
            </section>
        {% else %}
            <section class="passport-info">
                <h2>Welcome Back, {{ name }}!</h2>
                <p><strong>Home Base:</strong> {{ airport }}</p>
                <p><em>Your identity is currently stored in a 30-day persistent cookie.</em></p>
            </section>
        {% endif %}
    </div>
</body>
</html>

```

---

### 3. Implementation Checklist for ST-02

* **The "Check-in" Form:** A standard HTML form captures data and sends it to the `/check-in` route via `POST`.
* **The Response Object:** Instead of returning a simple string or template, the code creates a `response` object. This is a crucial architectural step because cookies are part of the **HTTP Header**, not the HTML body.
* **Max-Age:** The `max_age` parameter (in seconds) tells the browser exactly how long to keep this data.

### ✅ Verification Steps

1. The user starts the server using `python app.py` or `flask --app app run`.
2. The application is opened in a browser at `http://127.0.0.1:5001`.
3. The user fills out the form and submits it.
4. **The Test:** The user closes the browser tab, re-opens the browser, and returns to the URL. The "Welcome Back" message should appear automatically because the browser sent the persistent cookie back to the server.

**ST-02 is concluded.** The next task is **ST-03: Phase 2 (The Diplomatic Bag)**, which introduces **Signed Sessions** to manage a "Virtual Suitcase" that users cannot easily tamper with.
