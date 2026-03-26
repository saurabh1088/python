# ST-06 : Border Control

---

In **ST-06: Border Control**, the focus shifts from functionality to **Security Hardening**. While previous cookies were accessible to both the server and the browser, this task introduces the **HttpOnly** and **SameSite** flags to protect sensitive data from malicious attacks.

### 1. The Problem: Cookie Theft (XSS)
By default, cookies are accessible via JavaScript using `document.cookie`. If a malicious script (Cross-Site Scripting or XSS) is injected into a website, it can "scrape" all the cookies and send them to a hacker's server. 

For a "Vault Key" or an authentication token, this is a critical vulnerability. The solution is to tell the browser: *"You can store this, and you can send it back to the server, but you must never let JavaScript see it."*



---

### 2. The Solution: The "Vault Key" with Security Flags
A new route is created to issue a "Secret Vault Key." This cookie will be configured with strict security flags that make it invisible to the `script.js` file created in ST-04.

#### **Update the Backend Logic (`app.py`)**
The `set_cookie` method is updated with specific security parameters.

```python
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
```

#### **Update the Interface (`templates/dashboard.html`)**
A button is added to allow the user to "request" the secret key from the border control.

```html
<section class="security-vault">
    <h3>🔐 Security Vault</h3>
    <p>Status: 
        {% if request.cookies.get('vault_key') %}
            <span style="color: green;">Key Secured in Browser</span>
        {% else %}
            <span style="color: red;">No Key Detected</span>
        {% endif %}
    </p>
    <a href="/get-vault-key" class="btn">Request Vault Key</a>
</section>
```

---

### 3. Conceptual Breakdown: The Security Flags

| Flag | Function | Conceptual Analogy |
| :--- | :--- | :--- |
| **HttpOnly** | Blocks `document.cookie` access. | A locked safe that only the mailman (HTTP) can touch, not the resident (JS). |
| **SameSite** | Controls cross-domain behavior. | Ensuring the key only works at the front door of its own house. |
| **Secure** | Only sends over HTTPS. | Requiring an armored truck for transport (not used here for local dev). |



---

### ✅ ST-06 Completion Checklist
* [x] **Secure Route:** The `/get-vault-key` route is implemented.
* [x] **HttpOnly Implementation:** The flag is explicitly set to `True`.
* [x] **UI Feedback:** The dashboard correctly detects the presence of the cookie via Python.

### 🧪 The "Invisible" Test (Crucial)
1.  Click the **Request Vault Key** button.
2.  Open **DevTools -> Application -> Cookies**. Observe that `vault_key` exists and has a checkmark in the "HttpOnly" column.
3.  Open the **Console** tab and type: `console.log(document.cookie);`
4.  **Observation:** The `visitor_name` and `theme` will appear, but the `vault_key` will be **missing** from the output. 
