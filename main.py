import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import traceback
import sys

# Error reporting to file
logging.basicConfig(filename='error.log', level=logging.ERROR)

# Email settings
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
FROM_EMAIL = 'your_email@gmail.com'
PASSWORD = 'your_password'
TO_EMAIL = 'recipient_email@gmail.com'

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(FROM_EMAIL, PASSWORD)
    text = msg.as_string()
    server.sendmail(FROM_EMAIL, TO_EMAIL, text)
    server.quit()

def error_reporting(error):
    logging.error(error)
    subject = 'Error Report'
    body = f'Error: {error}\n\n{traceback.format_exc()}'
    send_email(subject, body)

try:
    # Your code here
    x = 1 / 0
except Exception as e:
    error_reporting(str(e))
```

Kodda quyidagilar mavjud:

1. Error reporting to file: Kodda `logging` moduli ishlatiladi, unda `basicConfig` funksiyasi oraliqda `error.log` fayli yaratib, unda xatolar yoziladi.
2. Email settings: Kodda email settings mavjud, unda `SMTP_SERVER`, `SMTP_PORT`, `FROM_EMAIL`, `PASSWORD`, `TO_EMAIL` kabi parametralar belgilangan.
3. `send_email` funksiyasi: Kodda `send_email` funksiyasi mavjud, unda email yuborish uchun `smtplib` moduli ishlatiladi.
4. `error_reporting` funksiyasi: Kodda `error_reporting` funksiyasi mavjud, unda xatolar yoziladi va emailga yuboriladi.
