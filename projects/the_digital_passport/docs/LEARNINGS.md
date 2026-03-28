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

## 📘 Part 3: QnAs

### 🎤 Technical Interview Prep: "The Digital Passport"

#### **Q1: "How do you handle sensitive data in a stateless web application?"**
**The Answer:** > "In the Digital Passport project, I implemented a **Defense in Depth** strategy. For non-sensitive UI preferences like 'Night Vision,' I used plain cookies accessible by JavaScript. However, for sensitive data like the 'Virtual Suitcase,' I utilized **Flask-signed sessions**. This ensures the data is cryptographically signed with a server-side `secret_key`. If a user attempts to tamper with the session string in their browser, the HMAC signature becomes invalid, and the server rejects the data, maintaining system integrity without a database."



#### **Q2: "What is a 'Flash of Unstyled Content' (FOUC) and how did you solve it?"**
**The Answer:** > "FOUC occurs when the browser renders the default CSS before the JavaScript can apply user preferences from a cookie. In my implementation, I moved the logic from 'Client-only' to 'Full-stack Sync.' Instead of waiting for JS to load, the **Python backend** reads the `theme` cookie during the initial request and injects the correct CSS class directly into the `<body>` tag via Jinja2. This ensures the page is 'pre-hydrated' with the correct theme before the first pixel is even rendered."



#### **Q3: "Explain the difference between a Persistent Cookie and a Session Cookie."**
**The Answer:** > "A **Session Cookie** is stored in the browser's RAM and is deleted when the tab or browser is closed; it’s the default behavior when no expiration is set. A **Persistent Cookie** uses the `max_age` or `expires` attribute to be saved to the user's disk. In this project, I used persistent cookies for the 'Traveler Identity' so that the application would recognize the user even if they returned weeks later, whereas I used session-based logic for temporary transactional data."



#### **Q4: "How do you protect cookies from Cross-Site Scripting (XSS) attacks?"**
**The Answer:** > "The primary defense I implemented was the **`HttpOnly` flag**. By setting this flag on the 'Vault Key' cookie, I instructed the browser to block all access to that cookie from the JavaScript `document.cookie` API. This ensures that even if a malicious script is successfully injected into the page, it cannot 'scrape' or steal the user's most sensitive credentials, as they are only visible to the server over HTTP headers."



---

### 🛡️ Final Portfolio Tip: The "Architect's Choice"
When discussing this project, emphasize that the **ST-08 Telemetry UI** was added specifically for **Observability**. Mentioning that you build internal tools to monitor state changes shows that you prioritize debugging and system transparency—traits highly valued in software architects.

