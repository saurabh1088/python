# Learnings

---

## 📘 Part 1: Lessons Learned (Architectural Review)

This summary captures the high-level engineering takeaways from the "Digital Passport" lifecycle.

### 1. The Persistence Trade-off
The developer learned that **Persistent Cookies** (`max_age`) are ideal for non-sensitive UX (like a username or theme) because they survive browser restarts. However, they lack the security of **Session Cookies**, which live only in the browser's volatile memory.

### 2. Integrity vs. Visibility
A major breakthrough was the implementation of **Signed Sessions**. The project demonstrated that even if a user can *see* their "Suitcase" data in the browser, the server uses a `secret_key` to ensure they cannot *modify* it. This move from "client-side honesty" to "server-side validation" is the foundation of secure web apps.

### 3. The Synchronization Bridge
Through the "Night Vision" feature, it was observed that state is a shared responsibility. Using **Jinja2** to pre-render the CSS class based on a cookie set by **JavaScript** solved the "White Flash" (FOUC) problem, proving that full-stack synchronization is mandatory for a premium user experience.

### 4. Defense in Depth
The use of the `HttpOnly` flag proved that security is about layers. By isolating the `vault_key` from the JavaScript engine, the application was hardened against XSS attacks without losing the ability to identify the user at the server level.


---

## 📘 Part 2: Plain Cookies
```
response.set_cookie('visitor_name', name, max_age=max_age)
```

- This sets a plain cookie(not the session cookie).
- Stores data directly in the browser, going into developer tools in browser, this value can be modified.

![Plain Cookie - Cookies here can be edited accessing from browser's developer tools](./screens/plain_cookie_example_screenshot_1.png)


![Plain Cookie - Cookies here can be edited accessing from browser's developer tools](./screens/plain_cookie_example_screenshot_2.png)


---

### 1. 🍪 Cookies Store Data Directly in the Browser

* The values like:

  * `visitor_name = Bruce Wayne`
  * `home_airport = Batcave`
* are stored **as plain text in the browser’s storage** (DevTools → Application → Cookies)

👉 This means the browser is the **source of truth**, not the server.

---

### 2. ✏️ User Can Freely Modify Cookie Values

* In the second screenshot, values are changed to:

  * `Bruce Wayne Updated`
  * `Batcave Updated`

👉 This was done **manually via DevTools**, not through your app UI.

---

### 3. 🔁 Browser Sends Modified Cookies Back to Server

* On page refresh:

  * Browser automatically sends updated cookies in the request header:

```http
Cookie: visitor_name=Bruce Wayne Updated; home_airport=Batcave Updated
```

👉 The server **blindly trusts this data**.

---

### 4. 🖥️ Server Renders UI Based on Modified Data

* Flask reads cookies using:

```python
request.cookies.get('visitor_name')
```

* Since cookies were modified:

  * UI now shows: **“Welcome Back, Bruce Wayne Updated!”**

👉 The server has **no way of knowing the data was tampered with**.

---

### 5. ⚠️ No Integrity or Security Protection

* Plain cookies:

  * ❌ Not encrypted
  * ❌ Not signed
  * ❌ Not validated

👉 Any user can:

* Change values
* Inject unexpected data
* Break application logic

---

### 6. 🛡️ Why This Is a Problem

* Demonstrates **lack of trust boundary**
* Real-world risks:

  * Changing user roles (`admin=true`)
  * Modifying prices or cart data
  * Session impersonation

---

### 7. 🔐 Motivation for Sessions (Next Step)

* This exact weakness is why:

  * **Flask Sessions (ST-03)** were introduced

👉 Sessions add:

* **Cryptographic signing**
* **Tamper detection**

---

### ⚡ One-Line Insight

```text
Plain cookies = client-controlled data → never trust blindly
```

---
