import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = to_email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email@gmail.com', 'your_app_password')
    server.sendmail('your_email@gmail.com', to_email, msg.as_string())
    server.quit()