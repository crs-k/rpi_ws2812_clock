import unittest
from unittest.mock import MagicMock, call, patch
from src.functions.strip import turn_off, Color

class TestTurnOff(unittest.TestCase):
    def setUp(self):
        self.strip = MagicMock()
        self.strip.numPixels.return_value = 5

    @patch('src.functions.strip.Adafruit_NeoPixel')
    @patch('src.functions.strip.Color')
    def test_turn_off(self, MockColor, MockNeoPixel):
        MockColor.return_value = (0, 0, 0)
        turn_off(self.strip)
        calls = [call(i, MockColor(0, 0, 0)) for i in range(5)]
        self.strip.setPixelColor.assert_has_calls(calls)
        self.strip.show.assert_called_once()

if __name__ == '__main__':
    unittest.main()