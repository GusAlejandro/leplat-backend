from sqlalchemy import Column, ForeignKey, Integer, String, LargeBinary
from sqlalchemy.orm import declarative_base, relationship
import bcrypt
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String, primary_key=True)
    username = Column(String, unique=True)
    password = Column(LargeBinary)

    def __init__(self, username, raw_password):
        self.username = username
        self.password = User.hash_password(raw_password)
        self.id = str(uuid.uuid4())
        


    @staticmethod
    def hash_password(raw_password):
        bytes = raw_password.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(bytes, salt)
    
    def is_password(self, raw_password):
        bytes = raw_password.encode('utf-8')
        return bcrypt.checkpw(bytes, self.password)

