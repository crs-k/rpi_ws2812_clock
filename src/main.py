from functions.patterns.clock import display as clock_display
from functions.patterns.random import display as random_display
from functions.patterns.spiral import display as spiral_display
from functions.patterns.smile import display as smile_display
from functions.patterns.flag import display as flag_display
from functions.patterns.logan import display as logan_display
from functions.patterns.wave import display as wave_display
from functions.patterns.rainbow import display as rainbow_display
from functions.hardware import strip

if __name__ == "__main__":
    strip_obj = strip()
    strip_obj.begin()

    clock_display(5, strip_obj)
    random_display(32, strip_obj)
    spiral_display(60, strip_obj)
    smile_display(5, strip_obj)
    flag_display(5, strip_obj)
    logan_display("LOGAN", strip_obj, 4)
    wave_display(strip_obj)
    rainbow_display(strip_obj, wait_ms=20, iterations=1)
