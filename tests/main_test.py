import unittest
from unittest.mock import MagicMock, patch
import datetime
from src.main import draw_digit, display_time

class TestDrawDigit(unittest.TestCase):
    def test_draw_digit(self):
        # Mock the strip object
        strip = MagicMock()

        # Test for each digit
        for digit in range(10):
            with self.subTest(digit=digit):
                draw_digit(strip, 0, digit)

                # Check that setPixelColor was called at least once
                self.assertTrue(strip.setPixelColor.called)

                # Check that show was called once
                strip.show.assert_called_once()

                # Reset the mock object for the next sub-test
                strip.reset_mock()

if __name__ == '__main__':
    unittest.main()

class TestDisplayTime(unittest.TestCase):
    def test_display_time(self):
        # Mock the strip object
        strip = MagicMock()

        # Call the function
        display_time(strip, iterations=5)

        # Check that setPixelColor was called at least once
        self.assertTrue(strip.setPixelColor.called)

        # Check that show was called at least once
        self.assertTrue(strip.show.called)

if __name__ == '__main__':
    unittest.main()