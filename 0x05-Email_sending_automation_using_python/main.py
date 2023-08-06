import smtplib
import ssl
from email.mime.text import MIMEText

# Email Sender and Email receiver info
emailSender = 'youremail@gmail.com'
emailPassword = 'yourpass'
emailReceiver = 'receiveremail'

# Subject and body of the email
subject = 'Daily Motivational Tweets'
body = """Continue growing champ!
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Be fun and confident. you will be ahead of 90% of men.</p>&mdash; Men Money Mindset (@MenMoneyMindset) <a href="https://twitter.com/MenMoneyMindset/status/1687984584817016832?ref_src=twsrc%5Etfw">August 6, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>"""

# Create a MIMEText object with HTML content
msg = MIMEText(body, 'html')
msg['From'] = emailSender
msg['To'] = emailReceiver
msg['Subject'] = subject

# Adding SSL security
context = ssl.create_default_context()

# Sending email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(emailSender, emailPassword)
    smtp.sendmail(emailSender, emailReceiver, msg.as_string())
