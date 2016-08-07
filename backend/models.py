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
    personality_data = db.Column(JSON)