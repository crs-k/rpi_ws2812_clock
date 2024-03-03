import unittest
from unittest.mock import MagicMock, call
from src.functions.strip import turn_off, Color

class TestTurnOff(unittest.TestCase):
    def setUp(self):
        self.strip = MagicMock()
        self.strip.numPixels.return_value = 5

    def test_turn_off(self):
        turn_off(self.strip)
        calls = [call(i, Color(0, 0, 0)) for i in range(5)]
        self.strip.setPixelColor.assert_has_calls(calls)
        self.strip.show.assert_called_once()

if __name__ == '__main__':
    unittest.main()