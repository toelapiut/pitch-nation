from . import db
from werkzeug.security import generate_password_hash,check_password_hash

##In here we will have our Class that contain instances

class User(db.Model):
  __tablename__='users'
  id=db.Column(db.Integer,primary_key=True)
  username=db.Column(db.String(255))
  role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
  pass_secure=db.Column(db.String(Length(min=7,max=80)))

  def __repr__(self):
    return f'User {self.username}'


class Role(db.Model):
  __tablename__='roles'
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(255))
  user=db.relationship('User',backref='role',lazy='dynamic')

  def __repr__(self):
    return f'User {self.name}


