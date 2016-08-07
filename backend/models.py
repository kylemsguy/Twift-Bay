from sqlalchemy.dialects.postgresql import JSON

from application import db


class TwitterUser(db.Model):
    __tablename__ = 'twitter_user'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(), index=True, nullable=False, unique=True)
    personality_data = db.Column(JSON)


class EbayProduct(db.Model):
    __tablename__ = 'ebay_product'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, index=True, nullable=False, unique=True)
    product_name = db.Column(db.String())
    product_price = db.Column(db.Float)
    product_img_link = db.Column(db.String())
    product_description = db.Column(db.String(), default='')
    product_url = db.Column(db.String())
    personality_data = db.Column(JSON)
    times_suggested = db.Column(db.Integer, default=0)
    times_clicked = db.Column(db.Integer, default=0)
