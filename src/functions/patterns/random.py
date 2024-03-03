import random
import time
from src.functions.strip import strip, LED_COUNT, turn_off
from rpi_ws281x import Color

def display(num_times):
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
            strip.setPixelColor(led, color)

           else:
               # Turn off the LED
               strip.setPixelColor(led, Color(0, 0, 0))
           # Update the strip to display the new color
           strip.show()

           # Wait for a short period of time
           time.sleep(0.1)
    except KeyboardInterrupt:
        turn_off(strip)
    finally:
        turn_off(strip)
