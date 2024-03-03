import time
from functions.hardware import LED_COUNT
from functions.strip import turn_off
from rpi_ws281x import Color

ROWS = 4
COLS = 8
assert LED_COUNT == ROWS * COLS, "LED_COUNT does not match the size of the matrix"

def display(display_time, led_strip):
    try:
        # Define the American flag pattern
        flag = [
            [0, 1, 0, 1, 2, 2, 2, 2],  # 1 = white star, 0 = blue, 2 = red stripe
            [1, 0, 1, 0, 3, 3, 3, 3],
            [0, 1, 0, 1, 2, 2, 2, 2],  # 3 = white stripe
            [1, 0, 1, 0, 3, 3, 3, 3]
        ]

        # Define the colors
        colors = [Color(0, 0, 255), Color(255, 255, 255), Color(255, 0, 0), Color(255, 255, 255)]  # Blue, White, Red, White

        # Iterate over the LEDs in the matrix
        for row in range(ROWS):
            for col in range(COLS):
                # Set the color of the LED based on the flag pattern
                color = colors[flag[row][col]]
                led_strip.setPixelColor(row * COLS + col, color)

        # Update the strip to display the new colors
        led_strip.show()

        # Display the flag for the specified number of seconds
        time.sleep(display_time)

    except KeyboardInterrupt:
        turn_off(led_strip)
    finally:
        turn_off(led_strip)