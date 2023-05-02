import smtplib

# Get user input for sender email address, recipient email address, subject, and message
sender_email = input("Enter your email address: ")
recipient_email = input("Enter recipient email address: ")
subject = input("Enter email subject: ")
message = input("Enter email message: ")

# Connect to Google SMTP and authenticate the user
# (In Gmail the user will need to generate "app password")
smtp_server = "smtp.gmail.com"
smtp_port = 587
password = input("Enter your email password: ")
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.starttls()
smtp_connection.login(sender_email, password)

# Compose the email message
email_message = f"Subject: {subject}\n\n{message}"

# Send the email to the specified recipient
smtp_connection.sendmail(sender_email, recipient_email, email_message)
print("Thank you for using DevSecOps12! Email sent successfully!")

# Disconnect from the SMTP server
smtp_connection.quit()
