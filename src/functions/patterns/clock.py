import datetime
import random
import time
from functions.strip import turn_off
from rpi_ws281x import Color


def draw_digit(start, digit, led_strip):
    # Define the digit patterns in terms of LED indices
    digits = [
        [0, 1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 31, 27, 23, 19, 15],  # 0
        [2, 6, 10, 14, 18, 22, 26, 30],  # 1
        [0, 1, 2, 3, 7, 11, 15, 19, 23, 27, 28, 29, 30, 31],  # 2
        [0, 1, 2, 3, 7, 11, 15, 19, 23, 27, 31, 30, 29, 28],  # 3
        [0, 4, 8, 12, 16, 20, 24, 28, 29, 30, 31, 7, 11, 15],  # 4
        [3, 2, 1, 0, 4, 8, 12, 16, 20, 24, 28, 29, 30, 31],  # 5
        [3, 2, 1, 0, 4, 8, 12, 16, 20, 24, 28, 31, 27, 23, 19, 15],  # 6
        [0, 1, 2, 3, 7, 11, 15, 19, 23, 27],  # 7
        [0, 1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 31, 27, 23, 19, 15, 7, 11],  # 8
        [0, 1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 31, 27, 23, 19, 15, 7, 11]  # 9
    ]

    # Turn off all LEDs in the 8x4 section
    for i in range(start, led_strip.numPixels()):
        led_strip.setPixelColor(i, Color(0, 0, 0))

    # Turn on the LEDs for the digit pattern
    for i in digits[digit]:
        led_strip.setPixelColor(start + i, Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    led_strip.show()

def display(num_times, led_strip):
    try:
        for _ in range(num_times):
            now = datetime.datetime.now()
            hours = now.hour
            minutes = now.minute

            # Display hours
            draw_digit(0, hours // 10, led_strip)
            draw_digit(8, hours % 10, led_strip)

            # Display minutes
            draw_digit(16, minutes // 10, led_strip)
            draw_digit(24, minutes % 10, led_strip)

            time.sleep(1)
    except KeyboardInterrupt:
        turn_off(led_strip)
    finally:
        turn_off(led_strip)
