#! python3
# bulletPointAdder.py - Adds wikipedia buller points to the start of each line of text one the clipboard
import pyperclip
text = pyperclip.paste()

#separate lines and add stars

pyperclip.copy(text)

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)