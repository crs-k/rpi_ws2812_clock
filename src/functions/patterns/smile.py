import time
from functions.hardware import LED_COUNT
from functions.strip import turn_off
from rpi_ws281x import Color

ROWS = 4
COLS = 8
assert LED_COUNT == ROWS * COLS, "LED_COUNT does not match the size of the matrix"

def display(num_times, led_strip):
    try:
        # Define the smiley face pattern
        smiley_face = [
            [0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 0]
        ]

        # Define the colors
        colors = [Color(255, 0, 0), Color(0, 255, 0), Color(0, 0, 255)]  # Red, Green, Blue

        color_index = 0

        for j in range(num_times):
            # Iterate over the LEDs in the matrix
            for row in range(ROWS):
                for col in range(COLS):
                    # Set the color of the LED based on the smiley face pattern
                    if smiley_face[row][col] == 1:
                        color = colors[color_index]  # Color for the smiley face
                    else:
                        color = Color(0, 0, 0)  # Black for the background

                    led_strip.setPixelColor(row * COLS + col, color)

            # Update the strip to display the new colors
            led_strip.show()

            # Change the color every 2 seconds
            time.sleep(2)
            color_index = (color_index + 1) % len(colors)

    except KeyboardInterrupt:
        turn_off(led_strip)
    finally:
        turn_off(led_strip)