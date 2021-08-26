import os

class Config:
        SECRET_KEY=os.environ.get('SECRET_KEY')
	MAIL_USERNAME='jumabarrak17@gmail.com'
 	MAIL_PASSWORD='barry@1234'
 	DATABASE_URL=''
	SQLALCHEMY_DATABASE_URL =''