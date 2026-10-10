# Catch-up plan: Weeks 0–6

Goal: get back up to speed after the break, then finish Week 6 (`scourgify.py`, `shirt.py`)
and continue to Week 7.

Rough time: **6–8 hours**, e.g. five or six sessions of an hour or so.

## How to do each exercise

1. Read the spec in the file's docstring.
2. **Write pseudocode as comments first**, like you did in `lines.py`. That habit is good.
3. Code it with **no notes and no looking at your old solutions**. Struggling to remember is
   what makes it stick. Open the docs or ask Claude for a *hint* only after ~10 minutes stuck.
4. Test it against every example in the spec, then try to break it with weird input.
5. Answer the **Reflect** question out loud (or in a comment). If you can't, that's your gap.
6. Tick it off below and commit.

## Session 0: recall (15 min, no code, no notes)

Answer these from memory, in a comment or on paper. Then check yourself against the
lecture notes or by testing in the Python REPL (`uv run python`). Any you got wrong are
the topics to watch for.

**Weeks 0–1**
- What's the difference between a function that `return`s a value and one that `print`s it?
- What type does `input()` always give you? How do you get a number from it?
- What do `.strip()`, `.split()` and `.lower()` each return? Do they change the original string?
- What does `f"{x:.2f}"` do? And `f"{n:02}"`?
- What's the difference between `elif` and a second `if`?

**Weeks 2–3**
- When would you use a list vs a dict?
- How do you loop over a dict's keys *and* values together?
- Walk through the order `try`, `except`, `else` blocks run in.
- What's the difference between *catching* an exception and *raising* one? When should a
  function raise instead of printing an error?
- What raises `EOFError` at the terminal?

**Weeks 4–5**
- What is `sys.argv`, and what's in `sys.argv[0]`?
- What does `if __name__ == "__main__":` protect against?
- How do you test that a function raises a `ValueError`?
- Why test edge cases like `0`, `""`, and values right at a boundary?

**Week 6**
- What does `with open(...) as file:` do for you?
- What's the difference between modes `"r"`, `"w"`, and `"a"`?
- What's the difference between `csv.reader` and `csv.DictReader`?

## The exercises

| # | File | Weeks | Concepts | Done |
|---|------|-------|----------|------|
| 1 | `receipt.py` | 0–1 | input, types, functions returning values, f-string formatting, conditionals | ☐ |
| 2 | `nutrition.py` | 2 | dicts, case-insensitive lookup | ☐ |
| 3 | `acronym.py` | 2 | loops, lists, string methods, building a result | ☐ |
| 4 | `votes.py` | 2–3 | dicts as counters, `EOFError`, sorting, ties | ☐ |
| 5 | `timer.py` | 3 | exceptions, raising your own `ValueError`, re-prompting | ☐ |
| 6 | `test_timer.py` | 5 | pytest, `pytest.raises`, boundary tests, mutation testing | ☐ |
| 7 | `dice.py` | 4 | `random`, `sys.argv`, `sys.exit` | ☐ |
| 8 | `wordfreq.py` | 6 | reading files, `with`, counting, `sorted(key=...)` | ☐ |
| 9 | `gradebook.py` | 6 | `csv.DictReader` / `DictWriter`, bad-data handling | ☐ |

Data files you'll need: `words.txt` (for 8) and `grades.csv` (for 9).

## Review your past self (30 min)

Reviewing code (including your own) is a real skill. Each file below has at least one
real issue: a bug, a gap, or something that's misleading. Find it, and explain *why* it's an issue,
before you ask Claude. Fix it yourself if you want.

- [ ] `Week6/problem_set_6/pizza.py`: look closely at what runs after `sys.exit`.
- [ ] `Week6/problem_set_6/lines.py`: run it with *zero* arguments. Is the message true?
- [ ] `Week5/problem_set_5/plates/plates_test.py`: does each test check what its name says?
- [ ] `Week5/problem_set_5/test_fuel.py`: list everything `convert` and `gauge` can do. How
      much of that is tested? Use the mutation trick from exercise 6.
- [ ] `Week4/problem_set_4/bitcoin.py`: what happens, in order, when you run it with no argument?
      What work is wasted?

## Then: back to Week 6

- [ ] `Week6/problem_set_6/scourgify.py`: exercise 9 has set you up for this.
- [ ] `shirt.py` (rewatch the Week 6 lecture section on PIL / Pillow first).
- [ ] Week 7: Regular expressions.
