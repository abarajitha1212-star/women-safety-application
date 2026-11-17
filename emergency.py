from datetime import datetime
from .location import maps_url

def build_sos_message(user_name, latitude, longitude):
    link = maps_url(latitude, longitude)
    return (
        f"🚨 EMERGENCY ALERT from {user_name}!\n"
        f"I may need immediate help. Please contact me and check my location.\n"
        f"Location: {link}\n"
        f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

def build_checkin_message(user_name, latitude=None, longitude=None):
    message = f"✅ Safety check-in: {user_name} is safe."
    if latitude is not None and longitude is not None:
        message += f"\nLocation: {maps_url(latitude, longitude)}"
    return message
