import smtplib
import os
from email.mime.text import MIMEText
import time

# Email addresses and message to send
from_address = "Example Sender <example@gmail.com>"
to_address_list = []
with open("emails.txt", "r") as f:
    for line in f:
        to_address_list.append(line.strip())

subject = "Example Email Subject"

# Open plain text file for reading
with open("message.txt", "r") as f:
    text = f.read()

valid_emails = []
for to_address in to_address_list:
    if '@' not in to_address: # check if email address is valid
        print(f"{to_address} is not a valid email address, removing from list")
    else:
        valid_emails.append(to_address)

for to_address in valid_emails:
    # Create a MIMEText message
    msg = MIMEText(text)

    # Add the From, To, and Subject headers
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    try:
        # Send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("example@gmail.com", "password")
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        print(f"Successfully sent email to {to_address}")
        valid_emails.remove(to_address)
    except Exception as e:
        print(f"Failed to send email to {to_address} with error: {e}. Sleeping for 5 minutes before continuing.")
        time.sleep(300)

# write valid emails to the file
with open("emails.txt", "w") as f:
    for email in valid_emails:
        f.write(email + '\n')
