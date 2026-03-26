# ST-06 Thoughts

In **ST-06**, the project transitions from **Functional State** to **Secure State**. Conceptually, the "Trust Model" of the application is redesigned to protect against malicious actors.

### 1. The Problem: The "XSS Vulnerability"
Until now, all cookies (`visitor_name`, `theme`) were stored in an "Open Folder." 
* **The Weakness:** Any script running on the page—including a malicious one from a third-party library or an injected ad—could use the command `document.cookie` to read the entire contents of that folder.
* **The Threat:** If a session token or a "Vault Key" is stolen, an attacker can impersonate the user from a completely different computer.

---

### 2. The Solution: "Digital Isolation"
In **ST-06**, the `HttpOnly` flag is introduced. This creates a one-way mirror for the browser.

* **The Browser's Role:** It still stores the cookie. It still sends the cookie back to the Flask server with every request so the server can "recognize" the user.
* **The JavaScript's Role:** It is completely blinded. Even though the cookie is physically in the browser, the JavaScript engine is forbidden from seeing or touching it.

---

### 3. Conceptual Breakdown: The Security Flags

| Concept | Flag Name | Role in the Passport App |
| :--- | :--- | :--- |
| **Visibility** | `HttpOnly=True` | Ensures the "Vault Key" cannot be stolen by scripts. |
| **Origin Trust** | `SameSite='Lax'` | Ensures the "Vault Key" is only sent when the user is actually on your site, not via a hidden link on a malicious site (CSRF protection). |
| **Encryption** | `Secure=True` | (Conceptual) Ensures the key is only sent over HTTPS so it can't be "sniffed" on public Wi-Fi. |

---

### 4. What has been achieved?
The application now differentiates between **UI Preferences** and **Security Credentials**.

* **Tier 1 (Public):** `theme` and `visitor_name`. These are "low-stakes" data points that JavaScript *should* see to update the UI.
* **Tier 2 (Protected):** `session` and `vault_key`. these are "high-stakes" data points that are locked away from the frontend entirely.

**The Achievement:** The architect has successfully implemented **Defense in Depth**. Even if a hacker finds a way to run a script on the dashboard, they can change the background color (Tier 1), but they cannot steal the user's secret access key (Tier 2).

**The next task is ST-07: Data Erasure.** This involves building the "Self-Destruct" mechanism to properly clear all these different types of cookies at once. 

