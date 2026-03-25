In **ST-05**, the goal is to eliminate the "Flash of Unstyled Content" (FOUC) by synchronizing the **Backend (Python)** with the **Frontend (JavaScript)** cookie.

### 1. The Problem: The "White Flash"
Currently, when a user with "Night Vision" enabled refreshes the page:
1.  **Flask** sends the default HTML (which is Light Mode by default).
2.  The browser renders the white background.
3.  **JavaScript** finally loads, reads the cookie, and flips the CSS class to Dark Mode.
This results in a jarring white flash for a fraction of a second. 



### 2. The Solution: Server-Side Theme Detection
The Python backend is modified to read the `theme` cookie *before* rendering the template. By passing this value to Jinja2, the correct CSS class can be applied directly to the `<body>` tag in the initial HTML response.

#### **Update the Backend Logic (`app.py`)**
The `dashboard` route is updated to extract the `theme` value from the request headers.

```python
@app.route('/')
def dashboard():
    # Phase 1 & 2 Data
    visitor_name = request.cookies.get('visitor_name')
    home_airport = request.cookies.get('home_airport')
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
```

#### **Update the Template (`templates/dashboard.html`)**
The `<body>` tag is modified to use the variable passed from Flask.

```html
<body class="{{ theme_class }}">
    <div class="container">
        </div>
    
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
```

---

### 3. Conceptual Breakdown: What has been achieved?

From a functional point of view, the application has moved from **Client-Only State** to **Full-Stack State Synchronization**.

* **The Bridge:** The `theme` cookie now acts as a shared variable. JavaScript "writes" the user's intent, and Python "reads" it to prepare the environment.
* **Performance:** The user experience is now seamless. Because the `class="dark-mode"` is present in the very first byte of HTML sent over the network, the browser never attempts to render the light version.
* **Reliability:** Even if a user has JavaScript disabled, the theme will still persist correctly based on the last saved cookie.



---

### ✅ ST-05 Completion Checklist
* [x] **Python Reader:** `request.cookies.get('theme')` is implemented in the main route.
* [x] **Jinja Injection:** The `theme_class` variable is dynamically inserted into the HTML template.
* [x] **Sync Test:** The "white flash" on refresh is gone.
