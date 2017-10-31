from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import db
from . import login_manager

##In here we will have our Class that contain instances

class User(UserMixin,db.Model):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(255))
	email=db.Column(db.String(255),unique=True,index=True)
	bio=db.Column(db.String(255))
	profile_pic_path=db.Column(db.String(255))
	pass_secure=db.Column(db.String(80))
	result_id=db.Column(db.Integer,db.ForeignKey('results.id'))

	@property
	def password(self):
		raise AttributeError('You cannot read the attribute')

	@password.setter
	def password(self,password):
		self.pass_secure=generate_password_hash(password)

	def verify_password(self,password):
		return check_password_hash(self.pass_secure,password)

	@login_manager.user_loader
	def loader_user(user_id):
		return User.query.get(int(user_id))


	def __repr__(self):
		return f'User {self.username}'


class Result(db.Model):
	__tablename__='results'
	id=db.Column(db.Integer,primary_key=True)
	review=db.Column(db.String(255))
	voteup=db.Column(db.Integer)
	votedown=db.Column(db.Integer)
	user=db.relationship('User',backref='result',lazy='dynamic')


	def __repr__(self):
		return f'User{self.review}'

