from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from modera.util import get_hashed_password
from modera.db import create_session

Base = declarative_base()

class User(Base):
    __tablename__ = 'modera_auth_user'
    
    user_id = Column(Integer, Sequence('modera_auth_user_id_seq'), 
            primary_key=True)
    fullname = Column(String(200))
    username = Column(String(50))
    password = Column(String(255))
    
    def __init__(self, fullname, username, password, hash_password=True):
        self.fullname = fullname
        self.username = username
        self.password = get_hashed_password(password) if hash_password \
                else password

    def __repr__(self):
        return "User(%d, %s, %s, %s)" % (
            self.user_id, repr(self.fullname), 
            repr(self.username), repr(self.password))

def authenticate(username, password):
    session = create_session()
    password = get_hashed_password(password)
    try:
        user = session.query(User).filter_by(
                username=username, password=password).one()
    except (MultipleResultsFound, NoResultFound) as e:
        user = None
    return user
