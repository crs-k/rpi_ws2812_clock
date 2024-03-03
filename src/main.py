from functions.patterns.clock import display as clock_display
from functions.patterns.random import display as random_display

from functions.hardware import strip

if __name__ == "__main__":
    strip_obj = strip()
    strip_obj.begin()

    patterns.clock.display(5)
    patterns.random.display(32)
    patterns.clock.display(5)
    patterns.random.display(32)