import os
import smtplib
from email.mime.text import MIMEText

def send_notification(report_file):
    with open(report_file, 'r') as file:
        report_content = file.read()

    msg = MIMEText(report_content, 'html')
    msg['Subject'] = 'Nikto Scan Report'
    msg['From'] = 'your-email@example.com'
    msg['To'] = 'recipient@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your-email@example.com', 'your-password')
        server.send_message(msg)

    print("Notification sent successfully.")

if __name__ == "__main__":
    report_file = 'report.html'
    send_notification(report_file)
