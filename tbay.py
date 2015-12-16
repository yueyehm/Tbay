from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    bids = relationship("Bid", uselist=True, backref="item")
    
    
class User(Base):
    __tablename__ = "Users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column
    items = relationship("Item", uselist=True, backref="owner")
    
class Bid(Base):
    __tablename__ = "Bids"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    item_id = Column(Integer, ForeignKey('Item.id'), nullable=False)

Base.metadata.create_all(engine)

