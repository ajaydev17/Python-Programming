"""
Reading a file in reverse order is useful for log files where recent events are at the
end. For smaller files, reading all lines and then reversing the list with reversed() is
straightforward. For larger files, reading the file in reverse by chunks may be more efficient,
though it requires more complex logic.

● Simple Reverse Read: For smaller files, readlines() and reversed() are sufficient.
"""

with open('example.log', 'r') as f:
    lines = f.readlines()
    reversed_lines = reversed(lines)

for line in reversed_lines:
    print(line.strip())