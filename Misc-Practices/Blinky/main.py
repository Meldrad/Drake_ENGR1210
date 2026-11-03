# =============================================================================
# ENGR 1210 - Blinky
# =============================================================================
# GOAL
#   Blink an LED 
# =============================================================================

#import hal_pc as hw
import hal_pico as hw  # uncomment this line to run on the real Pico 2


print("Board:", hw.board_info())      # tells you which world the HAL picked

hw.set_led(True)