## 📄 Project Requirements Document: The Digital Passport

### 1. Project Overview

**The Digital Passport** is a travel-themed web application designed to demonstrate the full lifecycle and security configurations of HTTP cookies and Flask sessions. Unlike a standard app that uses a database, this application relies entirely on the client's browser storage to "remember" the traveler's identity, luggage, and preferences.

---

### 2. Functional Requirements

#### **Phase 1: Identity & Persistence (The Entry Stamp)**

* **User Check-in:** The user must be able to enter their name and a "Home Airport."
* **Long-term Memory:** The app must remember the user’s name even if they close the browser and return a week later.
* **Technical Goal:** Implement **Persistent Cookies** using `max_age` and `expires`.

#### **Phase 2: The Virtual Suitcase (The Diplomatic Bag)**

* **Item Management:** Users can add travel items (e.g., "Passport," "Sunscreen") to a list.
* **Tamper-Proof Storage:** These items must be stored in a way that the user cannot manually edit the list values in the browser console without the server detecting it.
* **Technical Goal:** Master **Flask Sessions (Signed Cookies)** and the `app.secret_key` mechanism.

#### **Phase 3: Visual Environment (Night Vision)**

* **UI Toggling:** A "Night Vision" mode (Dark Mode) that can be toggled via the UI.
* **Synchronized State:** The setting must be readable by both JavaScript (for instant CSS changes) and Python (to ensure the correct theme is served on page load).
* **Technical Goal:** Understand **Client-Side vs. Server-Side** cookie access.

#### **Phase 4: Security & Border Control (The Secure Vault)**

* **Sensitive Data Simulation:** A "Secret Access Code" cookie that is invisible to JavaScript.
* **Data Erasure:** A "Reset Passport" function that clears all cookies and the session simultaneously.
* **Technical Goal:** Implement `HttpOnly`, `Secure`, and `SameSite` flags.

---

### 3. Technical Stack

* **Backend:** Python 3.x with Flask Framework.
* **Frontend:** HTML5, CSS3 (using Variables for themes), and Vanilla JavaScript.
* **State Management:** `Flask.session`, `make_response.set_cookie`, and `request.cookies`.

---

### 4. Cookie Architecture Design

| Feature | Cookie Name | Type | Storage Method | Security Level |
| --- | --- | --- | --- | --- |
| **Traveler Name** | `visitor_name` | Persistent | `set_cookie(max_age=...)` | Low |
| **Suitcase Items** | `session` | Signed/Encrypted | `flask.session` | Medium (Server-Signed) |
| **UI Theme** | `theme` | Functional | JS `document.cookie` | Low (Shared Access) |
| **Access Code** | `vault_key` | Secret | `set_cookie(httponly=True)` | High (Hidden from JS) |

---

### 5. Non-Functional Requirements

* **Educational Transparency:** The UI must include a "Dev Console" section that explains which cookie was just updated and why.
* **Statelessness:** No database (SQLite/PostgreSQL) is allowed. All data must live in the browser.
* **Robustness:** The app must handle "Empty States" gracefully (e.g., if a user visits for the first time with no cookies).

---

### 6. Success Criteria (Learning Milestones)

1. **Verification:** The user can see their name in the Chrome DevTools 'Application' tab.
2. **Security Check:** Attempting to type `document.cookie` in the console does **not** reveal the `vault_key`.
3. **Persistence:** Closing the browser tab and reopening the app still shows the "Virtual Suitcase" items.
4. **Integrity:** Changing a character in the `session` cookie manually in the browser causes the app to safely reset the session rather than crashing.

---
