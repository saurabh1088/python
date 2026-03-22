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


## Detailed Explaination

From a functional and architectural standpoint, **ST-03** represents the transition from **Insecure User Data** to **Server-Validated Integrity**.

The fundamental change is how the application trusts the information it receives from the browser.

### 1. The Problem: The "Honesty System" (ST-02)

In **ST-02**, the user's name and airport were stored in **Plaintext Cookies**.

* **Vulnerability:** The browser acts as a storage locker that the user has the key to. A user could open their Developer Tools, change `visitor_name` from "Saurabh" to "Admin," and the server would blindly believe it.
* **Risk:** This is fine for a theme preference, but dangerous for a "Suitcase." If a user could manually add an "Access Key" to their cookie, they could bypass security checks.
* **Statelessness Issue:** The server has no way to verify if the data it just read is the same data it sent five minutes ago.

---

### 2. The Solution: The "Sealed Envelope" (ST-03)

In **ST-03**, the application uses **Signed Sessions**. This changes the cookie from a "Sticky Note" to a "Sealed Envelope" with a wax seal (the HMAC Signature).

* **Mechanism:** When the user adds an item like "Passport," Flask takes that list, serializes it (converts it to a string), and attaches a cryptographic hash based on the `app.secret_key`.
* **The Result:** The user can still see the data in their browser, but they cannot **modify** it.

---

### 3. What has been achieved?

| Feature | ST-02 (Plain Cookies) | ST-03 (Signed Sessions) |
| --- | --- | --- |
| **Integrity** | **None.** User can edit values freely. | **High.** Any edit breaks the signature. |
| **Security** | **Low.** Vulnerable to "Session Hijacking." | **Medium.** Data is protected by a Secret Key. |
| **Trust Model** | The Server trusts the Client. | The Server only trusts its own Signature. |
| **Data Type** | Simple strings only. | Complex objects (Lists, Dicts). |

---

### 🔍 Architectural Insight: The "Secret Key"

The `app.secret_key` is now the most important part of the application.

* If the architect changes the `secret_key`, all existing "Suitcases" will become invalid because the old signatures won't match the new key.
* If a hacker steals the `secret_key`, they can forge their own signatures and put whatever they want in their "Suitcase."

**The Achievement:** The application now has a "Memory" that it can actually trust. This is the foundation for user accounts, shopping carts, and secure permissions.

