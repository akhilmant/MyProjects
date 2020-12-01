import smtplib
import getpass
#Establish the connection to the mail
test=smtplib.SMTP("smtp.gmail.com",587)
#using ehlo to greet the server 
test.ehlo()
#TLS is a type of encryption 
test.starttls()
email=getpass.getpass("Email:")
password=getpass.getpass("Password:")
test.login(email,password)
from_address=email
to_address=getpass.getpass("Enter the receiver's email:")
subject=input("Subject:")
body=input("body:")
msg="subject:" + subject + "\n" + body
test.sendmail(from_address,to_address,msg,)
test.quit()