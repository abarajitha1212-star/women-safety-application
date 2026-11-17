# Architecture

```text
User
  |
  v
CLI (cli.py)
  |
  +--> ContactManager ----> JSON contact storage
  |
  +--> Emergency module --> SOS / check-in messages
  |
  +--> Location module ---> Maps URL
  |
  +--> SafetyManager -----> Incident log + prepared alerts
  |
  v
Local files / external browser
```

The design keeps UI, location logic, contact storage, emergency-message generation, and safety records separated so each part can be tested and extended independently.
