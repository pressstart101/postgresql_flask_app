from email.mime.text import MIMEText
import smtplib


def send_email(email,income, average_income, count):
	from_email="YOUREMAIL@gmail.com"
	from_password="YOURPASSWORD"
	to_email=email

	subject="Income data"
	message="Hey there, your income is <strong>%s</strong>. <br> Average income of all is %s and that is calculated out of <strong>%s</strong> of people. Thanks!" % (income, average_income, count)


	msg=MIMEText(message, 'html')
	msg['Subject']=subject
	msg["To"]=to_email
	msg["From"]=from_email


	gmail=smtplib.SMTP('smtp.gmail.com',587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(from_email, from_password)
	gmail.send_message(msg)