# Source - https://stackoverflow.com/a
# Posted by Belter, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-08, License - CC BY-SA 3.0

import smtplib
from email.message import EmailMessage
def send_mail(to_email, subject, message, server='smtp.gmail.com',
              from_email='sidnegi1971@gmail.com'):
    # import smtplib
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ', '.join(to_email)
    msg.set_content(message)
    print(msg)
    server = smtplib.SMTP(server)
    server.set_debuglevel(1)
    server.login(from_email, 'password')  # user & password
    server.send_message(msg)
    server.quit()
    print('successfully sent the mail.')
	
	# Source - https://stackoverflow.com/a
# Posted by Belter, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-08, License - CC BY-SA 3.0

send_mail(to_email=['ssnegi@yahoo.com', 'sidnegi1971@gmail.com'],
          subject='hello', message='Your analysis has done!')

