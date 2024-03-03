import unittest
from unittest.mock import MagicMock, call, patch

class TestTurnOff(unittest.TestCase):
    def setUp(self):
        self.strip = MagicMock()
        self.strip.numPixels.return_value = 5

    @patch('src.functions.hardware.strip', new_callable=MagicMock)
    def test_turn_off(self, mock_strip):
        mock_strip.numPixels.return_value = 5
        from src.functions.strip import turn_off
        turn_off(mock_strip)
        calls = [call(i, 0) for i in range(5)]
        mock_strip.setPixelColor.assert_has_calls(calls)
        mock_strip.show.assert_called_once()

if __name__ == '__main__':
    unittest.main()