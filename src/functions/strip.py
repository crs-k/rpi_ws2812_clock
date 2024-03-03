from src.functions.hardware import strip
from rpi_ws281x import Color


def turn_off():
    # Turn off all LEDs
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()