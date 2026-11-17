import tempfile
import unittest
from pathlib import Path

from safety_app.location import validate_coordinates, maps_url
from safety_app.emergency import build_sos_message, build_checkin_message

class TestSafetyApplication(unittest.TestCase):
    def test_valid_coordinates(self):
        validate_coordinates(13.0827, 80.2707)

    def test_invalid_coordinates(self):
        with self.assertRaises(ValueError):
            validate_coordinates(100, 80)

    def test_maps_url(self):
        self.assertIn("13.0827,80.2707", maps_url(13.0827, 80.2707))

    def test_sos_message(self):
        msg = build_sos_message("Demo User", 13.0827, 80.2707)
        self.assertIn("EMERGENCY ALERT", msg)
        self.assertIn("google.com/maps", msg)

    def test_checkin(self):
        self.assertIn("safe", build_checkin_message("Demo User").lower())

if __name__ == "__main__":
    unittest.main()
