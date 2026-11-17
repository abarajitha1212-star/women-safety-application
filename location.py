from urllib.parse import quote

def validate_coordinates(latitude: float, longitude: float) -> None:
    if not (-90 <= latitude <= 90):
        raise ValueError("Latitude must be between -90 and 90.")
    if not (-180 <= longitude <= 180):
        raise ValueError("Longitude must be between -180 and 180.")

def maps_url(latitude: float, longitude: float) -> str:
    validate_coordinates(latitude, longitude)
    return f"https://www.google.com/maps?q={latitude},{longitude}"

def location_text(latitude: float, longitude: float) -> str:
    return f"📍 My current location: {maps_url(latitude, longitude)}"
