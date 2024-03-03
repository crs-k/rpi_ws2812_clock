import time
from rpi_ws281x import Color
from functions.hardware import LED_COUNT
from functions.strip import turn_off

def display(led_strip, start_color=Color(255, 0, 0), end_color=Color(0, 0, 255), delay=0.1):
    try:
        # Calculate the color change per LED
        r_step = (end_color.r - start_color.r) / LED_COUNT
        g_step = (end_color.g - start_color.g) / LED_COUNT
        b_step = (end_color.b - start_color.b) / LED_COUNT

        for i in range(0, LED_COUNT * 2):
            # Turn on LEDs
            for j in range(max(0, i - LED_COUNT + 1), min(i + 1, LED_COUNT)):
                # Calculate the color of the LED
                r = int(start_color.r + r_step * (j - i + LED_COUNT - 1))
                g = int(start_color.g + g_step * (j - i + LED_COUNT - 1))
                b = int(start_color.b + b_step * (j - i + LED_COUNT - 1))
                color = Color(r, g, b)

                led_strip.setPixelColor(j, color)

            # Turn off the LED that is 'LED_COUNT' LEDs behind
            if i - LED_COUNT >= 0:
                led_strip.setPixelColor(i - LED_COUNT, Color(0, 0, 0))

            led_strip.show()
            time.sleep(delay)

        # Turn off the remaining LEDs
        for i in range(LED_COUNT, LED_COUNT * 2):
            led_strip.setPixelColor(i - LED_COUNT, Color(0, 0, 0))
            led_strip.show()
            time.sleep(delay)

    except KeyboardInterrupt:
        turn_off(led_strip)
    finally:
        turn_off(led_strip)