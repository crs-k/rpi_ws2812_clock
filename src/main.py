from functions.patterns.clock import display as clock_display
from functions.patterns.random import display as random_display

from functions.hardware import strip

if __name__ == "__main__":
    strip_obj = strip()
    strip_obj.begin()

    clock_display(5, strip_obj)
    random_display(32, strip_obj)