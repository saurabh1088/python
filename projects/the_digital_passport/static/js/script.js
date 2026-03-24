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
