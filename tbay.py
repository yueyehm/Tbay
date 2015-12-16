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
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    bids = relationship("Bid", uselist=True, backref="item")
    
    
class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    items = relationship("Item", uselist=True, backref="owner")
    bids = relationship("Bid", backref = "bidder")
    
class Bid(Base):
    __tablename__ = "bid"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    item_id = Column(Integer, ForeignKey('item.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

Base.metadata.create_all(engine)

