# Finds all the email addresses in the clipboard text
#
# Select the text you want to find email addresses in, copy it,
# run this script (python get_email_from_clipboard.py), and then paste

import pyperclip, re

email_regex = re.compile(r'([\w\.\-%+]+@([\w]+\.)+[\w]+)')

text = str(pyperclip.paste())
matches = []

print(text)

for groups in email_regex.findall(text):
    matches.append(groups[0])

if len(matches) >0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard')
    print('\n'.join(matches))
else:
    print('no email addresses')
