import os
import smtplib


os.environ['EMAIL_USER'] = ''
os.environ['EMAIL_PASS'] = ''


sender_email = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASS')

receiver_email = 'manishbissau04@gmail.com'
subject = 'Simple Email'
body = 'Hello, this is a simple email sent using Python and os module.'

message = f"Subject: {subject}\n\n{body}"

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("Email sent successfully!")

except Exception as e:
    print("Error:", e)
