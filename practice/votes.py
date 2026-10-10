'''
Votes  (Weeks 2–3: dicts, while True, EOFError, sorting)

Goal: tally votes typed in one per line, then announce the result.

Steps:

Repeatedly prompt with "Vote: " until the user presses ctrl-D (that raises EOFError).
Votes are case-insensitive and should ignore surrounding spaces ("  alice " == "Alice").
Ignore blank lines.
After ctrl-D, print each candidate in alphabetical order with their count,
capitalised, like:  Alice: 3
Then print the winner: "Winner: Alice"
If two or more candidates tie for the most votes, print them all: "Tie: Alice, Bob"
If no votes were cast at all, print "No votes cast" and nothing else.

Example:

Vote: alice
Vote: Bob
Vote:  ALICE
Vote:
Vote: carol
Vote: bob
^D
Alice: 2
Bob: 2
Carol: 1
Tie: Alice, Bob

Reflect: what's the difference between counts[name] and counts.get(name)? When would each blow up?
'''
