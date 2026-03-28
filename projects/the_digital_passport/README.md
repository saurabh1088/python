# 🌍 The Digital Passport: A Cookie Laboratory

A professional-grade Flask application designed to demonstrate the lifecycle, security, and synchronization of HTTP state management.

## 🚀 Overview
The Digital Passport is a travel-themed web app that replaces traditional databases with advanced browser-side state management. It serves as a technical deep-dive into how modern web applications maintain identity, security, and performance using only HTTP headers.

## 🛠️ Technical Stack
- **Backend:** Python 3.11+ / Flask
- **Frontend:** HTML5, CSS Variables, Vanilla JavaScript
- **Security:** HMAC-signed Sessions, HttpOnly/SameSite Cookie Flags

## 🏗️ Architectural Milestones (The "ST" Series : Sub Tasks)
- **ST-01/02:** Implementation of Persistent Identity using `max_age` cookies.
- **ST-03:** Deployment of Signed Sessions to ensure data integrity for a "Virtual Suitcase."
- **ST-04/05:** Full-stack synchronization of UI themes to eliminate Flash of Unstyled Content (FOUC).
- **ST-06:** Security hardening of sensitive tokens using the `HttpOnly` protocol.
- **ST-07:** Engineered a secure "Data Erasure" mechanism for session termination.
- **ST-08:** Built an integrated Telemetry/Dev-Console for real-time state observability.

## 🛡️ Security Features
- **Tamper Protection:** Cryptographic signing of session cookies prevents manual value manipulation.
- **XSS Mitigation:** Sensitive "Vault Keys" are isolated from the DOM via `HttpOnly`.
- **CSRF Protection:** Strict `SameSite` policies enforced on all state-altering cookies.

## 🚦 Getting Started
1. Clone the repository.
2. Initialize virtual environment: `python -m venv venv`.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the lab: `python app.py`.
