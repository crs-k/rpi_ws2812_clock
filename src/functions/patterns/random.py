import random
import time
from functions.hardware import LED_COUNT
from functions.strip import turn_off
from rpi_ws281x import Color


def display(num_times, led_strip):
    try:
        for _ in range(num_times):
           # Pick a random LED
           led = random.randint(0, LED_COUNT - 1)

           # Randomly decide whether to turn on or off the LED
           if random.choice([True, False]):
            # Turn on the LED with a random color and "brightness"
            brightness = random.random()
            color = Color(int(random.randint(0, 255) * brightness), 
                          int(random.randint(0, 255) * brightness), 
                          int(random.randint(0, 255) * brightness))
            led_strip.setPixelColor(led, color)

           else:
               # Turn off the LED
               led_strip.setPixelColor(led, Color(0, 0, 0))
           # Update the strip to display the new color
           led_strip.show()

           # Wait for a short period of time
           time.sleep(0.1)
    except KeyboardInterrupt:
        turn_off(led_strip)
    finally:
        turn_off(led_strip)
