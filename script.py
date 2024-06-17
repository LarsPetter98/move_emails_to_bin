import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv
import os

#Loading environment variables from the .env file
load_dotenv()

#Access environment variables
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

#Connect to the server
mail = imaplib.IMAP4_SSL("imap.mail.yahoo.com") #Yahoo mail imap server
mail.login(username, password)

#Selecting folder in yahoo mail
mail.select("inbox")

#Searching the inbox for all email. "None" is for the character format, "ALL" is the search criteria
mail_sender = "customerservice@books.nextory.com"
mail_sender2 = "english-personalized-digest@quora.com"
mail_sender3 = "jippi5000@gmail.com"
status, messages = mail.search(None, f'FROM "{mail_sender3}"')

""" if messages:
    latest_email_num = messages[-1]  #Get the last (latest) message number
    print(latest_email_num)
    status, latest_email_data = mail.fetch(latest_email_num, "(RFC822)")  #Fetch the latest email
    mail.store(latest_email_num, "+FLAGS", "\\Deleted") """

#Getting the id for each emal
email_ids = messages[0].split()

#Placing a copy of the email with the corresponding id in the bin, then adding the "Deleted" flag to the same email
for email_id in email_ids:
    status, msg_data = mail.fetch(email_id, "(RFC822)")
    if status == "OK":
        print(msg_data)
    else:
        print(f"Failed to fetch email with ID {email_id}. Status: {status}")

    mail.copy(email_id, "Trash")
    mail.store(email_id, "+FLAGS", "\\Deleted")

#Places mail marked with "Deleted" flag from the inbox directory to the bin
mail.expunge()

#Closing the mailbox
mail.close()

#Loggin out from the yahoo mail server
mail.logout()

