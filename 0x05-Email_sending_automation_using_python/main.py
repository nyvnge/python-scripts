import tweepy
import smtplib
import ssl
from email.mime.text import MIMEText

#Twitter API Credentials
consumer_key = 'ani8GL6cn90Rl5uM3emxr1F4C'
consumer_secret = '8nJr3ItjY06bbVJCUTEVBuu8k69jE8VOM8ih3rB7kVWWBEFU4H'
access_token = '1589515639164641280-JZoILPq4TqO41EYJ2n8GYI9dEeYw9w'
access_token_secret = 'rGgkZDNDc1IU5S8XWHt6PogEcPWCspbkaY23P1JCxbLEJ'

#Email Sender and Email receiver info
emailSender = 'sandersonnyangejr@gmail.com'
emailPassword = 'sgllvyykiknfrcsl'
emailReceiver = 'sanywalkerke@gmail.com'

#Function to fetch latest tweets
def getLatestTweets():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name = 'MenMoneyMindset', count=1)
    if tweets:
        return tweets[0].text
    else:
        return None
    
#Subject and body of the email
subject = 'Daily Motivational Tweets'

#Get latest tweet content body
latest_tweet = getLatestTweets()

if latest_tweet:
    body = f"""Continue growing champ!\n\n{latest_tweet}"""
else:
    body = "No recent tweets found. "

#MIMEText object
msg = MIMEText(body, 'html')
msg['From'] = emailSender
msg['To'] = emailReceiver
msg['Subject'] = subject

#Adding SSL security
context = ssl.create_default_context()

#Sending email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(emailSender, emailPassword)
    smtp.sendmail(emailSender, emailReceiver, msg.as_string())