import time
import random
from functions.hardware import LED_COUNT
from functions.strip import turn_off
from rpi_ws281x import Color

ROWS = 4
COLS = 8
assert LED_COUNT == ROWS * COLS, "LED_COUNT does not match the size of the matrix"

# Define the bitmaps for the characters
char_bitmaps = {
    'L': [[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 1, 1, 0]],
    'O': [[0, 1, 1, 0],
          [1, 0, 0, 1],
          [1, 0, 0, 1],
          [0, 1, 1, 0]],
    'G': [[0, 1, 1, 1],
          [1, 0, 0, 0],
          [1, 0, 1, 1],
          [0, 1, 1, 0]],
    'A': [[0, 1, 1, 0],
          [1, 0, 0, 1],
          [1, 1, 1, 1],
          [1, 0, 0, 1]],
    'N': [[1, 0, 0, 1],
          [1, 1, 0, 1],
          [1, 0, 1, 1],
          [1, 0, 0, 1]],
    ' ': [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]
}

def display(text, led_strip, display_time):
    try:
        # Convert the text to a list of bitmaps, adding a space between each character
        bitmaps = [char for char in text] + [' ']
        bitmaps = [char_bitmaps[char] for char in bitmaps]

        # Add a column of 'off' LEDs between each character
        bitmaps_with_spaces = []
        for bitmap in bitmaps:
            bitmaps_with_spaces.append(bitmap)
            bitmaps_with_spaces.append(char_bitmaps[' '])

        # Iterate over the columns of the bitmaps
        for col in range(len(bitmaps_with_spaces) * 4 + COLS):
            # Iterate over the LEDs in the matrix
            for row in range(ROWS):
                for x in range(COLS):
                    # Calculate the color of the LED based on the bitmaps
                    if 0 <= col - x < len(bitmaps_with_spaces) * 4 and bitmaps_with_spaces[(col - x) // 4][row][(col - x) % 4] == 1:
                        # Generate a random shade of purple
                        r = random.randint(128, 255)
                        g = 0
                        b = random.randint(128, 255)
                        color = Color(r, g, b)
                    else:
                        color = Color(0, 0, 0)  # Black for the background

                    # Set the color of the LED, reversing the order of the LEDs in each row
                    led_strip.setPixelColor(row * COLS + (COLS - 1 - x), color)

            # Update the strip to display the new colors
            led_strip.show()

            # Wait for a short period of time
            time.sleep(display_time / (len(bitmaps_with_spaces) * 4 + COLS))

    except KeyboardInterrupt:
        turn_off(led_strip)
    finally:
        turn_off(led_strip)