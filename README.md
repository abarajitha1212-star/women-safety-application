# 🛡️ Women Safety Application

A Python-based safety assistant designed to help a user quickly prepare an emergency alert, share a location link, notify trusted emergency contacts, and record safety incidents.

## ✨ Features

- 🚨 One-action SOS workflow
- 📍 Location sharing using a Google Maps link
- 👥 Emergency contact management
- 💬 Personalized emergency message generation
- 📱 SMS-ready notification workflow
- 🕐 Safety check-in / safe-status message
- 📝 Incident report recording
- 🔐 Local data stored outside Git history
- 📋 Input validation and error handling
- 🧪 Unit tests
- 🧩 Clean modular architecture

## 🛠️ Technology

- Python 3.10+
- Python standard library
- JSON for local contact storage
- `webbrowser` for opening map/message links
- `unittest` for testing

## 📁 Project Structure

```text
women-safety-application/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── safety_app/
│   ├── __init__.py
│   ├── cli.py
│   ├── emergency.py
│   ├── location.py
│   ├── contacts.py
│   ├── safety_manager.py
│   └── utils.py
├── tests/
│   └── test_safety_manager.py
├── data/
│   └── contacts.example.json
├── logs/
│   └── .gitkeep
└── docs/
    ├── ARCHITECTURE.md
    ├── PROJECT_REPORT.md
    └── SOURCES.md
```

## ▶️ Run

```bash
python app.py
```

The program provides a menu for managing contacts, creating an SOS alert, generating a location link, sending a safe check-in message, and recording incidents.

## 📍 Location Sharing

The application accepts latitude and longitude and generates a Google Maps URL. It does **not** silently access a user's GPS. This keeps the demo privacy-friendly.

Example:

```text
https://www.google.com/maps?q=13.0827,80.2707
```

## 📱 Emergency Notification

For this GitHub project, the application creates a notification message and an SMS-ready link. Actual SMS delivery requires a phone/SMS provider or an Android application with the appropriate permissions.

The project intentionally does not contain real phone numbers, API keys, passwords, or private credentials.

## 🧪 Testing

```bash
python -m unittest discover -s tests -v
```

## 🔐 Privacy & Safety

- Do not commit real emergency contact data.
- Do not put API keys or passwords in source code.
- Use trusted contacts only.
- Verify local emergency numbers before relying on an emergency workflow.
- This project is an educational safety assistant, not a replacement for emergency services.

## 🎓 Learning Outcomes

This project demonstrates:

- Python modular programming
- File handling and JSON
- Validation
- Exception handling
- Logging
- Unit testing
- URL construction
- Basic software architecture
- Privacy-aware application design
- Git/GitHub project organization

## 🚀 Future Enhancements

- Android GPS integration
- Real SMS provider integration
- Push notifications
- Trusted-contact authentication
- Secure encrypted local storage
- Background safety check-ins
- Optional wearable integration
- Cloud backend with authentication
