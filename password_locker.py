#! python3
# password_locker.py - An insecure password locker program

PASSWORDS = {'email': 'SomeTextThatIDontWantToWriteFromTheBook',
             'blog': 'AnotherTextThatIDontWantToWriteFromTheBook',
             'luggage': '12345'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account to clipboard')
    sys.exit()

account = sys.argv[1] #first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password fpr ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)