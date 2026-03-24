In **ST-03**, the project moves from "Plain Cookies" (which are easily readable and editable by users) to **Signed Sessions**. This is a critical architectural shift for any software engineer.

---

### 🛡️ ST-03: The Diplomatic Bag (Signed Sessions)

**The Problem:** If items like "Passport" or "Gold Bar" are stored in a plain cookie (like `visitor_name`), a user could open the browser console and change the value to something else.
**The Solution:** **Flask Sessions**. Flask takes the data, turns it into a string, and signs it with a "cryptographic signature" using the `app.secret_key`. The user can see the data, but if they change a single character, the signature becomes invalid, and the server rejects the data.

#### 1. Update the Backend Logic (`app.py`)

The `session` object in Flask acts like a dictionary that is automatically saved into a signed cookie.

```python
from flask import Flask, render_template, request, make_response, redirect, url_for, session

app = Flask(__name__)
# The secret key is the "password" for the signature. 
# In production, this should be a random, hidden string.
app.secret_key = "passport_secret_dev_key"

@app.route('/')
def dashboard():
    visitor_name = request.cookies.get('visitor_name')
    home_airport = request.cookies.get('home_airport')
    
    # Retrieve the suitcase list from the session. 
    # Default to an empty list if it doesn't exist.
    suitcase = session.get('suitcase', [])
    
    return render_template('dashboard.html', 
                           name=visitor_name, 
                           airport=home_airport, 
                           suitcase=suitcase)

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

```

---

#### 2. Update the Interface (`templates/dashboard.html`)

The "Passport" section is expanded to include the "Virtual Suitcase" and a form to add new items.

```html
<section class="passport-info">
    <h2>Welcome Back, {{ name }}!</h2>
    <p><strong>Home Base:</strong> {{ airport }}</p>
    <hr>
    
    <h3>🧳 Your Virtual Suitcase</h3>
    <ul>
        {% for item in suitcase %}
            <li>{{ item }}</li>
        {% else %}
            <li><em>Your suitcase is empty. Pack something!</em></li>
        {% endfor %}
    </ul>

    <form action="/add-item" method="POST">
        <input type="text" name="item" placeholder="Add item (e.g. Camera)" required>
        <button type="submit">Pack Item</button>
    </form>
</section>

```

---

### ✅ ST-03 Completion Checklist

* [x] **Secret Key defined:** The `app.secret_key` is active.
* [x] **Session Logic:** The `/add-item` route correctly modifies the `session` dictionary.
* [x] **UI Rendering:** The Jinja2 `{% for %}` loop displays items stored in the signed cookie.

### 🧪 The "Integrity" Test

1. Open the application and pack 2-3 items.
2. Open DevTools -> Application -> Cookies. Find the `session` cookie.
3. The value is a long, encoded string. **Delete the last character** of that value.
4. Refresh the page.
5. **Observation:** The suitcase will likely appear empty. This happens because the Flask backend detected the signature was tampered with and safely discarded the session.

**ST-03 is concluded.** The next objective is **ST-04: Phase 3 (Night Vision)**, which focuses on using JavaScript to manipulate cookies for UI theme changes. Would the user like to proceed? 🧱✨
