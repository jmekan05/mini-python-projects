import time
import sys

lines = [
  ("My prized possession", 0.08),
  ("One and only", 0.10),
  ("Adore ya", 0.10),
  ("Girl, I want ya", 0.08),
  ("The one I can't live without, that's you, that's you", 0.08),
  ("You're my special little lady", 0.09),
  ("The one that makes me crazy", 0.09),
  ("Of all the girls I've ever known, it's you, it's you", 0.09),
  ("My favorite, my favorite, my favorite", 0.09),
  ("My", 0.09), ("  favorite", 0.05), ("     girl", 0.05),
  ("My", 0.09), ("  favorite", 0.10), ("     girl", 0.10)
]


delays = [0.05, 0.3, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.2, 0.5, 0.3]

def print_lyrics():
  for i, (line, char_delay) in enumerate(lines):
    for char in line:
      print(char, end='')
      sys.stdout.flush()
      time.sleep(char_delay)
    time.sleep(delays[i])
    print('')
print_lyrics()