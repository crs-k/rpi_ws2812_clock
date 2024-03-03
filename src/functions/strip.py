from rpi_ws281x import Color


def turn_off(led_strip):
    # Turn off all LEDs
    for i in range(led_strip.numPixels()):
        led_strip.setPixelColor(i, Color(0, 0, 0))
    led_strip.show()