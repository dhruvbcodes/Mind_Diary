import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st

def send_email(email, report, auth):
    try:
        # Set up the server
        pwd=st.secrets["AUTH_TOKEN"]
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login("rohituwuskrtt@gmail.com", pwd)

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = "rohituwuskrtt@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Your Patient's report for today"

        # Create the body of the email
        body = f"Hi Doctor,  \n Check out your patients' status today!! \nDo not reply back to this email. \n\n Your patient is having a {report} mood today.\n\nRegards\nMindDiary"
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.send_message(msg)
        server.quit()
        return True

    except Exception as e:
        print(f"Error sending email: {e}")
        return False
