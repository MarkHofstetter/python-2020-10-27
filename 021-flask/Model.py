from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    
    
def get_session ():   
    engine = create_engine('sqlite:///sqlalchemy_student.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


if __name__ == '__main__':
    engine = create_engine('sqlite:///sqlalchemy_student.db')
    Base.metadata.create_all(engine)    


