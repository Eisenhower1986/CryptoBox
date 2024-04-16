import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config

def send_email(subject, message, to_email):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'your-email@gmail.com'  # 发件人邮箱地址
    sender_password = 'your-password'      # 发件人邮箱密码

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Failed to send email:", str(e))

# Example usage
if __name__ == '__main__':
    subject = 'Test Email'
    message = 'This is a test email message.'
    to_email = 'recipient@example.com'
    send_email(subject, message, to_email)
