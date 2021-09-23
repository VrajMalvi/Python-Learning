# link 1 : https://docs.python.org/3/library/email.examples.html
# link 2: https://docs.python.org/3/library/email.html#module-email

# NOTE do not name the email code file to email.py it will give error

import smtplib  # creates smtp server
from email.message import EmailMessage
from string import Template  # with this we can substitute var with $sign
from pathlib import Path  # similar to os.path


# now we can access index.html file
html = Template(
    Path('17_Scripting-with-python/3_send_Emails/index.html').read_text())
email = EmailMessage()
email['from'] = 'vraj malvi'
email['to'] = 'vrajmalvi08@gmail.com'
email['subject'] = 'you won 1,000,000 $'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('zerotomastery1@gmail.com', 'helloztmmyoldfriend1')
    smtp.send_message(email)
    print('all good!')
