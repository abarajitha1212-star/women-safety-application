import json
from pathlib import Path
from .utils import valid_phone

class ContactManager:
    def __init__(self, path: str):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self):
        if not self.path.exists():
            return []
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return []

    def save(self, contacts):
        self.path.write_text(json.dumps(contacts, indent=2), encoding="utf-8")

    def add(self, name: str, phone: str, relation: str):
        if not name.strip() or not valid_phone(phone):
            raise ValueError("Enter a valid name and phone number.")
        contacts = self.load()
        contacts.append({"name": name.strip(), "phone": phone.strip(), "relation": relation.strip()})
        self.save(contacts)

    def remove(self, index: int):
        contacts = self.load()
        if index < 0 or index >= len(contacts):
            raise IndexError("Invalid contact number.")
        contacts.pop(index)
        self.save(contacts)
