# rpi_ws2812_clock

This repository contains Python code to display the current time on an LED strip using a Raspberry Pi.

## Dependencies

This project depends on the `rpi_ws281x` library, which is a Python wrapper for the rpi_ws281x library used to control WS281x series RGB LED strips (such as NeoPixels) from a Raspberry Pi.

You can install the required libraries using pip:

```bash
pip install rpi_ws281x
```

## Configuration

The LED strip configuration can be adjusted in the `main.py` file:

```python
# LED strip configuration:
LED_COUNT      = 32      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 10      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
```

## Usage

To run the program, navigate to the project directory in your terminal and run the `main.py` file:

```bash
python main.py
```

This will start the LED clock display. The display will continue until a `KeyboardInterrupt` (typically triggered by a Ctrl+C command) is detected, at which point all the LEDs on the strip will be turned off.

## License

This project is licensed under the terms of the MIT license.
