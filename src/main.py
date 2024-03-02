import datetime
import random
import time
from rpi_ws281x import Adafruit_NeoPixel, Color


# LED strip configuration:
LED_COUNT      = 32      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 10    # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

def draw_digit(strip, start, digit):
    # Define the digit patterns in terms of LED indices
    digits = [
        [0, 1, 2, 4, 6, 8, 9, 10],  # 0
        [2, 6, 10],  # 1
        [0, 1, 2, 5, 6, 8, 9, 10],  # 2
        [0, 1, 2, 5, 6, 9, 10],  # 3
        [0, 2, 4, 5, 6, 10],  # 4
        [1, 2, 4, 5, 6, 9, 10],  # 5
        [0, 1, 2, 4, 5, 6, 8, 9, 10],  # 6
        [2, 6, 10],  # 7
        [0, 1, 2, 4, 5, 6, 8, 9, 10],  # 8
        [0, 1, 2, 4, 5, 6, 10]  # 9
    ]

    # Turn off all LEDs in the 8x4 section
    for i in range(start, start + 32):
        strip.setPixelColor(i, Color(0, 0, 0))

    # Turn on the LEDs for the digit pattern
    for i in digits[digit]:
        strip.setPixelColor(start + i, Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    strip.show()

def display_time(strip, iterations=1):
    try:
        for _ in range(iterations):
            now = datetime.datetime.now()
            hours = now.hour
            minutes = now.minute

            # Display hours
            draw_digit(strip, 0, hours // 10)
            draw_digit(strip, 8, hours % 10)

            # Display minutes
            draw_digit(strip, 16, minutes // 10)
            draw_digit(strip, 24, minutes % 10)

            time.sleep(1)
    except KeyboardInterrupt:
        # Turn off all LEDs
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()

if __name__ == "__main__":
    strip.begin()

    display_time(strip)