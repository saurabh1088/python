# ST-07 : Data Erasure

In **ST-07: Data Erasure**, the project completes the **Cookie Lifecycle**. Having learned how to create, sign, and secure cookies, the final architectural requirement is knowing how to destroy them.

### 1. The Problem: The "Zombie Cookie"
Simply "forgetting" a variable in Python does not remove a cookie from the user's browser. Because cookies are stored on the client's hard drive, they will persist until they naturally expire. 

To "Log Out" or "Reset" a user, the server must explicitly send a command to the browser to delete the data. However, there is no `delete_cookie` command in HTTP. Instead, the server sends the cookie again but sets its **expiration date to the past**.



---

### 2. The Solution: The "Self-Destruct" Route
A single route is created that targets every type of storage used in the project:
1.  **Plain Cookies** (`visitor_name`, `home_airport`)
2.  **JavaScript Cookies** (`theme`)
3.  **Signed Sessions** (`suitcase`)
4.  **HttpOnly Cookies** (`vault_key`)

#### **Update the Backend Logic (`app.py`)**
The `set_cookie` method is used with `expires=0` to force immediate deletion.

```python
@app.route('/reset-passport')
def reset_passport():
    # 1. Clear the Signed Session (Suitcase)
    session.clear()
    
    # 2. Create the response to redirect home
    response = make_response(redirect(url_for('dashboard')))
    
    # 3. Explicitly expire the Persistent Cookies
    # Setting expires to 0 tells the browser the cookie is already dead
    response.set_cookie('visitor_name', '', expires=0)
    response.set_cookie('home_airport', '', expires=0)
    response.set_cookie('theme', '', expires=0)
    response.set_cookie('vault_key', '', expires=0)
    
    return response
```

#### **Update the Interface (`templates/dashboard.html`)**
A "Emergency Reset" button is added to the bottom of the passport.

```html
<hr>
<section class="danger-zone">
    <p>Need to clear your tracks?</p>
    <a href="/reset-passport" class="btn-danger">Clear All Passport Data</a>
</section>
```

---

### 3. Conceptual Breakdown: How Deletion Works

| Step | Action | Conceptual Analogy |
| :--- | :--- | :--- |
| **Session Clear** | `session.clear()` | Emptying the "Diplomatic Bag" on the server side. |
| **Cookie Expire** | `expires=0` | Telling the browser the "Milk" (cookie) expired in 1970. |
| **Value Reset** | `set_cookie('', ...)` | Overwriting the data with an empty string for safety. |

---

### 4. What has been achieved?
The application now supports a **Clean State Transition**.

* **Security:** If a user is on a public computer, they can now fully "wipe" their presence.
* **Full Coverage:** By including `vault_key` in the reset, even the `HttpOnly` cookies that JavaScript couldn't see are successfully removed by the server.
* **Lifecycle Completion:** The project has successfully moved through **Creation -> Usage -> Protection -> Destruction**.

### ✅ ST-07 Completion Checklist
* [x] **Session Wipe:** `session.clear()` effectively empties the suitcase.
* [x] **Header Manipulation:** The response sends multiple `Set-Cookie` headers with past expiration dates.
* [x] **User Redirection:** After the wipe, the user is sent back to the original "Check-in" form.

### 🧪 The "Clean Slate" Test
1.  Ensure you have a name, a suitcase, and a vault key active.
2.  Click **Clear All Passport Data**.
3.  **Observation:** You should be redirected to the "Check-in" screen. 
4.  Check **DevTools -> Application -> Cookies**. The list should be empty (or only contain a new, empty session ID).
