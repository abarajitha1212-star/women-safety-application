from datetime import datetime
from pathlib import Path

class SafetyManager:
    def __init__(self, logger):
        self.logger = logger

    def record_incident(self, description: str, path="data/incidents.log"):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        entry = f"{datetime.now().isoformat()} | {description.strip()}\n"
        with open(path, "a", encoding="utf-8") as f:
            f.write(entry)
        self.logger.info("Incident recorded")
        return entry

    def prepare_alerts(self, contacts, message):
        return [{"contact": c["name"], "phone": c["phone"], "message": message} for c in contacts]
