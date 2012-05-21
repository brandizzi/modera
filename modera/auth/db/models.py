from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
	__tablename__ = 'modera_auth_user'
	
	user_id = Column(Integer, sequence=Sequence('modera_auth_user_id_seq'), 
	        primary_key=True)
	fullname = Column(String(200))
	username = Column(String(50))
	password = Column(String(255))
	
	def __init__(self, fullname, username, password):
	    self.fullname = fullname
	    self.username = username
	    self.password = password	
    
    def __repr__(self):
        return "User(%d, %s, %s, %s)" % (
            self.user_id, repr(self.fullname), 
            repr(self.username), repr(self.password))

