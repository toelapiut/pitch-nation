from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

##In here we will have our Class that contain instances

class User(UserMixin,db.Model):
  __tablename__='users'
  id=db.Column(db.Integer,primary_key=True)
  username=db.Column(db.String(255))
  email=db.Column(db.String(255),unique=True,index=True)
  role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
  pass_secure=db.Column(db.String(Length(min=7,max=80)))

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


class Role(db.Model):
  __tablename__='roles'
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(255))
  user=db.relationship('User',backref='role',lazy='dynamic')

  def __repr__(self):
    return f'User {self.name}


