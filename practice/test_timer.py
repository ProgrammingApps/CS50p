'''
Testing the timer  (Week 5: pytest, testing edge cases, pytest.raises)

Goal: write tests for parse() in timer.py so thorough that a bug can't sneak past them.

Steps:

Import parse from timer.
Write at least three test functions, each for one kind of case:
  - valid durations
  - badly formatted input (wrong shape)
  - well-formed but out-of-range input
Use pytest.raises for the invalid cases.
Think about boundaries: the values right at the edge of valid (and right past it).

Run:  uv run --with pytest pytest test_timer.py

Then break it on purpose (mutation testing):
  1. In timer.py, sabotage the seconds check (e.g. let 60 through). Do your tests fail? They should.
  2. Undo it. Now make parse accept "1:3". Do your tests catch that?
  3. Undo it. Invent your own sabotage.
Any sabotage that your tests don't catch means a test is missing. Add it.

Reflect: what would happen when pytest imports timer.py if it had no __name__ guard?
'''
