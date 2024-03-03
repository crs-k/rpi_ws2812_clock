import time
from functions.hardware import LED_COUNT
from functions.strip import turn_off
from rpi_ws281x import Color

ROWS = 4
COLS = 8
assert LED_COUNT == ROWS * COLS, "LED_COUNT does not match the size of the matrix"

def display(num_times, led_strip):
    try:
        for j in range(num_times):
            # Iterate over the layers of the matrix from the outside to the center
            for layer in range(min(ROWS, COLS) // 2):
                # Iterate over the LEDs in the current layer in a spiral order
                for i in spiral_order(layer, ROWS, COLS):
                    # Calculate the color based on the LED's position in the spiral
                    red = ((i + j) % LED_COUNT * 255) // LED_COUNT
                    green = ((LED_COUNT - (i + j) % LED_COUNT) * 255) // LED_COUNT
                    blue = ((i + j) % LED_COUNT * 255) // LED_COUNT

                    # Set the color of the LED
                    color = Color(red, green, blue)
                    led_strip.setPixelColor(i, color)

            # Update the strip to display the new colors
            led_strip.show()

            # Wait for a short period of time
            time.sleep(0.1)
    except KeyboardInterrupt:
        turn_off(led_strip)
    finally:
        turn_off(led_strip)

def spiral_order(layer, rows, cols):
    # Calculate the dimensions of the current layer
    rows -= layer * 2
    cols -= layer * 2

    # Iterate over the top row from left to right
    for col in range(layer, layer + cols):
        yield layer * COLS + col

    # Iterate over the right column from top to bottom
    for row in range(layer + 1, layer + rows):
        yield row * COLS + layer + cols - 1

    if rows > 1:
        # Iterate over the bottom row from right to left
        for col in range(layer + cols - 2, layer - 1, -1):
            yield (layer + rows - 1) * COLS + col

    if cols > 1:
        # Iterate over the left column from bottom to top
        for row in range(layer + rows - 2, layer, -1):
            yield row * COLS + layer