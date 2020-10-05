
#WILL ONLY WORK IF YOU TURN OFF THE TWO FACTOR AUTHENTICATION!

import imaplib


M=imaplib.IMAP4_SSL("imap.gmail.com")


import getpass


email=getpass.getpass("email : ")
password=getpass.getpass("password: ")


M.login(email,password)

M.select("INBOX")
typ,data=M.search(None,'SUBJECT "This is a python test"')
email_id=data[0]
result,email_id=M.fetch(email_id,"(RFC882)")


