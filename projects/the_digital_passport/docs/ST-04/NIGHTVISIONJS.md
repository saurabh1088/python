# ST-04 : Night Vision (JS)

---

In **ST-04**, the project explores the **Client-Side** aspect of state management. While the previous tasks focused on the server (Python) setting the rules, this task demonstrates how **JavaScript** can independently read and write cookies to update the UI instantly without a page refresh.

### 🎭 The Goal: Night Vision (Dark Mode)
The objective is to implement a theme toggle that:
1.  **Instantly updates** the website's look using CSS Variables.
2.  **Saves the choice** in a cookie using JavaScript (`document.cookie`).
3.  **Remains persistent** so the user doesn't have to toggle it every time they navigate.

---

### 1. The CSS Variables (`static/css/style.css`)
First, CSS variables (Custom Properties) are defined. This allows the theme to be switched by simply changing a class on the `<body>` tag.

```css
/* Default Light Theme */
:root {
    --bg-color: #f4f7f6;
    --text-color: #333;
    --card-bg: #ffffff;
    --accent-color: #2c3e50;
}

/* Dark Theme Variables */
body.dark-mode {
    --bg-color: #1a1a1a;
    --text-color: #e0e0e0;
    --card-bg: #2d2d2d;
    --accent-color: #3498db;
}

body {
    background-color: var(--bg-color);
    color: var(--text-color);
    transition: background 0.3s ease;
    font-family: sans-serif;
}

.container {
    background: var(--card-bg);
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
```

---

### 2. The JavaScript Logic (`static/js/script.js`)
This script handles the "Write" and "Read" operations on the client side. 



```javascript
// Function to set a cookie via JavaScript
function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        let date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    // Security Note: SameSite=Lax is a modern standard requirement
    document.cookie = name + "=" + (value || "") + expires + "; path=/; SameSite=Lax";
}

// Function to get a cookie value by name
function getCookie(name) {
    let nameEQ = name + "=";
    let ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

// Toggle logic
document.addEventListener('DOMContentLoaded', () => {
    const themeBtn = document.getElementById('theme-toggle');
    
    // Check if a theme cookie already exists on load
    const savedTheme = getCookie('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
    }

    themeBtn.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        
        // Determine the new state and save it
        const isDark = document.body.classList.contains('dark-mode');
        setCookie('theme', isDark ? 'dark' : 'light', 7);
    });
});
```

---

### 3. Update the Template (`templates/dashboard.html`)
The button is added and the script is linked at the bottom of the body.

```html
<button id="theme-toggle" class="btn-secondary">🌙 Toggle Night Vision</button>

<script src="{{ url_for('static', filename='js/script.js') }}"></script>
```

---

### ✅ ST-04 Completion Checklist
* [x] **CSS Variables:** The UI responds to the `.dark-mode` class.
* [x] **JavaScript Cookie Handler:** `setCookie` and `getCookie` functions are implemented.
* [x] **Event Listener:** The button successfully toggles the class and updates the cookie.

### 🧪 The "Instant Memory" Test
1.  Open the dashboard and click **Toggle Night Vision**.
2.  Open DevTools -> Application -> Cookies. A new cookie named `theme` should appear with the value `dark`.
3.  Refresh the page.
4.  **Observation:** Because of the `DOMContentLoaded` logic in `script.js`, the theme remains dark immediately after the page loads.
