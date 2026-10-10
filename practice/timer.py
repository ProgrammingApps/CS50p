'''
Timer  (Week 3: exceptions, raising your own, re-prompting)

Goal: convert a duration written as MM:SS into total seconds.

Steps:

Prompt with "Duration: ". If the input is invalid, prompt again (as many times as needed).
Print the result as "90 seconds".

Structure:

    def main(): ...           # the loop, the try/except, the printing
    def parse(duration): ...  # returns an int number of seconds,
                              # or RAISES ValueError if invalid (it never prints, never loops)

Rules for a valid duration:
  - exactly one colon
  - minutes: a whole number, 0 or more, any number of digits
  - seconds: exactly two digits, 00–59

Examples:

1:30    → 90 seconds
01:30   → 90 seconds
0:59    → 59 seconds
125:00  → 7500 seconds
2:60    → invalid (re-prompt)
1:3     → invalid
-1:30   → invalid
1:30:00 → invalid
abc     → invalid

Include an  if __name__ == "__main__":  guard. You'll find out why in the next exercise.

Reflect: some invalid inputs raise ValueError "for free" without you writing a raise.
Which ones, and why?
'''
