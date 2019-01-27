from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://HEROKU_CONFIG--APP_APPNAME?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
	__tablename__="data"
	id=db.Column(db.Integer, primary_key=True)
	email_=db.Column(db.String(1020),unique=True)
	income_=db.Column(db.Integer)

	def __init__(self, email_, income_):
		self.email_=email_
		self.income_=income_




@app.route("/")
def index():
	return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
	if request.method=="POST":
		email=request.form["email_name"]
		income=request.form["income_name"]
		if db.session.query(Data).filter(Data.email_==email).count() == 0:
			data=Data(email,income)
			db.session.add(data)
			db.session.commit()
			average_income=db.session.query(func.avg(Data.income_)).scalar()
			average_income=round(average_income,1)
			count=db.session.query(Data.income_).count()
			print(average_income)
			send_email(email, income, average_income, count)
			return render_template("success.html")
		return render_template('index.html', text="Seems like we've got something from this email already")	

if __name__ == '__main__':
		app.debug=True
		app.run()	