import time
import sys

lines = [
  ("Everyone else in the room can see it", 0.09),
  ("Everyone else but you", 0.10),
  ("Baby, you light up my world like nobody else", 0.075),
  ("The way that you flip your hair gets me overwhelmed", 0.065),
  ("But when you smile at the ground, it ain't hard to tell", 0.06),
  ("You don't know, oh-oh", 0.08),
  ("You don't know you're beautiful", 0.06),
  ("If only you saw what I can see", 0.075),
  ("You'll understand why I want you so desperately", 0.07),
  ("Right now I'm looking at you and I can't believe", 0.07),
  ("You don't know, oh-oh", 0.08),
  ("You don't know you're beautiful", 0.06),
  ("Oh-Oh", 0.14),
  ("That's what makes you beautiful", 0.063),
]


delays = [0.5, 1.0, 0.65, 0.5, 0.5, 0.75, 0.45, 0.5, 0.5, 0.5, 0.8, 1.0, 0.6, 0.5]

def print_lyrics():
  for i, (line, char_delay) in enumerate(lines):
    for char in line:
      print(char, end='')
      sys.stdout.flush()
      time.sleep(char_delay)
    time.sleep(delays[i])
    print('')
print_lyrics()