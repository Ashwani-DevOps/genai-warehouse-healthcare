import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, body, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'ashwanikumarm@gmail.com'
    msg['To'] = to_email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ashwanikumarm@gmail.com', 'IamfromThane#6')  # Use app password
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    server.quit()
    # for Testing yes