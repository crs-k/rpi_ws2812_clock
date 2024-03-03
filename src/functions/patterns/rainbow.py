import time
from functions.strip import turn_off
from rpi_ws281x import Color

def wheel(pos):
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def display(led_strip, wait_ms=20, iterations=1):
    try:
        for j in range(256*iterations):
            for i in range(led_strip.numPixels()):
                led_strip.setPixelColor(i, wheel((i+j) & 255))
            led_strip.show()
            time.sleep(wait_ms/1000.0)
    except KeyboardInterrupt:
        turn_off(led_strip)
    finally:
        turn_off(led_strip)