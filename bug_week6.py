# bug_week6.py
# BUG OF THE WEEK - Week 6: User Input and while Loops
#
# INSTRUCTIONS: This file has 4 bugs in it.
# Bug 1: Find with the console error message.
# Bug 2: Find with the VS Code Debugger.
# Bug 3: Find with the VS Code Debugger — WARNING: infinite loop risk.
#         Read the debugger instructions BEFORE running this one.
# Bug 4: Can ONLY be found by running a complete set of TEST CASES.
#
# ============================================================
# STANDARD DEBUGGING PROCESS (review):
#   STEP 1: Run — read error type and line number.
#   STEP 2: Fix ONE bug, save, run again.
#   STEP 3: Repeat until no crashes.
#   STEP 4: CHECK YOUR OUTPUT. Running ≠ correct.
#
# VS CODE DEBUGGER (review):
#   Set breakpoint : click gray margin left of line number
#   Start          : F5  →  Python File
#   Step Over      : F10
#   Continue       : F5
#   STOP           : Shift+F5   ← IMPORTANT this week (see Bug 3)
#   Variables panel: left sidebar while paused
#
# ============================================================
# NEW THIS WEEK: INFINITE LOOPS AND THE DEBUGGER
#
# A while loop keeps running AS LONG AS its condition is True.
# If the condition NEVER becomes False, the loop runs forever.
# This is called an INFINITE LOOP.
#
# Symptoms in VS Code:
#   - The program appears to "hang" — no output, no error
#   - The terminal shows a spinning cursor or no prompt
#   - VS Code's stop button becomes active
#
# How to escape an infinite loop:
#   - In the terminal:      Ctrl+C
#   - In the VS Code debugger: Shift+F5  (Stop)
#
# How to FIND an infinite loop with the debugger:
#   1. Set a breakpoint INSIDE the while loop body.
#   2. Press F5 to start.
#   3. Press F10 a few times — watch the loop variable in
#      the Variables panel. Is it changing? Is it moving
#      toward making the condition False? hmmmmm
#   4. If the same values keep repeating, you have found
#      your infinite loop. Press Shift+F5 to stop.
#
# ============================================================
# BUILDING ON TEST CASES FROM WEEK 5:
#
# Last week: first, middle, last, missing, edge
# This week we add two new categories specific to loops:
#
#   BOUNDARY — the exact value where behavior should change
#              (e.g., age == 3 exactly, or quantity == 0)
#   EMPTY    — what happens when the input list/collection
#              starts out empty? Does the loop handle it
#              gracefully, or does it crash or behave oddly?
#
# Test case categories so far (running list for the semester):
#   first | middle | last | missing | edge | boundary | empty
# ============================================================


# ============================================================
# THE PROGRAM: a simple sandwich order system
#
# Customers enter sandwich orders one at a time.
# The system processes orders, tracks what's been made,
# and applies a discount for large orders (5 or more).
# ============================================================

# ============================================================
# BUG 1 — Find with: console error message 
#
# HINT: Read about getting numerical input (p. 120-121).
#       input() ALWAYS returns a string, even if the user
#       types a number. What function converts a string to
#       an integer? Where should it be applied here?
# ============================================================
print("--- Sandwich Order System ---")
num_orders = input("How many sandwiches would you like to order? ")

# Bug is here: num_orders is a string — you can't compare
# a string to an integer with >
if num_orders > "0":
    print(f"Great! Let's get started on {num_orders} sandwiches.")
else:
    print("No sandwiches ordered.")


# ============================================================
# BUG 2 — Find with: VS Code Debugger
#
# The sandwich queue below should contain exactly these orders:
#   ["turkey", "veggie", "roast beef", "grilled cheese"]
# But when you loop through it, one sandwich is wrong.
# No crash — just wrong data quietly sitting in the list.
#
# DEBUGGER INSTRUCTIONS:
#   1. Set a breakpoint on: current = sandwich_queue.pop(0)
#   2. Press F5. In the Variables panel, watch sandwich_queue.
#   3. Press F10 each iteration. What does sandwich_queue
#      look like after each pop()? What does 'current' hold?
#   4. Compare what you see to what the list should contain.
#
# HINT: Read about working with lists in while loops (p. 128-129).
#       Look very carefully at the sandwich_queue definition.
#       One entry has a subtle typo — it won't cause a crash
#       but it will make a customer unhappy.
# ============================================================
print("\n--- Processing Orders ---")
sandwich_queue = ["turkey", "veggie", "roast beef", "grilled cheese"]
finished = []

while sandwich_queue:
    current = sandwich_queue.pop(0)
    finished.append(current)
    print(f"  Made: {current}")

print("\n--- Completed Orders ---")
for sandwich in finished:
    print(f"  {sandwich.title()}")


# ============================================================
# BUG 3 — Find with: VS Code Debugger (INFINITE LOOP RISK)
#
# !! READ THIS BEFORE RUNNING !!
# This section contains an infinite loop bug.
# Do NOT just press F5 and walk away.
# Use the debugger to catch it BEFORE it locks up VS Code.
#
# DEBUGGER INSTRUCTIONS:
#   1. Set a breakpoint on the line: while active:
#   2. Press F5. The debugger pauses immediately.
#   3. Check the Variables panel: what is 'active'?
#      What is 'order_count'? What is 'max_orders'?
#   4. Press F10 once to enter the loop body.
#   5. Keep pressing F10 slowly, watching the variables.
#      Ask yourself: what would need to happen for 'active'
#      to become False? Is that ever going to happen?
#   6. Press Shift+F5 to STOP before it runs away.
#
# HINT: Read about using a flag to control a while loop (p. 124-125).
#       The 'active' flag is supposed to become False when
#       order_count reaches max_orders. Trace the logic:
#       is order_count actually being updated inside the loop?
# ============================================================
print("\n--- Order Counter (max 3) ---")
max_orders  = 3
order_count = 0
active      = True

while active:
    print(f"  Order #{order_count + 1} received.")
    order_count += 1
    # BUG: order_count is never incremented — it stays 0 forever
    if order_count == max_orders:
        active = False

# The fix requires one line added inside the loop.
# Where should it go, and what should it say?


# ============================================================
# BUG 4 — Find with: TEST CASES  (boundary + empty categories)
#
# This section applies a bulk discount: orders of 5 or more
# sandwiches get 20% off. The logic looks correct at a glance,
# and it passes several casual test cases. But there are two
# specific inputs that expose the bug.
#
# STEP 1: Run the program and observe the discount output
#         for the default value (order_total = 4, qty = 5).
#         Does it look correct?
#            No
# STEP 2: Design and run these test cases by temporarily
#         changing order_total and qty below:
#
#   | Test Case          | qty | order_total | Expected          | Actual | Pass? |
#   |--------------------|-----|-------------|-------------------|--------|-------|
#   | A: Clearly above   |  8  |    40.00    | 20% off → $32.00  | $20    | Fail  |
#   | B: Clearly below   |  3  |    15.00    | No discount       |  $20   | Fail  |
#   | C: BOUNDARY (exact)|  5  |    25.00    | 20% off → $20.00  |  $20   | Pass  |
#   | D: One below bdry  |  4  |    20.00    | No discount       | $20    | Fail  |
#   | E: EMPTY (zero qty)|  0  |     0.00    | No discount       |  $20   | Fail  |
#
# STEP 3: Which test case(s) fail? What does the output show?
#  
# HINT: The discount threshold is 5 or more sandwiches.
#       Read the if condition carefully.
#       Is it using the right comparison operator for
#       "5 or more"? What is the difference between
#       > 5 and >= 5 at the exact boundary value?
#
# USE THE DEBUGGER on the failing test case:
#   1. Set a breakpoint on: if qty > 5:
#   2. Check: what is qty? What does > 5 evaluate to
#      when qty IS exactly 5? it evaluates to $20
#   3. Step Over — which branch runs?
#     The discount Branch 
# ============================================================
print("\n--- Discount Calculator ---")
order_total = int(num_orders)*5
qty         = int(num_orders)          # change this when running test cases

if qty >= 5:              # BUG: should be >= 5
    discount     = order_total * 0.20
    final_total  = order_total - discount
    print(f"  Qty: {qty}  |  Bulk discount applied!")
    print(f"  Original: ${order_total:.2f}  →  Final: ${final_total:.2f}")
else:
    print(f"  Qty: {qty}  |  No discount. Total: ${order_total:.2f}")


# ============================================================
# TEST CASE LOG — complete this as you work through Bug 4
#
#   | Test Case          | qty | order_total | Expected    | Actual | Pass? |
#   |--------------------|-----|-------------|-------------|--------|-------|
#   | A: Clearly above   |  20 |      $80    |    $80      |  $80   |   Y   |
#   | B: Clearly below   |  1  |      $5     |     $5      |     $5 |   Y   |
#   | C: Boundary exact  | 5   |     $20     |      $20    |   $20  |   Y   |
#   | D: One below bdry  |  4  |     $20     |      $20    |   $20  |   Y   |
#   | E: Empty / zero    |   0 |      $0     |       $0    |    $0  |   Y   |
#
# ============================================================
# REFLECTION QUESTIONS:
#
#   1. What was Bug 3? What are TWO different ways
#      you could fix it? (Hint: you could change the loop
#      condition OR add something inside the loop body.)
#      Which fix is more readable, and why?
#   Bug 3 was an infinite order #1 recieved loop. To fix it, you could either add a break in the loop or change the loops condition. 
#   2. Bug 4 was caused by what?
#      What kind of error is this typically called? (Hint: it's a very common type of logic error.) 
#      What are some strategies for avoiding this kind of error in the future? 
#    A logic error caused this bug. To avoid it, try to not hardcode and use rules. 
#   3. This week we added BOUNDARY and EMPTY to our test
#      case categories. Why is the boundary case (qty == 5)
#      more likely to contain a bug than qty == 8 or qty == 3?
#    Because 5 is the boundary between the discount and not discount price. 
#   4. Imagine you had to test this discount calculator for
#      a real sandwich shop. Write out ALL the test cases
#      you would run before calling the software "done."
#      Think about: what inputs could a real customer provide
#      that you might not have considered?
#      (This is the beginning of thinking like a QA engineer.)
#      I would test for 0, 1, 4, 5, 8, and 20. This covers 0, the minimum, before and after the discount condition, and 2 greater numbers. I think this covers ever branch in the code. 
# ============================================================