import webbrowser
from config import DATA_FILE, LOG_FILE, APP_NAME
from .contacts import ContactManager
from .emergency import build_sos_message, build_checkin_message
from .location import maps_url
from .safety_manager import SafetyManager
from .utils import setup_logger

def ask_coordinates():
    lat = float(input("Latitude: ").strip())
    lon = float(input("Longitude: ").strip())
    return lat, lon

def run_app():
    logger = setup_logger(LOG_FILE)
    contacts = ContactManager(DATA_FILE)
    manager = SafetyManager(logger)

    while True:
        print(f"\n=== {APP_NAME} ===")
        print("1. Add emergency contact")
        print("2. View emergency contacts")
        print("3. SOS emergency alert")
        print("4. Safety check-in")
        print("5. Generate location link")
        print("6. Record safety incident")
        print("7. Exit")

        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                name = input("Contact name: ")
                phone = input("Phone number: ")
                relation = input("Relationship: ")
                contacts.add(name, phone, relation)
                print("✅ Contact saved.")

            elif choice == "2":
                items = contacts.load()
                if not items:
                    print("No contacts added yet.")
                for i, c in enumerate(items, 1):
                    print(f"{i}. {c['name']} | {c['relation']} | {c['phone']}")

            elif choice == "3":
                name = input("Your name: ")
                lat, lon = ask_coordinates()
                message = build_sos_message(name, lat, lon)
                prepared = manager.prepare_alerts(contacts.load(), message)
                print("\n" + message)
                print(f"\n📨 Prepared alerts for {len(prepared)} emergency contact(s).")
                print("For real SMS delivery, connect an authorized SMS provider or Android SMS layer.")

            elif choice == "4":
                name = input("Your name: ")
                use_location = input("Include location? (y/n): ").lower() == "y"
                if use_location:
                    lat, lon = ask_coordinates()
                    print(build_checkin_message(name, lat, lon))
                else:
                    print(build_checkin_message(name))

            elif choice == "5":
                lat, lon = ask_coordinates()
                url = maps_url(lat, lon)
                print(url)
                if input("Open in browser? (y/n): ").lower() == "y":
                    webbrowser.open(url)

            elif choice == "6":
                description = input("Describe the incident: ")
                manager.record_incident(description)
                print("📝 Incident recorded locally.")

            elif choice == "7":
                print("Stay safe. Goodbye!")
                break
            else:
                print("Please choose a valid option.")
        except (ValueError, IndexError) as exc:
            print(f"❌ {exc}")
