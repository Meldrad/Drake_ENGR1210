# =============================================================================
# main.py  -  STARTER for this week's lab: a Morse SEND / RECEIVE station
#
# What is given to you:
#   - the exception that picks the hardware layer (hal_pico on a Pico / Wokwi,
#     hal_pc on your PC)
#   - a short DEMO that shows how to use the photoresistor
#   - the station loop that asks "send or receive?" each round
#
# What YOU write (this is the lab):
#   - send_message(message)   week 9 you wrote how to send a word, now (week 10)extend to a whole message (add word gaps)
#   - receive()               week 10, read the photoresistor and decode the message
#
# =============================================================================

# NEW in WEEK 10 - replace the hal_pico import and hal_pc imports with this try/except. 
# It will pick the right one for you, and you can run the same code on a Pico or on your PC.
try:
    import hal_pico as hw
except ImportError:
    import hal_pc as hw

import morse_code
from morse_code import WORD_GAP_MS, DOT_MS, DASH_MS, SYMBOL_GAP_MS, LETTER_GAP_MS, encode_message

# =============================================================================
# WEEK9 Lab - you sent a word
# WEEK10 Lab - extend to send a whole message
# =============================================================================
def send_message(message):
    patterns = encode_message(message)
  
    for pattern in patterns:
        if pattern == ' ':
            hw.set_led_timed(False, WORD_GAP_MS - LETTER_GAP_MS) #Word Gap (Space)
        elif pattern == '?':
            print ('?')
        else: 
            for symbol in pattern:
                if symbol == '.': 
                    hw.set_led_timed(True, DOT_MS)               # dot
                    hw.set_led_timed(False, SYMBOL_GAP_MS)       # gap after a symbol
                elif symbol == '-':
                    hw.set_led_timed(True, DASH_MS)              # dash
                    hw.set_led_timed(False, SYMBOL_GAP_MS)       # gap after a symbol
       
        hw.set_led_timed(False, LETTER_GAP_MS - SYMBOL_GAP_MS)

# =============================================================================
# WEEK10 Lab - read the photo resistor and decode the message
# =============================================================================

def receive():
    unit = morse_code.DOT_MS            # one "dot" of time, in ms
    text = ""                           # the decoded message so far
    pattern = ""                        # the dots/dashes of the letter being built
    light_on = False                    # was the light on at the last read?
    started = False                     # have we seen the first flash yet?
    change_time = hw.now_ms()           # when the light last switched on/off

    while True:
        on = hw.read_u16() > 500        # above ~500 means the light is ON

        if on != light_on:
            # The light just switched, so the thing that was happening just ended.
            duration = hw.elapsed_ms(change_time)
            change_time = hw.now_ms()

            if light_on:
                # An ON pulse ended: short = dot, long = dash
                if duration < 2 * unit:
                    pattern = pattern + "."
                else:
                    pattern = pattern + "-"
            elif started:
                # A dark gap ended: symbol gap, letter gap, or word gap
                if duration >= 5 * unit:                  # word gap (about 7 units)
                    text = text + morse_code.decode_pattern(pattern) + " "
                    pattern = ""
                elif duration >= 2 * unit:                # letter gap (about 3 units)
                    text = text + morse_code.decode_pattern(pattern)
                    pattern = ""
                # otherwise it was a symbol gap (about 1 unit): keep building

            light_on = on
            if on:
                started = True

        elif started and not light_on and hw.elapsed_ms(change_time) > 10 * unit:
            # Dark for longer than any word gap: the message is over
            if pattern != "":
                text = text + morse_code.decode_pattern(pattern)
            break

        hw.sleep_ms(morse_code.SAMPLE_MS)    # steady sampling rate

    return text


# =============================================================================
# THE MORSE CODE STATION  (given - this is how your two functions get used)
# =============================================================================
print("Board:", hw.board_info())
print("Morse station. Choose a mode each round.")

while True:
    mode = input("\n[s]end or [r]eceive? (blank to quit) ")
    mode = mode.strip().lower()
    if mode == "":
        break

    if mode == "s" or mode == "send":
        message = input("  message to SEND: ")
        message = message.strip().upper()
        if message != "":
            send_message(message)             # <-- your function flashes the LED

    elif mode == "r" or mode == "receive":
        message = input("  message being sent to you: ")
        message = message.strip().upper()
        if message != "":
            hw.play(message)                  # fake sensor: make it "see" this message
            decoded = receive()               # <-- your function reads + decodes
            print("  you received:", decoded)

    else:
        print("  please type s or r")

print("done.")
