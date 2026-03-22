## Tasks

To transition from requirements to execution, we will break the **Digital Passport** project into a logical, sprint-based task list. This structure ensures you master one "Cookie Level" before moving to more complex security configurations.

## 🗺️ Digital Passport: Project Task Board

| Task ID | Status | Task Description | Technical Focus | Est. Time |
| --- | --- | --- | --- | --- |
| **ST-01** | ✅ | **Environment & Scaffold** | Directory structure, `venv`, and Flask Init | 15m |
| **ST-02** | ⬜ | **Phase 1: The Entry Stamp** | Build "Check-in" form & set persistent `visitor_name` | 45m |
| **ST-03** | ⬜ | **Phase 2: The Diplomatic Bag** | Setup `app.secret_key` and Session-based "Suitcase" | 60m |
| **ST-04** | ⬜ | **Phase 3: Night Vision (JS)** | Create theme toggle via `document.cookie` in Vanilla JS | 45m |
| **ST-05** | ⬜ | **Phase 3: Night Vision (Py)** | Read `theme` cookie in Flask to persist CSS on load | 30m |
| **ST-06** | ⬜ | **Phase 4: Border Control** | Implement `HttpOnly` "Vault Key" & Security Flags | 40m |
| **ST-07** | ⬜ | **Phase 4: Data Erasure** | Create "Reset Passport" to clear cookies & sessions | 20m |
| **ST-08** | ⬜ | **The Dev Console UI** | Build a UI section that displays active cookies visually | 60m |

---

### 📂 ST-01: Project Directory Structure

Before writing code, create this professional structure to keep your concerns separated:

```text
digital_passport/
├── app.py              # Flask Backend (Cookie Logic)
├── requirements.txt    # Dependencies (Flask)
├── static/
│   ├── css/
│   │   └── style.css   # Theme variables and layout
│   └── js/
│       └── script.js   # Client-side cookie handling
└── templates/
    └── dashboard.html  # Main UI

```

---

### 🎯 Detailed Task Breakdown

#### **ST-02: Persistent Identity (The Entry Stamp)**

* **Requirement:** Capture user name and "Home Airport."
* **Logic:** In `app.py`, use `response.set_cookie('visitor_name', name, max_age=60*60*24*30)`.
* **Validation:** Open DevTools -> Application -> Cookies. Ensure the "Expires / Max-Age" column shows a date 30 days in the future.

#### **ST-03: Signed Sessions (The Diplomatic Bag)**

* **Requirement:** Prevent users from manually adding "Illegal Items" to their suitcase via the console.
* **Logic:** Use `flask.session['suitcase']`.
* **Validation:** Notice that the `session` cookie in DevTools is a long, unreadable string. Try to delete one character from that string and refresh; the app should effectively "log you out" or clear the suitcase because the signature is now invalid.

#### **ST-06: Security Flags (The Border Control)**

* **Requirement:** A "Vault Key" that is immune to XSS (Cross-Site Scripting).
* **Logic:** `resp.set_cookie('vault_key', 'SECRET123', httponly=True, samesite='Lax')`.
* **Validation:** Open the Browser Console and type `console.log(document.cookie)`. You should see the name and theme, but **not** the `vault_key`.

---
