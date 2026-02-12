from .extensions import db


class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_name = db.Column(db.String(120), nullable=False)
    platform = db.Column(db.String(50), nullable=False)
    budget = db.Column(db.Float, nullable=False)
    impressions = db.Column(db.Integer, nullable=False)
    clicks = db.Column(db.Integer, nullable=False)
    leads = db.Column(db.Integer, nullable=False)
    conversions = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
