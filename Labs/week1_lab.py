# =============================================================================
# ENGR1210 — Introduction to Programming
# Morse Code Translator Project
# Week 1 Lab: Variables and Simple Data Types
# Chapter 2 — Python Crash Course, 3rd Edition
#
# HOW THIS FILE WORKS
# =============================================================================
# This file IS your lab. Read it top to bottom. Run it with F5.
# Each section builds on the one before it.
#
# SECTION 1 — ANCHOR      (fully worked — read, run, understand)
# SECTION 2 — GUIDED      (partially complete — fill in the blanks)
# SECTION 3 — EXTENSION   (working code — add a small piece)
# SECTION 4 — STRETCH     (open-ended — design it yourself)
#
# The rule: you must be able to EXPLAIN every line you submit.
# If you can run it but not explain it, you're not done yet.
#
# HOW THIS COURSE IS BUILT  (read this once — it explains everything)
# =============================================================================
# For the next several weeks you will build a Morse code translator as
# a PLAIN SCRIPT — top to bottom, no functions, no imports, no extra
# files. You will use only what the textbook has taught so far:
#
#   Week 1: variables & types     Week 4: if / elif / else
#   Week 2: lists                  Week 5: dictionaries
#   Week 3: loops over lists       Week 6: while loops & input
#
# Then in Week 7 ("Functions"), once you have a working script, you will
# learn to REFACTOR it: wrap the logic in functions and split it into
# modules (separate .py files). That is also when the hardware layer
# appears. You will literally turn the script you are about to start
# into a real, reusable program — and you will understand WHY functions
# exist, because you will have lived without them first.
#
# So when you see a note like "(Week 7: this becomes a function)",
# that is a promise, not a missing piece. For now, write it inline.
#
# THE BIGGER PICTURE
# =============================================================================
#   Text in -> encode -> "LED" blinks -> read signal -> decode -> text out
#
# Week 1 builds the foundation: timing constants and project metadata.
# This week the "LED" is just a printed line. Real hardware comes later.
# =============================================================================


# =============================================================================
# SECTION 1 — ANCHOR
# Fully worked example. Read every line. Run it. Study the output.
# Then answer the three questions in the comments before moving on.
# =============================================================================

print("=" * 52) 
print("SECTION 1: ANCHOR — Timing Constants")
print("=" * 52)

# -- What is Morse code timing? --------------------------------------------
# Morse code is defined entirely by TIMING RATIOS.
# The dot (.) is the base unit. Everything else is a multiple of it.
#
# ITU-R M.1677 standard ratios:
#   DOT          = 1 unit  (the base)
#   DASH         = 3 units
#   SYMBOL GAP   = 1 unit  (pause between dots/dashes within a letter)
#   LETTER GAP   = 3 units (pause between letters)
#   WORD GAP     = 7 units (pause between words)
#
# We store the base unit in milliseconds so we can tune speed by
# changing ONE variable. Everything else is calculated from it.

DOT_MS        = 50          # base unit: one dot = 100 milliseconds
DASH_MS       = DOT_MS * 3   # a dash is 3 dot durations = 300ms
SYMBOL_GAP_MS = DOT_MS * 1   # gap within a letter = 100ms
LETTER_GAP_MS = DOT_MS * 3   # gap between letters = 300ms
WORD_GAP_MS   = DOT_MS * 7   # gap between words = 700ms

# Print the timing table (just sequential print statements — no loop yet;
# loops arrive in Week 3).
print(f"\nBase unit (DOT_MS): {DOT_MS}ms")
print(f"{'Symbol':<15} {'Duration':>10}ms {'Ratio':>8}")
print("-" * 36)
print(f"{'dot':<15} {DOT_MS:>10}    {'1x':>8}")
print(f"{'dash':<15} {DASH_MS:>10}    {'3x':>8}")
print(f"{'symbol gap':<8} {SYMBOL_GAP_MS:>10}    {'1x':>8}")
print(f"{'letter gap':<15} {LETTER_GAP_MS:>10}    {'3x':>8}")
print(f"{'word gap':<15} {WORD_GAP_MS:>10}    {'7x':>8}")

# -- Our first "LED" -------------------------------------------------------
# For now the LED is just text. In Week 7 this single print becomes a
# function call into a hardware module that you can swap for a real Pico.
print("\n[LED] ON")
print("[LED] OFF")

# -- ANCHOR QUESTIONS (discuss with your partner before continuing) --------
# Q1. Change DOT_MS to 50. What happens to DASH_MS and WORD_GAP_MS?
#     Why does this work without changing any other lines?
#  They also cut into half of there original value, this is beacuse they are directly linked to the Dot value. 
# Q2. What does the :<15 in the f-string format specifier do?
#     Try changing 15 to 8 and observe what happens to the output.
#  It formats the table below, the :< means spaces to the right of the previous text, the :<15 means it will move the text 15 spaces to the right. 
# Q3. Every other timing variable is calculated from DOT_MS instead of
#     being typed in as a fixed number. Why is that safer than writing
#     DASH_MS = 300 directly?
#  They are linked together like that so you can easily adjust the speed by only changing 1 number and keeping all of the ratios the same. 

# =============================================================================
# SECTION 2 — GUIDED
# The structure is given. Fill in every line marked # TODO.
# Week 1 has generous hints — hints get shorter each week.
# =============================================================================

print("\n" + "=" * 52)
print("SECTION 2: GUIDED — Project Banner and Metadata")
print("=" * 52)

# -- Step 1: Define project metadata variables ------------------------------
# Store the information below in correctly-typed variables.
# Use str for text, int for whole numbers, bool for True/False.
# Book reference: p. 19-22 (variables), p. 29-31 (numbers)

PROJECT_NAME = "Morse Code Translator"   # str  <- this one is done for you

# TODO: store your own first and last name as two separate string variables
FIRST_NAME   = "Drake"    # TODO: replace "" with your first name
LAST_NAME    = "Mellen"    # TODO: replace "" with your last name

# TODO: store the version string "0.1.0"
VERSION      = "0.1.0"    # TODO

# TODO: store the target board name "Pi Pico"
TARGET_BOARD = "Pi Pico"    # TODO

# TODO: store True if you are running on your PC (not real hardware yet).
#       Right now that is always the case.
ON_PC        = True  # TODO: replace None with the correct boolean

# TODO: store the number of letters in the Morse alphabet as an integer.
# Hint: count A through Z
ALPHABET_SIZE = 26    # TODO: replace 0 with the correct count

# -- Step 2: Print a formatted project banner -------------------------------
# Expected output (with your name and correct values):
#
#   ====================================================
#   Morse Code Translator v0.1.0
#   Student: Jordan Smith
#   Board:   Pi Pico
#   Mode:    PC (VS Code)
#   Alphabet: 26 letters
#   ====================================================
#
# Rules:
#   - Use f-strings for ALL values (no hardcoded text)
#   - Combine FIRST_NAME and LAST_NAME using .title()
#   - For the mode line, build the text with a conditional expression:
#       mode_str = "PC (VS Code)" if ON_PC else "Pico (hardware)"
# Book reference: p. 23-28 (strings), p. 32-34 (f-strings)

print("=" * 52)

# TODO: print the project name and version on one line
# Hint: f"{PROJECT_NAME} v{VERSION}"
print (f"{PROJECT_NAME} v{VERSION}")   # TODO: replace with f-string

# TODO: print the student name using FIRST_NAME and LAST_NAME (use .title())
print(FIRST_NAME.title(), LAST_NAME.title())    # TODO

# TODO: print the target board
print(TARGET_BOARD)    # TODO

# TODO: build the mode string, then print it
mode_str = "PC (VS Code)" if ON_PC else "Pico (hardware)"   # TODO: use the conditional expression shown above
print(mode_str)        # TODO: then print it

# TODO: print the alphabet size
print(ALPHABET_SIZE)    # TODO

print( "=" * 52)


# =============================================================================
# SECTION 3 — EXTENSION
# The code below works. Your job: add one small piece using the same style.
# (No functions yet — just variables and arithmetic. Week 7 turns this
#  calculation into a reusable function.)
# =============================================================================

print("\n" + "=" * 52)
print("SECTION 3: EXTENSION — Transmission Time of One Letter")
print("=" * 52)

# -- Existing working code -------------------------------------------------
# How long does it take to send the letter A?  A is dot-dash ( .- ).
# That is: a dot, then a symbol gap, then a dash.
# We add the three durations together with plain arithmetic.

a_dot_part  = DOT_MS
a_gap_part  = SYMBOL_GAP_MS
a_dash_part = DASH_MS
a_total_ms  = a_dot_part + a_gap_part + a_dash_part

print(f"\nLetter A ( .- ):")
print(f"  dot {a_dot_part}ms + gap {a_gap_part}ms + dash {a_dash_part}ms")
print(f"  total = {a_total_ms}ms")

# -- YOUR EXTENSION --------------------------------------------------------
# Calculate the transmission time for the letter U, whose pattern is ..- .
# U is: dot, symbol gap, dot, symbol gap, dash.
# Build it the same way: one variable per part, then add them up.
# Finally, print the breakdown and the total, like the example above.
#
# (Week 7: you will replace this hand-counting with a function that
#  takes ANY pattern string and loops over it. For now, do it by hand —
#  it makes the function you write later much easier to understand.)

# TODO: create variables for each part of the letter U and a total
u_dot_part  = DOT_MS
u_gap_part  = SYMBOL_GAP_MS
u_dash_part = DASH_MS
u_total_ms  = u_dot_part + u_gap_part + u_dot_part + u_gap_part + u_dash_part
# TODO: print the breakdown and total for U
print(f"\nLetter U ( ..- ):")
print(f"  dot {u_dot_part}ms + gap {u_gap_part}ms + dot {u_dot_part}ms + gap {u_gap_part}ms + dash {u_dash_part}ms")
print(f"  total = {u_total_ms}ms")

# =============================================================================
# SECTION 4 — STRETCH
# No starter code. No hints. Design it yourself.
# This section is optional but strongly recommended.
# =============================================================================

print("\n" + "=" * 52)
print("SECTION 4: STRETCH — Words-Per-Minute Speed")
print("=" * 52)

# -- Challenge -------------------------------------------------------------
# Morse speed is measured in WPM (words per minute). The standard test
# word "PARIS" takes exactly 50 dot units to send, which gives:
#
#       WPM = 1200 / DOT_MS        (when DOT_MS is in milliseconds)
#
# Using ONLY variables and arithmetic (no functions, no loops yet):
#
#   1. Calculate the current WPM from DOT_MS and print it nicely,
#      e.g. "At DOT_MS=100, speed is 12 WPM".
#
#   2. Suppose you want to send at 5 WPM. Rearrange the formula to find
#      the DOT_MS you would need, and print it. (Check: 5 WPM -> 240ms.)
#
#   3. Print a small "speed card" of three fixed speeds using separate
#      print lines (one each for 5, 12, and 20 WPM) showing the DOT_MS
#      for each. (Week 3, with loops, you'll turn this into a real table.)
#
# Bonus: change DOT_MS at the top of the file from 100 to 50 and re-run.
# Confirm your WPM line updates automatically. Why does it?

# TODO: implement the stretch challenge here


# =============================================================================
# WHAT I BUILT THIS WEEK — Checklist
# =============================================================================
#   [Y] ANCHOR:    I ran the anchor code and can explain every line
#   [Y] ANCHOR:    I answered all three anchor questions
#   [Y] GUIDED:    All metadata variables are filled in and correctly typed
#   [Y] GUIDED:    The banner prints with my name and correct values
#   [Y] EXTENSION: The letter U transmission time prints correctly
#   [Y] STRETCH:   (optional) WPM speed calculations implemented
#   [Y] I can explain my code to a partner without looking at it
#
# =============================================================================
# LOOKING AHEAD — Week 2
# =============================================================================
# Next week you learn LISTS, and you'll store the Morse codebook — every
# letter and its dot/dash pattern — as a list. Keep this file: your
# DOT_MS timing constants carry forward into the whole project.
#
# And remember the promise: in Week 7 the inline calculations you wrote
# this week become reusable FUNCTIONS, and the project splits into MODULES.
# =============================================================================
