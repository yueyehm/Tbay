from tbay import User, Item, Bid, session

perry = User(name="Perry",password="123")
baseball = Item(name="BaseBall")
perry.items = [baseball]
jesse = User(name="Jesse",password="123")
monica = User(name="Monica",password="123")
bid1 = Bid(price=23.8,bidder=jesse,item=baseball)
bid2 = Bid(price=18.5, bidder=monica,item=baseball)

session.add_all([perry, jesse, monica, baseball, bid1, bid2])
session.commit()
highestBid = session.query(Bid).order_by(Bid.price.desc()).first()
print(highestBid.price, highestBid.bidder.name)