import re
import email.utils

for _ in range(int(raw_input())):
    name_, email_ = email.utils.parseaddr(raw_input())
    # print name_, email_
    if re.match(r'[a-z][a-z0-9_.-]+@[a-z]+\.[a-z]{1,3}$', email_, re.IGNORECASE):
        print email.utils.formataddr((name_, email_))
